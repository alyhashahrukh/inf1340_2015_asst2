#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):

    if len(word) > 0 and word.isalpha():
        return True

    first_letter = word[0]

    if first_letter == "a" or "e" or "i" or "o" or "u":
        word_vowel = word.lower()
        word_vowel.append("yay")
        return (word_vowel)

    elif first_letter != "a" or "e" or "i" or "o" or "u":
        word_consonant = word.lower() + first_letter
        word_consonant = word_consonant[1:len(word_consonant)]
        word_consonant.append("ay")
        return (word_consonant)

    else:
        print ('empty')

    """

    :param word: a word starting with vowel or consonant
    :return: the resulting pig latin word
    :raises: none

    """
    result = ""

    return result