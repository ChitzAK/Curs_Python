# vip_user
from os import path
import datetime
from datetime import datetime

# def list_task():
#     print("TasksDB:")
#     if not path.exists("TasksDB.txt"):
#         print("Missing file")
#     else:
#         f = open("TasksDB.txt", "r")
#         for x in f:
#             print(x)
#
#
# def assort_task():
#     alltasks = []
#
#     print("Sorting ascending TasksDB:")
#     if not path.exists("TasksDB.txt"):
#         print("Missing file")
#     else:
#         f = open("TasksDB.txt", "r")
#         lines = f.readlines()
#         f.close()
#
#         for line in lines:
#             alltasks.append(line)
#             alltasks.sort()
#     return alltasks
#
#
# def dessort_task():
#     alltasks = []
#
#     print("Sorting descending TasksDB:")
#     if not path.exists("TasksDB.txt"):
#         print("Missing file")
#     else:
#         f = open("TasksDB.txt", "r")
#         lines = f.readlines()
#         f.close()
#
#         for line in lines:
#             alltasks.append(line)
#             alltasks.sort(reverse=True)
#     return alltasks
from typing import Dict, Any



def add_task():
    to_does = {}
    action = str(input(
        "Enter what you wish to do: 'A' for add, 'D' for delete, 'L' for list, 'S' for sort or 'Q' for quit")).upper()
    while action != 'Q':
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
            to_do = {'date_due': due, 'task': due_task, 'name': who, 'category': cat}
            to_do.update(to_does)
            break
        elif action == 'D':
            del_nr = input('Enter the index number for the task you want to remove: ')
            del_nr = int(del_nr)
            to_does.drop([del_nr])
            break
        elif action == 'L':
            print(to_does)
            break
        elif action == 'S':
            sorted = input(
                "Enter how you want the list sorted: 'D' by due date; 'T' by task, 'N' by name or 'C' by category").upper()
            if sorted == 'D':
                to_does.sort_value(by='date_due')
            elif sorted == 'T':
                to_does.sort_value(by='task')
            elif sorted == 'N':
                to_does.sort_value(by='name')
            elif sorted == 'C':
                to_does.sort_value(by='category')
        elif action == 'Q':
            break

# def remove_deadline():
#     deadline = []

#    # removes deadline to existent task
#     print("Add deadline to existent task in TasksDB:")
#     if not path.exists("TasksDB.txt"):
#         print("Missing file")
#     else:
#         f = open("TasksDB.txt", "r")
#         lines = f.readlines()
#         f.close()
#
#         for line in lines:
#             deadline.append(line)
#             deadline.sort(reverse=True)
#     print(deadline)
