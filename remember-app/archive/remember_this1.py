import os
import argparse

# Determine the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

def add_to_remember_file(header, description, command, verbose=False):
    header_file_path = os.path.join(script_dir, f"{header.lower()}.txt")
    index_file_path = os.path.join(script_dir, 'index_header.txt')

    # Check if the header already exists
    if os.path.exists(header_file_path):
        # If the header file exists, check for duplicate commands
        with open(header_file_path, 'r') as hf:
            existing_content = hf.read()
            if command in existing_content:
                print(f"Command already exists under header '{header}'.")
                return
        # Append the new description and command
        with open(header_file_path, 'a') as hf:
            hf.write(f"## {description}\n{command}\n")
        print(f"Description and Command appended to # {header}.")
    else:
        # If the header file does not exist, create it
        with open(header_file_path, 'w') as hf:
            hf.write(f"## {description}\n{command}\n")
        with open(index_file_path, 'a') as index_file:
            index_file.write(f"{header}\n")
        print(f"New Header created for {header}. Description and Command appended to # {header}.")

    if verbose:
        print("\nUpdated content under the header:")
        print(f"# {header}\n## {description}\n{command}\n")

def interactive_mode():
    header = input("Enter the header: ")
    description = input("Enter the description: ")
    command = input("Enter the command: ")
    add_to_remember_file(header, description, command, verbose=True)

def main():
    parser = argparse.ArgumentParser(description="Remember and retrieve commands and descriptions.")
    parser.add_argument('-H', '--header', help='Header for the new entry')
    parser.add_argument('-D', '--description', help='Description for the new entry')
    parser.add_argument('-C', '--command', help='Command for the new entry')
    parser.add_argument('-i', '--interactive', action='store_true', help='Interactive mode to add entries')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print detailed information')

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.header and args.description and args.command:
        add_to_remember_file(args.header, args.description, args.command, verbose=args.verbose)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

