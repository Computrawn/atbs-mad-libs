#! python3
# mad_libs.py — An exercise in reading and writing to text files.

import os
import pathlib
import shelve


def mad_lib():
    user_adjective = input("Please enter an adjective: ")
    user_noun = input("Please enter a noun: ")
    user_adverb = input("Please enter an adverb: ")
    user_verb = input("Please enter a verb: ")

    f = open("mad_temp.txt", "r")
    print(f.name)

    f.close()


mad_lib()
