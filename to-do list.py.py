lists = []

def show_lists():
    if not lists:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(lists):
            print(f"{index + 1}. {task['title']} - {task['comment']}")

def add():
    title = input("Enter the task title: ")
    comment = input("Enter a comment: ")
    lists.append({'title': title, 'comment': comment})
    print("Task added successfully!")

def update():
    show_lists()
    index_task =int(input("Enter the task number you want to update (or 0 to cancel): "))- 1
    if 0 <= index_task < len(lists):
        new_title = input("Enter the new title (or press Enter to keep the current title): ")
        new_description = input("Enter the new comment (or press Enter to keep the current comment): ")
        if new_title:
            lists[index_task]['title'] = new_title
        if new_description:
            lists[index_task]['comment'] = new_description
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def pop_task():
    show_lists()
    index_task = int(input("Enter the task number you want to remove (or 0 to cancel): "))- 1
    if 0 <= index_task < len(lists):
        removed_task = lists.pop(index_task)
        print(f"Task '{removed_task['title']}' removed successfully!")
    else:
        print("Invalid task number.")

while True:
    print("To-Do List Manager\n")
    print("SELECT THE OPERATION YOU WANNA PERFORM")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        show_lists()
    elif choice == '2':
        add()
    elif choice == '3':
        update()
    elif choice == '4':
        pop_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

