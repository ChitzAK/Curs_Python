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
        action = str(input("Enter what you wish to do:\n'L' to List task\n'S' to Sort task\n'D' to Delete task or set "
                           "as Done\n'Q' to Quit")).upper()

        if action == 'L':
            # show only the list that has the user's name?
            print(to_does)

        elif action == 'S':
            b = input(
                "Enter how you want the list sorted:\n'A' for Ascending\n'D' for Descending").upper()
            if b == 'A':
                a = input(
                    "Enter how you want the list sorted:\n'D' by Due date\n'T' by Task\n'N' by Name\n'C' by Category").upper()
                if a == 'D':
                    to_does = to_does.sort_values(by='Due_Date')
                elif a == 'T':
                    to_does = to_does.sort_values(by='Task')
                elif a == 'N':
                    to_does = to_does.sort_values(by='Name')
                elif a == 'C':
                    to_does = to_does.sort_values(by='Category')
            elif b == 'D':
                a = input(
                    "Enter how you want the list sorted:\n'D' by due date\n'T' by task\n'N' by name\n'C' by category").upper()
                if a == 'D':
                    to_does = to_does.sort_values(by='Due_Date', reverse=True)
                elif a == 'T':
                    to_does = to_does.sort_values(by='Task', reverse=True)
                elif a == 'N':
                    to_does = to_does.sort_values(by='Name', reverse=True)
                elif a == 'C':
                    to_does = to_does.sort_values(by='Category', reverse=True)
        elif action == 'D':
            del_nr = input('Enter the index number for the task you want to remove if it was done: ')
            del_nr = int(del_nr)
            to_does.drop([del_nr], inplace=True)

        elif action == 'Q':
            break

        to_does.to_csv('to_does.csv', index=False)
        to_does = pd.read_csv('to_does.csv')
        print(to_does)

    return None
