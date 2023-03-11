#! python3
"""mad_libs.py — An exercise in reading and writing to text files."""

import re
import shelve


user_name = input("Please name your file: ")
file_name = user_name + ".txt"


def copy_template():
    """opens template file and writes it to user-defined text file"""
    with open("mad_temp.txt", "r", encoding="utf-8") as rf:
        with open(file_name, "w", encoding="utf-8") as wf:
            for line in rf:
                wf.write(line)


def mad_lib():
    """uses regexes to search for NOUN, ADJECTIVE, VERB and ADVERB in file
    and replaces them with user input"""
    with open(file_name, "r", encoding="utf-8") as rf:
        content = rf.read()
        with open(file_name, "w", encoding="utf-8") as wf:
            madlib_regex = re.compile(r"ADJECTIVE")
            mo_madlib = madlib_regex.sub(
                input("Please type an adjective: "), content, count=1
            )
            wf.write(mo_madlib)

    with open(file_name, "r", encoding="utf-8") as rf:
        content = rf.read()
        with open(file_name, "w", encoding="utf-8") as wf:
            madlib_regex = re.compile(r"NOUN")
            mo_madlib = madlib_regex.sub(
                input("Please type a noun: "), content, count=1
            )
            wf.write(mo_madlib)

    with open(file_name, "r", encoding="utf-8") as rf:
        content = rf.read()
        with open(file_name, "w", encoding="utf-8") as wf:
            madlib_regex = re.compile(r"VERB")
            mo_madlib = madlib_regex.sub(
                input("Please type a past-tense verb: "), content, count=1
            )
            wf.write(mo_madlib)

    with open(file_name, "r", encoding="utf-8") as rf:
        content = rf.read()
        with open(file_name, "w", encoding="utf-8") as wf:
            madlib_regex = re.compile(r"NOUN")
            mo_madlib = madlib_regex.sub(
                input("Please type a noun: "), content, count=1
            )
            wf.write(mo_madlib)

    with open(file_name, "r", encoding="utf-8") as rf:
        content = rf.read()
        print(content)


copy_template()
mad_lib()
