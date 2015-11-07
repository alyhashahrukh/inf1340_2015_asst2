#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):

    """
    :param: string, substring, start integer, end integer
    :return: start index of string as integer
    :raises: -1
    """
    x = (len(substring))

    for i in range(start, len(input_string)):
        if input_string[i:(i+x)] == substring:
            return i
        else:
            i += 1

    return -1


def multi_find(input_string, substring, start, end):

    """
    :param: string, substring, start integer, end integer
    :return: variable result
    :raises: -1
    """

    loop = True
    results = ""
    r = start - 1

    while loop:
        r = find(input_string, substring, r + 1)
        if r != -1:
            if results == "":
                results += str(r)
            else:
                results += "," + str(r)
        else:
            loop = False
    return results
