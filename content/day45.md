# 👉 Day 45 Challenge: Ta Daaaa! It's A To Do

<a href="https://youtu.be/553lAJbfZMM?si=bPXvOiAivSyBXa8w" target="_blank">Dāvida video</a>


Today is a todo list management system. Wait, we did this? Yes, but your last to do list didn't allow you to store dates or anything besides the actual list.

Your program will store a todo list, and allow you to give each task a priority.

So, what are you waiting for? Item 1, top priority. Head on over to the challenge page for details.

### Still here? Stop procrastinating!

# 👉 Day 45 Challenge

Made it? Good! Let's get cracking.

Your system should:
1. Have a menu that asks if you want to add, view, move or edit a 'to do'.
2. If you choose 'add' then the system should:
    - Prompt you to input what the to do is, when it is due by and the priority (high, medium or low).
    - Add the 'to do' to the list.
3. 'View' should give two options:
    - View all - shows all 'to dos' with a pretty print.
    - View priority - allows you to search for high, medium or low priority and only see matching tasks.
4. 'Edit' allows you to change any of the information within one of the 'to dos'.
5. 'Remove' lets you completely remove a 'to do' when it is 'to done'.

Example:

```python
🌟Life Organizer🌟

Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > Add

What is the task? > Pay teachers more.
When is it due by? > 11/01/2022
What is the priority? >  High

Thanks, this task has been added.

Do you want to see the menu again or quit? > quit.
```


### To run this code you can use terminal and run the file 👀


<details>
<summary>💡 Hint</summary>

- Use a separate subroutine for add, view, edit, and remove.
- Clear the console before viewing a new entry.
- Use a `while True` loop to call the subroutines and display the menu.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/y7Vhi19EBDc?si=PrOiY4lh-Ekihu63" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import os
import time

todoList = []

def printAllList():
    if not todoList:
        print("Your to-do list is empty.")
    else:
        for index, item in enumerate(todoList):
            print(f"{index}: {item['item']} (Priority: {item['priority']})")

def printTodoListByPriority(priority):
    filtered_list = [item for item in todoList if item['priority'] == priority]
    if not filtered_list:
        print(f"No items with {priority} priority.")
    else:
        for index, item in enumerate(filtered_list):
            print(f"{index}: {item['item']}")

def addItemToList():
    print("Let's add a new item to your list!")
    priority = int(input("What is the priority of this task?\n1: High\n2: Medium\n3: Low\nEnter the number: "))
    item = input("What should I add to your to-do list? ")
    todoList.append({"priority": priority, "item": item})
    print(f"{item} added to your list.")

def updateItemInTodoList():
    printAllList()
    item_index = int(input("Which item would you like to update? "))
    if item_index < 0 or item_index >= len(todoList):
        print("Invalid item index.")
        return
    print(f"Editing item: {todoList[item_index]['item']} (Priority: {todoList[item_index]['priority']})")
    new_priority = int(input("What is the new priority?\n1: High\n2: Medium\n3: Low\nEnter the number: "))
    new_item = input("What should I update this to? ")
    todoList[item_index] = {"priority": new_priority, "item": new_item}
    print(f"Updated item: {new_item} (Priority: {new_priority})")

def removeItemFromTodoList():
    printAllList()
    item_index = int(input("Which item would you like to remove? "))
    if item_index < 0 or item_index >= len(todoList):
        print("Invalid item index.")
        return
    item = todoList.pop(item_index)
    print(f"Removed item: {item['item']} (Priority: {item['priority']})")

while True:
    print("\nTo-do list manager.📝")
    if not todoList:
        print("Your to-do list is empty.")
        addItemToList()
        time.sleep(1)
        os.system("clear")
        continue
    print("Menu:")
    print("1: Add a to-do")
    print("2: Remove a to-do")
    print("3: View to-do list")
    print("4: Edit a to-do")
    print("5: Erase the list")
    print("6: Exit")
    option = input("Select an option (1/2/3/4/5/6): ")
    
    if option == "1":
        addItemToList()
    elif option == "2":
        removeItemFromTodoList()
    elif option == "3":
        print("View by priority:")
        print("1: High")
        print("2: Medium")
        print("3: Low")
        print("4: All")
        view_option = input("Select an option (1/2/3/4): ")
        if view_option == "1" or view_option == "2" or view_option == "3":
            printTodoListByPriority(int(view_option))
        elif view_option == "4":
            printAllList()
        else:
            print("Invalid option.")
    elif option == "4":
        updateItemInTodoList()
    elif option == "5":
        confirm_erase = input("Are you sure you want to erase your list? (yes/no): ")
        if confirm_erase.lower() == "yes":
            todoList.clear()
            print("Your list has been erased.")
        else:
            print("Erase canceled.")
    elif option == "6":
        break
    else:
        print("Invalid option. Please choose a valid option (1/2/3/4/5/6).")

    time.sleep(1)
    os.system("clear")
```

</details>
