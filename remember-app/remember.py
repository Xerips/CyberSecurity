import os
import argparse

# Define ANSI escape codes for color
HEADER_COLOR = "\033[1;34m"  # Bold Blue
DESCRIPTION_COLOR = "\033[1;36m"  # Cyan
RESET_COLOR = "\033[0m"  # Reset to default color

# Determine the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))


def list_headers():
    index_file_path = os.path.join(script_dir, "index_header.txt")
    if os.path.exists(index_file_path):
        with open(index_file_path, "r") as f:
            headers = f.readlines()
            print("Available headers:")
            for header in headers:
                print(f"{HEADER_COLOR}# {header.strip()}{RESET_COLOR}")
    else:
        print("No headers found.")


def print_all():
    index_file_path = os.path.join(script_dir, "index_header.txt")
    if os.path.exists(index_file_path):
        with open(index_file_path, "r") as f:
            headers = f.readlines()
        for header in headers:
            header = header.strip()
            header_file = os.path.join(script_dir, f"{header.lower()}.txt")
            if os.path.exists(header_file):
                print(f"\n{HEADER_COLOR}# {header}{RESET_COLOR}")
                with open(header_file, "r") as hf:
                    content = hf.read().splitlines()
                    for line in content:
                        if line.startswith("##"):
                            print(f"{DESCRIPTION_COLOR}{line}{RESET_COLOR}")
                        else:
                            print(line)
    else:
        print("No headers found.")


def search_keyword(keyword):
    keyword = keyword.lower()
    index_file_path = os.path.join(script_dir, "index_header.txt")
    if os.path.exists(index_file_path):
        with open(index_file_path, "r") as f:
            headers = f.readlines()
        found = False
        for header in headers:
            header = header.strip()
            header_file = os.path.join(script_dir, f"{header.lower()}.txt")
            if os.path.exists(header_file):
                with open(header_file, "r") as hf:
                    content = hf.read().splitlines()
                    if keyword in "\n".join(content).lower():
                        print(f"\n{HEADER_COLOR}# {header}{RESET_COLOR}")
                        for line in content:
                            if keyword in line.lower():
                                if line.startswith("##"):
                                    print(f"{DESCRIPTION_COLOR}{line}{RESET_COLOR}")
                                else:
                                    print(line)
                        found = True
        if not found:
            print(f"No matches found for keyword '{keyword}'.")
    else:
        print("No headers found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Retrieve remembered commands and descriptions."
    )
    parser.add_argument("header", nargs="?", help="Header to display")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Display all headers with their commands and descriptions",
    )
    parser.add_argument("--list", action="store_true", help="List all headers")
    parser.add_argument("--search", help="Search for a keyword in descriptions")

    args = parser.parse_args()

    if args.all:
        print_all()
    elif args.list:
        list_headers()
    elif args.search:
        search_keyword(args.search)
    elif args.header:
        header_file = os.path.join(script_dir, f"{args.header.lower()}.txt")
        if os.path.exists(header_file):
            print(f"{HEADER_COLOR}# {args.header}{RESET_COLOR}")
            with open(header_file, "r") as f:
                content = f.read().splitlines()
                for line in content:
                    if line.startswith("##"):
                        print(f"{DESCRIPTION_COLOR}{line}{RESET_COLOR}")
                    else:
                        print(line)
        else:
            print(f"Header '{args.header}' not found.")
    else:
        parser.print_help()
