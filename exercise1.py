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
        word = word.lower()
        result = ""
        vowel = "a,e,i,o,u"
        if word[0] is vowel:
            return result + yay
        while word[0] is not vowel:
            word[0] += (word[1:] + word[0])
            if word[0] == vowel:
                print result + "ay"
        else:
            return ""

print pig_latinify("crapple")


"""
def pig_latinify(word):
    """

    :param word: a word starting with vowel or consonant
    :return: the resulting pig latin word
    :raises: none

    """

    if len(word) > 0 and word.isalpha():
        first_letter = word[0]
        word = word.lower()
        vowel = "a" or "e" or "i" or "o" or "u":
        result = []
        if first_letter :
            result.append(word + "yay")
            return result
        elif first_letter != "a" or "e" or "i" or "o" or "u":
            result.append(word[1:len(word)] + first_letter + "ay")
            return result


"""

""" consonant word + ay"  change to while loop to accomodate words liek "scratch"
    else:
        return """


