# admin
from os import path


def add_name(name):
    find = 0

    # search duplicates if file exist
    if path.exists("NameDB.txt"):
        f = open("NameDB.txt", "r")
        lines = f.readlines()
        for line in lines:
            if line.strip("\n") == name:
                find = 1
                break
        f.close()

    # if no duplicate add name
    if find == 0:
        f = open("NameDB.txt", "a")
        text = "%s\n" % name
        f.write(text)
        print(name, "added to NameDB")
        f.close()
    else:
        print("not added, duplicate name")


def remove_name(name):
    # if file exist search for name, if find remove
    if not path.exists("NameDB.txt"):
        print("Missing file")
    else:
        f = open("NameDB.txt", "r")
        lines = f.readlines()
        f.close()

        find = 0

        new_f = open("NameDB.txt", "w")
        for line in lines:
            if line.strip("\n") == name:
                find = 1
            if line.strip("\n") != name:
                new_f.write(line)
        new_f.close()

        if find == 0:
            print("name not found in DB")
        else:
            print(name, "removed from NameDB")


def list_name():
    print("NameDB:")
    if not path.exists("NameDB.txt"):
        print("Missing file")
    else:
        f = open("NameDB.txt", "r")
        for x in f:
            print(x)


