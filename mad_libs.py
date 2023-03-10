#! python3
# mad_libs.py — An exercise in reading and writing to text files.

import os
import pathlib
import shelve


user_name = input("Please name your file: ")
file_name = user_name + ".txt"


def new_file():
    with open("mad_temp.txt", "r") as rf:
        with open(file_name, "w") as wf:
            for line in rf:
                wf.write(line)


def open_file():
    with open(file_name, "r") as f:
        print(f.name)
        print(f.read())


def mad_input():
    # input_1 = input("Please enter an adjective: ")
    # input_2 = input("Please enter a noun: ")
    # input_3 = input("Please enter an adverb: ")
    # input_4 = input("Please enter a verb: ")
    pass


new_file()
open_file()
