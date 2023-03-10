#! python3
# mad_libs.py — An exercise in reading and writing to text files.

import re
import shelve


user_name = input("Please name your file: ")
file_name = user_name + ".txt"


def copy_template():
    with open("mad_temp.txt", "r") as rf:
        with open(file_name, "w") as wf:
            for line in rf:
                wf.write(line)


def save_input():
    shelf_file = shelve.open("user_data")
    user_list = [
        input("Please enter an adjective: "),
        input("Please enter a noun: "),
        input("Please enter a present-tense verb: "),
        input("Please enter a noun: "),
    ]
    shelf_file["user_list"] = user_list
    print(list(shelf_file.values()))
    shelf_file.close()


def open_file():
    with open(file_name, "r") as f:
        content = f.read()
        noun_regex = re.compile(r"NOUN")
        mo = noun_regex.search(content)
        print(mo.group())

    # print(f.name)
    # print(f.read())


copy_template()
save_input()
open_file()
