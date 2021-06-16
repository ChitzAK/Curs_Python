import pandas as pd
import os.path as path


def list_task():
    if path.exists('to_does.csv'):
        to_does = pd.read_csv('to_does.csv', header=0)
    else:
        columns = ['Due_Date', 'Task', 'Name', 'Category']
        to_does = pd.DataFrame(columns=columns)
    action = ''

    while action != 'Q':
        action = str(input("Enter what you wish to do: "
                           "'L' to List task "
                           "'S' to Sort task "
                           "'Q' to Quit")).upper()

        if action == 'L':
            print(to_does)
        elif action == 'S':
            a = input(
                "Enter how you want the list sorted: 'D' by due date; 'T' by task, 'N' by name or 'C' by category").upper()
            if a == 'D':
                to_does = to_does.sort_values(by='Due_Date')
            elif a == 'T':
                to_does = to_does.sort_values(by='Task')
            elif a == 'N':
                to_does = to_does.sort_values(by='Name')
            elif a == 'C':
                to_does = to_does.sort_values(by='Category')
        elif action == 'Q':
            break

    # to_does.to_csv('to_does.csv', index=False)
    to_does = pd.read_csv('to_does.csv')
    print(to_does)

    return None

