import json

tasks = []

# input output operation to actually parse
# use try to test a block of code for errors
# when using json need to do both loads and dumps
# json.load takes characters and turns it into a json object
# json.dump takes the object and turns it into characters that can be saved
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    pass

while True:
    # functionaity for tasks menu
    menu = input("Choose one of 'add', 'view', 'save', or 'quit': ").strip().lower() #remove whitespace and isolate terms

    # if input add is chosen
    if menu == "add":
        task = input("Add task and time: ")
        tasks.append(task)
    
    # iterate and add numbering functionality using f string to list tasks
    elif menu == "view":
        print("Your Current To do list:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

    # json.dump used to save characters
    elif menu == "save":
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        print("To do list is saved")
    
    elif menu == "quit":
        break


