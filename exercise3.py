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
table1 = GRADUATES

#Deep copy of table1 using .append to create table2
table2 = []
for table in GRADUATES:
    table2.append(table)

def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table union
    :raises: MismatchedAttributesException: none?
        if tables t1 and t2 don't have the same attributes
    """
    table_union = []
    for u in table1 and table2:
        u = table1.union(table2)
        table_union.append(u)
        return table_union


def intersection(table1, table2):
    """
    Perform the intersection set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table intersection
    :raises: none?
    """

    table_intersection = []
    for intersect in table1 and table2:
        intersect = table1.intersection(table2)
        table_intersection.append(intersect)
    return table_intersection


def difference(table1, table2):
    """
    Perform the difference set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table difference
    :raises: none?
    """

    table_difference = []
    for differ in table1 and table2:
        differ = table1.union(table2)
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

