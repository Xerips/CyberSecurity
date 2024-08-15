import os
import argparse

def list_headers():
    if os.path.exists('index_header.txt'):
        with open('index_header.txt', 'r') as f:
            headers = f.readlines()
            print("Available headers:")
            for header in headers:
                print(f"# {header.strip()}")
    else:
        print("No headers found.")

def print_all():
    if os.path.exists('index_header.txt'):
        with open('index_header.txt', 'r') as f:
            headers = f.readlines()
        for idx, header in enumerate(headers):
            header = header.strip()
            header_file = f"{header.lower()}.txt"
            if os.path.exists(header_file):
                if idx > 0:
                    print("\n")  # Add a new line before each header section
                print(f"# {header}")
                with open(header_file, 'r') as hf:
                    print(hf.read().strip())
    else:
        print("No headers found.")

def search_keyword(keyword):
    keyword = keyword.lower()
    if os.path.exists('index_header.txt'):
        with open('index_header.txt', 'r') as f:
            headers = f.readlines()
        found = False
        for idx, header in enumerate(headers):
            header = header.strip()
            header_file = f"{header.lower()}.txt"
            if os.path.exists(header_file):
                with open(header_file, 'r') as hf:
                    content = hf.read()
                    if keyword in content.lower():
                        if idx > 0 and found:
                            print("\n")  # Add a new line before each header section when searching
                        print(f"# {header}")
                        lines = content.splitlines()
                        for i in range(len(lines)):
                            if keyword in lines[i].lower():
                                print(lines[i])
                                # Print the command if it's on the next line
                                if i + 1 < len(lines) and not lines[i + 1].startswith("##"):
                                    print(lines[i + 1])
                        found = True
        if not found:
            print(f"No matches found for keyword '{keyword}'.")
    else:
        print("No headers found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve remembered commands and descriptions.")
    parser.add_argument('header', nargs='?', help='Header to display')
    parser.add_argument('--all', action='store_true', help='Display all headers with their commands and descriptions')
    parser.add_argument('--list', action='store_true', help='List all headers')
    parser.add_argument('--search', help='Search for a keyword in descriptions')

    args = parser.parse_args()

    if args.all:
        print_all()
    elif args.list:
        list_headers()
    elif args.search:
        search_keyword(args.search)
    elif args.header:
        header_file = f"{args.header.lower()}.txt"
        if os.path.exists(header_file):
            print(f"# {args.header}")
            with open(header_file, 'r') as f:
                print(f.read().strip())
        else:
            print(f"Header '{args.header}' not found.")
    else:
        parser.print_help()

