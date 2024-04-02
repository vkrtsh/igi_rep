# Laboratory work No.3.
# Topic: Standard data types, collections, functions, modules.
# Developer: Artish Victoria Olegovna.
# Date of development: 22.03.2024.

from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5
from checking import check_input


def task_selection_interface():
    print("Welcome to the task selection interface!")
    print("Please choose one of the following tasks by entering the corresponding number:")
    print("1. Task 1")
    print("2. Task 2")
    print("3. Task 3")
    print("4. Task 4")
    print("5. Task 5")

    while True:
        task_number = check_input("Enter the number of the task you want to execute (or enter 0 to exit): ", 0, 5, int)
        if task_number == 0:
            break
        elif task_number == 1:
            task1(2, 0.000001)
        elif task_number == 2:
            task2()
        elif task_number == 3:
            task3()
        elif task_number == 4:
            task4()
        elif task_number == 5:
            task5()


task_selection_interface()
