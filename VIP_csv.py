import pandas as pd
from datetime import datetime
import os.path as path


def add_task():
    if path.exists('to_does.csv'):
        to_does = pd.read_csv('to_does.csv', header=0)
    else:
        columns = ['Due_Date', 'Task', 'Name', 'Category']
        to_does = pd.DataFrame(columns=columns)
    action = ''

    while action != 'Q':
        action = str(input("Enter what you wish to do:\n'A' to add task\n'D' to delete task\n'L' to list task\n'S' to "
                           "Sort task\n'Q' to Quit")).upper()
        if action == 'A':
            # search duplicates if task exist/ if no duplicates it adds the task
            due_task = input('Enter the task you need to do: ')
            # adds deadline to existent task
            date = str(input('Enter the deadline (i.e. 2021,7,21): '))
            year, month, day = map(int, date.split(','))
            due = datetime(year, month, day)
            due = str(due)
            due = due[:10]
            who = input('Enter the person you need to do the task: ')
            cat = input('Enter the category for the task: ')
            to_does = to_does.append({'Due_Date': due, 'Task': due_task, 'Name': who, 'Category': cat},
                                     ignore_index=True)
        elif action == 'D':
            del_nr = input('Enter the index number for the task you want to remove: ')
            del_nr = int(del_nr)
            to_does.drop([del_nr], inplace=True)
        elif action == 'L':
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

    to_does.to_csv('to_does.csv', index=False)
    to_does = pd.read_csv('to_does.csv')
    print(to_does)

    return None


