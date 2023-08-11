#!/usr/bin/env python3
# mad_libs.py — An exercise in reading and writing files.
# For more information, see README.md

import logging
import os
import re
import shutil

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.

file_name = f'{input("Please name your file: ")}.txt'


def copy_template():
    """opens template file and writes it to user-defined text file"""
    tmp_file = f"{os.getcwd()}/mad_temp.txt"
    renamed_file = f"{os.getcwd()}/{file_name}"
    shutil.copy(tmp_file, renamed_file)


def mad_lib():
    """uses regexes to search for NOUN, ADJECTIVE, VERB and ADVERB in file
    and replaces them with user input"""
    with open(file_name, "r", encoding="utf-8") as rf:
        content = rf.read()
        madlib_regex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")
        search = madlib_regex.findall(content)
        length = len(search)

    for word in range(length):
        if search[word] == "NOUN":
            with open(file_name, "r", encoding="utf-8") as rf:
                content = rf.read()
                with open(file_name, "w", encoding="utf-8") as wf:
                    noun_madlib = madlib_regex.sub(
                        input("Please type a noun: "), content, count=1
                    )
                    wf.write(noun_madlib)

        elif search[word] == "ADJECTIVE":
            with open(file_name, "r", encoding="utf-8") as rf:
                content = rf.read()
                with open(file_name, "w", encoding="utf-8") as wf:
                    adj_madlib = madlib_regex.sub(
                        input("Please type an adjective: "), content, count=1
                    )
                    wf.write(adj_madlib)

        elif search[word] == "VERB":
            with open(file_name, "r", encoding="utf-8") as rf:
                content = rf.read()
                with open(file_name, "w", encoding="utf-8") as wf:
                    verb_madlib = madlib_regex.sub(
                        input("Please type a verb: "), content, count=1
                    )
                    wf.write(verb_madlib)

        elif search[word] == "ADVERB":
            with open(file_name, "r", encoding="utf-8") as rf:
                content = rf.read()
                with open(file_name, "w", encoding="utf-8") as wf:
                    adv_madlib = madlib_regex.sub(
                        input("Please type an adverb: "), content, count=1
                    )
                    wf.write(adv_madlib)

    with open(file_name, "r", encoding="utf-8") as rf:
        content = rf.read()
        print(content)


def main() -> None:
    copy_template()
    mad_lib()


if __name__ == "__main__":
    main()
