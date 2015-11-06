#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start=0, end=1):

    """
    :param:
    :return:
    :raises:
    """
    index = start
    while 0 <= index < len(input_string):
        if input_string[index] == substring:
            return index
        index += end
    return -1


def multi_find(input_string, substring, start, end):

    """
    :param:
    :return:
    :raises:
    """

    result = ""
    index = start

    while 0 <= index < len(input_string):
        if input_string[index] == substring:
            result = result + str(index) + ","
        index += 1
    else:
        index += 1

    result = result[0:len(result) - 1]
    return -1
