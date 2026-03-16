import argparse
from netscope.scanner import discover_hosts, scan_target


def main():
    parser = argparse.ArgumentParser(
        description="NetScope - Lightweight Network Security Audit Tool"
    )

    parser.add_argument(
        "--target",
        required=True,
        help="Target IP, range, or network (example: 192.168.1.1 or 192.168.1.0/24)"
    )

    args = parser.parse_args()

    print("NetScope starting...")
    print(f"Target selected: {args.target}")

    discover_hosts(args.target)
    scan_target(args.target)


if __name__ == "__main__":
    main()
