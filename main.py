import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    userAction = input("Type add, show, edit, complete or exit: ")
    userAction = userAction.strip()

    if userAction.startswith("add"):
        todo = userAction[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    elif userAction.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index +1}-{item}"
            print(row)

    elif userAction.startswith("edit"):
        try:
            number = int(userAction[5:])
            index = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not a number!")
            continue

    elif userAction.startswith("complete"):
        try:
            number = int(userAction[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif userAction.startswith("exit"):
        break

    else:
        print("Invalid Command.")
print("Successfully Exited!")
