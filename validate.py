import pandas as pd
import os
from ast import literal_eval


# Validate filename input function
def validate_file(f):
    dir = os.path.dirname(os.path.realpath(__file__))
    while True:
        try:
            T = pd.read_csv(dir + "\\data\\" + f, sep="\n", header=None, names=['items'])
        except FileNotFoundError:
            f = input("Please enter a valid filename: ")
            continue
        else:
            break
    return T


# Validate support and confidence input function
def validate_measure(m, T=None):
    while True:
        try:
            m = literal_eval(m)
        except (ValueError, SyntaxError):
            m = input("Please enter a valid number: ")
            continue

        if m <= 0:
            m = input("Please enter a positive number: ")
            continue

        if type(m) == int and T is not None:
            if m > len(T):
                m = input("Please enter a number less than or equal to " + str(len(T)) + ": ")
                continue
            else:
                m /= len(T)
                break
        elif type(m) == float:
            if m > 1.0:
                m = input("Please enter a number less than or equal to 1.0: ")
                continue
            else:
                break
    return m
