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
    while start < end:
        if input_string[start:start + len(substring)] == substring:
            return start
        else:
            start += 1
    return -1


def multi_find(input_string, substring, start, end):

    """
    :param: string, substring, start integer, end integer
    :return: variable result
    :raises: -1
    """
    result = ""

    while start < end:
        if input_string[start:start + len(substring)] == substring:
            result = result + str(start) + ","
            start += 1
        else:
            start += 1

        result = result[0:len(result) - 1]
        return -1
