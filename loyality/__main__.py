import sys


def main() -> int:
    print('CLI is live')
    print(sys.argv[1:])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
