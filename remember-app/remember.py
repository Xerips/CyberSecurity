import os
import argparse

# Determine the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

def list_headers():
    index_file_path = os.path.join(script_dir, 'index_header.txt')
    if os.path.exists(index_file_path):
        with open(index_file_path, 'r') as f:
            headers = f.readlines()
            print("Available headers:")
            for header in headers:
                print(f"# {header.strip()}")
    else:
        print("No headers found.")

def print_all():
    index_file_path = os.path.join(script_dir, 'index_header.txt')
    if os.path.exists(index_file_path):
        with open(index_file_path, 'r') as f:
            headers = f.readlines()
        for header in headers:
            header = header.strip()
            header_file = os.path.join(script_dir, f"{header.lower()}.txt")
            if os.path.exists(header_file):
                print(f"\n# {header}")
                with open(header_file, 'r') as hf:
                    print(hf.read().strip())
    else:
        print("No headers found.")

def search_keyword(keyword):
    keyword = keyword.lower()
    index_file_path = os.path.join(script_dir, 'index_header.txt')
    if os.path.exists(index_file_path):
        with open(index_file_path, 'r') as f:
            headers = f.readlines()
        found = False
        for header in headers:
            header = header.strip()
            header_file = os.path.join(script_dir, f"{header.lower()}.txt")
            if os.path.exists(header_file):
                with open(header_file, 'r') as hf:
                    content = hf.read()
                    if keyword in content.lower():
                        print(f"\n# {header}")
                        lines = content.splitlines()
                        for line in lines:
                            if keyword in line.lower():
                                print(line)
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
        header_file = os.path.join(script_dir, f"{args.header.lower()}.txt")
        if os.path.exists(header_file):
            with open(header_file, 'r') as f:
                print(f"# {args.header}")
                print(f.read().strip())
        else:
            print(f"Header '{args.header}' not found.")
    else:
        parser.print_help()

