import argparse
from os import name
import subprocess


examples = ["free_fall"]


def main():
    parser = argparse.ArgumentParser(
        description="A simple simulator and solver for ODEs",
        epilog="Example: python simulator.py -e free_fall",
    )

    parser.add_argument(
        "-e",
        "--example",
        type=str,
        choices=examples,
        help="run an example simulation, use the flag -l to list all examples.",
    )

    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="List all examples.",
    )

    args = parser.parse_args()

    if args.example:
        subprocess.run(["python", "-m", f"examples.{args.example}.main"])

    if args.list:
        [print(example) for example in examples]


if __name__ == "__main__":
    main()
