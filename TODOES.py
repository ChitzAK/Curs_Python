from ADMIN import *
from VIP_csv import *
from USER import *

if __name__ == '__main__':

    sign = 0
    user = 0

    # loop program, can exit with "end"
    while True:

        if sign == 0:
            print("Sign in as:")
            who = ""

            # not able to sign in as long as name is admin vip_user or name from DB
            # admin: able to create names and categories
            # vip user: able to create remove tasks or to add deadlines
            # users (names from NameDB added by admin): complete task
            # view_task, sort_task, filter_task, info - overall access

            while True:
                who = input()
                find = 0
                if path.exists("NameDB.txt"):
                    f = open("NameDB.txt", "r")
                    lines = f.readlines()
                    for line in lines:
                        if line.strip("\n") == who:
                            find = 1
                    f.close()

                if who == "admin" or who == "vip_user" or find == 1:
                    sign = 1
                    break
                elif who == "end":
                    sign = 0
                    break
                else:
                    print("Login types: [admin, vip_user, name_user]")

            if who == "end":
                break

            # giving privileges
            if who == "admin":
                user = 1
            if who == "vip_user":
                user = 2
            if find == 1:
                user = 3

            # displaying rights
            if user == 1:
                print("Admin Full Rights:")
                print(" add_name  \t\t-->Adds name to NameDB\n remove_name  \t-->Removes name from NameDB\n list_name  "
                      "\t-->Lists names from NameDB")
                print(" list_task  \t-->including:  Delete Task - 'D'\n\t\t\t\t\t\t\t   Sort Column by Task, Date, "
                      "Name and Category - 'S'")

            if user == 2:
                print("Vip_user Partial Rights:")
                print(" list_name")
                print(" add_task -->including: Add Task, Date, Name and Category - 'A'\n\t\t\t\t\t\tDelete Task - "
                      "'D'\n\t\t\t\t\t\tSort Column by Task, Date, Name and Category - 'S'")

            if user == 3:
                print(who, "Limited Rights:")
                print(" list_task  -->including:   Done Task - 'D'\n\t\t\t\t\t\t\tSort Column by Task, Date, "
                      "Name and Category - 'S'")

            print("Additional 'exit' to sign out")
            print("Additional 'end' to end session")

        # sign = 0 not sign in, 1 sign in
        if sign == 1:
            command = input()

            'full access'
            if command == "exit":
                sign = 0

            if command == "end":
                sign = 0
                break

            # astea 2 mai tarziu
            if command == "info":
                print("info mai tarziu")

            if command == "altceva":
                print("unknown command")

            # User 1
            if command == "add_name":
                if user == 1:
                    name = input()
                    if name == "admin" or name == "vip_user":
                        print("admin/vip_user key words")
                    else:
                        add_name(name)
                else:
                    print("No admin rights")

            if command == "remove_name":
                if user == 1:
                    name = input()
                    remove_name(name)
                else:
                    print("No admin rights")

            if command == "list_name":
                if user == 1 or user == 2:
                    list_name()
                else:
                    print("No rights")

            # User 2
            if command == "add_task":
                if user == 2:
                    add_task()
                else:
                    print("No admin rights")

            # User 3
            if command == "list_task":
                if user == 3 or user == 1:
                    list_task()
                else:
                    print("No admin rights")

