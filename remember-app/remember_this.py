import os
import argparse

def add_to_remember_file(header, description, command, verbose=False):
    header_file = f"{header.lower()}.txt"
    header_exists = os.path.isfile(header_file)
    
    # Check for duplicate commands
    if header_exists:
        with open(header_file, 'r') as f:
            content = f.read()
        if command in content:
            print(f"Command '{command}' already exists under #{header}.")
            return
    
    # Append to header file
    with open(header_file, 'a') as f:
        f.write(f"## {description}\n{command}\n\n")
    
    if not header_exists:
        with open('index_header.txt', 'a') as index_file:
            index_file.write(f"{header}\n")
        print(f"New Header created for #{header}. Description and Command appended to #{header}.")
    else:
        print(f"Description and Command appended to #{header}.")
    
    # Verbose mode: Display the updated content of the header file
    if verbose:
        with open(header_file, 'r') as f:
            print("\nUpdated content under the header:")
            print(f"#{header}\n{f.read()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remember commands and descriptions.")
    parser.add_argument('-H', '--header', help='Header for the new entry')
    parser.add_argument('-D', '--description', help='Description for the new entry')
    parser.add_argument('-C', '--command', help='Command for the new entry')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    parser.add_argument('-i', '--interactive', action='store_true', help='Enable interactive mode')

    args = parser.parse_args()

    if args.interactive:
        header = input("Enter the header: ")
        description = input("Enter the description: ")
        command = input("Enter the command: ")
    else:
        header = args.header
        description = args.description
        command = args.command

    if not all([header, description, command]):
        print("Error: Header, Description, and Command must all be provided.")
    else:
        add_to_remember_file(header, description, command, verbose=args.verbose)

