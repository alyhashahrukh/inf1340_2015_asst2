#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



def pig_latinify(word):

    """
    :param word: a word starting with vowel or consonant
    :return: the resulting pig latin word
    :raises: none
    """

    if len(word) > 0 and word.isalpha():
        word = word.lower()
        result = ""
        vowel = "a,e,i,o,u"
        if word[0] is vowel:
            return result + yay
        elif word[0] is not vowel:
            for i in range(1, len(word)):
                if word[i] in vowel:
                    word = word[i:] + word[:i] + "ay"
                    result += word
                    return result
        else:
            return ""






