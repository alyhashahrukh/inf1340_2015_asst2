#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):

    if len(substring) > len(input_string):
        return -1

    if end > len(input_string):
        end = len(input_string)
    for i in range(start, end):
        index = i
    for j in range(len(substring)):
        if not substring[j] == input_string[i + j]:
            index = -1
            break
    if index >= 0:
        return index
        return -1


def multi_find(input_string, substring, start, end):
    result = ""


