#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


GRADUATES = [["Number", "Surname", "Age"],
            [7274, "Robinson", 37],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

#deep copy of GRADUATES[0]
t1 = [] + GRADUATES[0]
t1
#deep copy of MANAGERS[0]
t2 = [] + MANAGERS[0]
t2

"""
WHAT THEY ARE LOOKING FOR:
NUMBER OF COLUMNS
len(t1) == len(t2)

NAMES OF COLUMNS
str(t1) == str(t2)

ORDER OF COLUMNS
t1 == t2 ?????
"""

def union(t1, t2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param t1: a table (a List of Lists)
    :param t2: a table (a List of Lists)
    :return: the resulting table union
    :raises: MismatchedAttributesException: none?
        if tables t1 and t2 don't have the same attributes
    """

    table_union = []
    for unify in t1 and t2:
        unify = t1.union(t2)
        table_union.append(unify)
    return table_union


def intersection(t1, t2):
    """
    Perform the intersection set operation on tables, table1 and table2.

    :param t1: a table (a List of Lists)
    :param t2: a table (a List of Lists)
    :return: the resulting table intersection
    :raises: none?
    """

    table_intersection = []
    for intersect in t1 and t2:
        intersect = t1.intersection(t2)
        table_intersection.append(intersect)
    return table_intersection


def difference(t1, t2):
    """
    Perform the difference set operation on tables, table1 and table2.

    :param t1: a table (a List of Lists)
    :param t2: a table (a List of Lists)
    :return: the resulting table difference
    :raises: none?
    """

    table_difference = []
    for differ in t1 and t2:
        differ = t1.difference(t2)
        table_difference.append(differ)
    return table_difference




#NOT SURE WHAT TO DO WITH THIS def remove_duplicates(1) function #


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True
    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

