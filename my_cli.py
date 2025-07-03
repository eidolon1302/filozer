#!/usr/bin/env python
import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple example CLI.")
    parser.add_argument("name", help="The name to greet.")
    parser.add_argument("--times", type=int, default=1, help="Number of times to greet.")

    args = parser.parse_args()

    for _ in range(args.times):
        print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
