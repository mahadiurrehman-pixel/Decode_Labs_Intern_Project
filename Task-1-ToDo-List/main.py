import json
import os

DATA_FILE = 'tasks.json'
tasks = []

def load_tasks():
    global tasks
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, IOError):
            print('Warning: Could Not Load Tasks File. Starting Fresh.')
            tasks = []

def save_tasks():
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print('Error: Could Not Save Tasks To File!')

def main():
    load_tasks()
    while True:
        print('\n===== TO-DO LIST =====')
        print("1.Add_Task \n2.View_Task \n3.Delete_Task \n4.Search_Task \n5.Edit_Task \n6.Clear_Tasks \n0.Exit")
        try:
            choice = int(input('Enter Your Choice: '))
        except ValueError:
            print('Please Enter A Valid Number!')
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            search_task()
        elif choice == 5:
            edit_task()
        elif choice == 6:
            clear_tasks()
        elif choice == 0:
            print('Good Bye Take Care!')
            break
        else:
            print('Invalid Choice! Please Try Again.')

def add_task():
    while True:
        task = input('Enter The Task You Want To Add (or 0 to cancel): ')
        if task == '0':
            print('Cancelled.')
            return
        elif task.strip() == '':
            print('Enter A Valid Task!')
        else:
            tasks.append(task)
            save_tasks()
            print(f'Your Task "{task}" Is Added Successfully!')
            return

def view_task():
    if not tasks:
        print('No Tasks Found!')
        return
    print('\n===== YOUR TASKS =====')
    for number, task in enumerate(tasks, start=1):
        print(f'{number}. {task}')

def delete_task():
    if not tasks:
        print('No Tasks To Delete!')
        return
    view_task()
    try:
        no = int(input('Enter No of Task You Want To Delete (or 0 to cancel): '))
        if no == 0:
            print('Cancelled.')
            return
        elif no < 1 or no > len(tasks):
            print('Invalid Task Number!')
            return
        no = no - 1
        removed = tasks.pop(no)
        save_tasks()
        print(f'"{removed}" Is Removed From The Tasks!')
    except ValueError:
        print('Please Enter A Valid Number!')

def search_task():
    if not tasks:
        print('No Tasks To Search!')
        return
    keyword = input('Enter Keyword To Search: ')
    if keyword.strip() == '':
        print('Enter A Valid Keyword!')
        return
    results = [(number, task) for number, task in enumerate(tasks, start=1)
               if keyword.lower() in task.lower()]
    if not results:
        print(f'No Tasks Found With Keyword "{keyword}"!')
    else:
        print(f'\n===== SEARCH RESULTS FOR "{keyword}" =====')
        for number, task in results:
            print(f'{number}. {task}')

def edit_task():
    if not tasks:
        print('No Tasks To Edit!')
        return
    view_task()
    try:
        no = int(input('Enter No of Task You Want To Edit (or 0 to cancel): '))
        if no == 0:
            print('Cancelled.')
            return
        elif no < 1 or no > len(tasks):
            print('Invalid Task Number!')
            return
        old_task = tasks[no - 1]
        new_task = input(f'Enter New Task To Replace "{old_task}": ')
        if new_task.strip() == '':
            print('Enter A Valid Task!')
            return
        tasks[no - 1] = new_task
        save_tasks()
        print(f'"{old_task}" Is Updated To "{new_task}" Successfully!')
    except ValueError:
        print('Please Enter A Valid Number!')

def clear_tasks():
    if not tasks:
        print('No Tasks To Clear!')
        return
    confirm = input(f'Are You Sure You Want To Delete All {len(tasks)} Tasks? (yes/no): ')
    if confirm.lower() == 'yes':
        tasks.clear()
        save_tasks()
        print('All Tasks Are Cleared!')
    else:
        print('Cancelled.')

if __name__ == "__main__":
    main()
