from task1.task1 import task1_run
from task2.task2 import task2_run
from task3.task3 import task3_run
from task4.task4 import task4_run
from task5.task5 import task5_run
from checking import check_input

if __name__ == "__main__":
    while True:
        print(
                "\n---Choose task---\n"
                "1: Task1\n"
                "2: Task2\n"
                "3: Task3\n"
                "4: Task4\n"
                "5: Task5\n"
                "0: Exit"
            )
        choice = check_input("Enter the number ", 0, 5, int)
        match choice:
            case 0:
                print('(◕‿◕)')
                break
            case 1:
                task1_run()
            case 2:
                task2_run()
            case 3:
                task3_run()
            case 4:
                task4_run()
            case 5:
                task5_run()
