import argparse
import sys

balances: dict[str, int] = {}


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
    new_balance = balances.get(customer_id, 0) + points
    balances[customer_id] = new_balance
    return balances[customer_id]


def main() -> int:
    print('CLI is live, You can start!')

    parser = build_parser()
    args = parser.parse_args()

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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
