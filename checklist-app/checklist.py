import json
import os

# Define the path to the checklist
CHECKLIST_FILE = os.path.join(os.path.dirname(__file__), "checklist.json")


def load_checklist():
    """Load the checklist from the JSON file."""
    if not os.path.exists(CHECKLIST_FILE):
        print(f"Checklist file not found at {CHECKLIST_FILE}")
        return {}
    with open(CHECKLIST_FILE, "r") as f:
        return json.load(f)


def save_checklist(checklist):
    """Save the checklist to the JSON file."""
    with open(CHECKLIST_FILE, "w") as f:
        json.dump(checklist, f, indent=4)


def display_checklist(checklist):
    """Display the checklist with current progress."""
    for category in checklist["tasks"]:
        print(f"\n## {category['category']}")
        for idx, item in enumerate(category["items"], 1):
            status = "[x]" if item["done"] else "[ ]"
            print(
                f"{idx}. {status} {item['description']} (Pages: {item.get('page', 'N/A')})"
            )


def mark_done(checklist, category_number, task_number):
    """Mark a task as done."""
    category_idx = category_number - 1
    task_idx = task_number - 1
    if category_idx < 0 or category_idx >= len(checklist["tasks"]):
        print("Invalid category number.")
        return
    if task_idx < 0 or task_idx >= len(checklist["tasks"][category_idx]["items"]):
        print("Invalid task number.")
        return
    checklist["tasks"][category_idx]["items"][task_idx]["done"] = True
    save_checklist(checklist)
    print(f"Task {task_number} in category {category_number} marked as done.")


def reset_checklist(checklist):
    """Reset all tasks to undone."""
    for category in checklist["tasks"]:
        for item in category["items"]:
            item["done"] = False
    save_checklist(checklist)
    print("Checklist has been reset.")


def main():
    checklist = load_checklist()

    if not checklist:
        return

    while True:
        print("\nCurrent Checklist:")
        display_checklist(checklist)
        print("\nOptions:")
        print("1. Mark task as done")
        print("2. Reset checklist")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category_number = int(input("Enter the category number: "))
            task_number = int(input("Enter the task number to mark as done: "))
            mark_done(checklist, category_number, task_number)
        elif choice == "2":
            reset_checklist(checklist)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
