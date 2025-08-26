import argparse
import sys
import shlex

balances: dict[str, int] = {}


def repl() -> int:
    parser = build_parser()
    print("Entering interactive mode. Type 'help' or 'quit'.")
    while True:
        try:
            line = input("loyalty> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

        if not line:
            continue
        if line.lower() in {"quit", "exit"}:
            print("Bye!")
            return 0
        if line.lower() in {"help", "?"}:
            print("Commands: create <id> <points>, earn <id> <points>, redeem <id> <points>, quit")
            continue

        try:
            tokens = shlex.split(line)
            args = parser.parse_args(tokens)
            execute(args)
        except SystemExit:
            continue


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="loyalty",
        description="Customer Loyalty Points CLI"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_earn = sub.add_parser("earn", help="Add points to customer balance")
    p_earn.add_argument("customer_id", type=str)
    p_earn.add_argument("points", type=int)

    p_redeem = sub.add_parser("redeem", help="Redeem points from a customer's balance")
    p_redeem.add_argument("customer_id", type=str)
    p_redeem.add_argument("points", type=int)

    p_create = sub.add_parser("create", help="Create a new customer with an initial balance")
    p_create.add_argument("customer_id", type=str)
    p_create.add_argument("points", type=int)

    return parser


def create_customer(customer_id: str, points: int) -> int:
    if customer_id in balances:
        raise ValueError(f"Customer with {customer_id} already exists")
    if points < 0:
        raise ValueError("Initial value cannot be negative")
    balances[customer_id] = points
    return 0


def earn(customer_id: str, points: int) -> int:
    if customer_id not in balances:
        raise ValueError(f"Customer {customer_id} does not exist. Use create cmd first")
    if points < 0:
        raise ValueError("Points must be a positive int.")
    balances[customer_id] += points
    return balances[customer_id]


def redeem(customer_id: str, points: int) -> int:
    if customer_id not in balances:
        raise ValueError(f"Customer {customer_id} does not exist. Use 'create' first.")
    if points <= 0:
        raise ValueError("Points to redeem must be a positive integer.")
    current = balances[customer_id]
    if points > current:
        raise ValueError(f"Cannot redeem {points} points. Current balance is {current}.")
    balances[customer_id] = current - points
    return balances[customer_id]


def execute(args) -> int:
    if args.command == "create":
        try:
            create_customer(args.customer_id, args.points)
            print(f"Customer {args.customer_id} created with balance {args.points} points.")
            return 0
        except ValueError as e:
            print(f"Error: {e}")
            return 1

    if args.command == "earn":
        try:
            new_balance = earn(args.customer_id, args.points)
            print(f"Customer {args.customer_id} balance is now {new_balance} points.")
            return 0
        except ValueError as e:
            print(f"Error: {e}")
            return 1

    if args.command == "redeem":
        try:
            new_balance = redeem(args.customer_id, args.points)
            print(f"Customer {args.customer_id} balance is now {new_balance} points.")
            if new_balance < 10:
                print(f"Warning: Customer {args.customer_id} has a low balance: {new_balance} points.")
            return 0
        except ValueError as e:
            print(f"Error: {e}")
            return 1

    print("Unknown command.")
    return 2


def main() -> int:

    if len(sys.argv) == 1:
        return repl()

    print('CLI is live, You can start!')

    parser = build_parser()
    args = parser.parse_args()

    return execute(args)


if __name__ == "__main__":
    raise SystemExit(main())
