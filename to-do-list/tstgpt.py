import time

tasks = []
# functions part
def load_tasks():
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
load_tasks()

def save_tasks():
    with open('tasks.txt', 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')
        
def add_task():
    new_task = input('Enter a new task >')
    tasks.append(new_task)
    time.sleep(0.5)
    print('Saved!')

def show_tasks():
    print('\n--- MY TASKS ---')
    if len(tasks) == 0:
        print('Your list is empty.')
    else:
        for index, task in enumerate(tasks):
            print(f'{index + 1}. {task}')

def remove_task():
    show_tasks()

    if len(tasks) > 0:
        task_number = int(input('Enter the number of the task to remove>'))
        index_to_remove = task_number - 1
        tasks.pop(index_to_remove)
        time.sleep(0.5)
        print('Task has been removed')
    else:
        print('Your list is empty.')
# menu and logics
while True:
    print('\n--- MENU ---')
    print('1 - Add new task')
    print('2 - Show tasks')
    print('3 - Remove')
    print('4 - Exit')

    choice = input('Choose an operation >')

    if choice == '1':
        add_task()

    elif choice == '2':
        show_tasks()
    
    elif choice == '3':
        remove_task()

    elif choice == '4':
        save_tasks()
        time.sleep(0.5)
        print("Goodbye! See you next time")
        break
   
    else:
        print('Try again')