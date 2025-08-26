import argparse
import sys


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

    return parser


def main() -> int:
    print('CLI is live, You can start!')

    parser = build_parser()
    args = parser.parse_args()

    print("parsed:", args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
