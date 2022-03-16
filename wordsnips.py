from flask import Flask, render_template, redirect, request


# word value calculator
def word_value_calc(raw_word):
    """calculate the word value of a word
    based on A=1 to Z=26 and the reverse"""
    # convert to uppercase
    upper_word = raw_word.upper()
    # remove non-alpha characters and calculate value sum
    final_word = ''
    value = 0
    reverse_value = 0
    for ch in upper_word:
        if "A" <= ch <= "Z":
            final_word += ch
            value += ord(ch) - 64
            reverse_value += 27 - (ord(ch)-64)
    return final_word, value, reverse_value


def reverse_word_value_calc(raw_word):
    """calculate the word value of a word
    based on A=26 to Z=1"""
    upper_word = raw_word.upper()
    final_word = ''
    value = 0
    for ch in upper_word:
        if "A" <= ch <= "Z":
            final_word += ch
            value += 27 - (ord(ch) - 64)
    return value


def scrabble_word_value_calc(raw_word):
    """calculate the word value of a word
    based on Scrabble letter values"""
    upper_word = raw_word.upper()
    final_word = ''
    value = 0
    pointdict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
                 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
                 'Y': 4, 'Z': 10}
    for ch in upper_word:
        if "A" <= ch <= "Z":
            final_word += ch
            value += pointdict[ch]
    return value


# helper functions for anagram checker ++
def cap_and_strip(text):
    """converts to all caps and removes all non-alphabetic characters"""
    text = text.upper()
    for ch in text:
        if not ch.isalpha():
            text = text.replace(ch, "")
    return text


def in_common(string1, string2):
    """prints letters that are the same between 2 strings"""
    commonletters = [ch for ch in string1 if ch in string2]
    print("Letters in common are", " ".join(commonletters))
    return True


def lettercountold(string):
    """returns a dictionary with letter counts of each character in a string
    naive method"""
    newdict = {}
    for char in string:
        if char in newdict:
            newdict[char] += 1
        else:
            newdict[char] = 1
    return newdict


def lettercount(string):
    """ creates a dictionary with key = char in string
    and value = count of char in string
    using count method"""
    return {char: string.count(char) for char in string}


def comparecounts(dict1, dict2):
    """takes 2 dictionaries with letter counts of characters
    returns 3 dictionaries of letter counts and characters:
    first = letters in common between the two dicts
    second = letters unique to the first dict
    third = letters unique to the second dict"""
    common = {
        key: dict1[key] if dict1[key] <= dict2[key] else dict2[key]
        for key in dict1
        if key in dict2
    }
    uniquea = comp_dict(dict1, common)
    uniqueb = comp_dict(dict2, common)
    uniquea = remove_zeroes(uniquea)
    uniqueb = remove_zeroes(uniqueb)
    return common, uniquea, uniqueb


def comp_dict(sample_dict, common_dict):
    """
    returns a new dictionary with unique characters in sample_dict
    compared to another dictionary
    """
    return {
        key: sample_dict[key] - common_dict[key]
        if key in common_dict
        else sample_dict[key]
        for key in sample_dict
    }


def remove_zeroes(dict1):
    """
    removes dictionary entries if value = 0
    """
    return {key: dict1[key] for key in dict1 if dict1[key] != 0}


def string_from_dict(dict1):
    """generates a string from a dictionary of character counts
    for A:3, the string will contain A A A"""
    newstr = ''
    for key in dict1:
        for _ in range(dict1[key]):
            newstr += key
    return sorted(newstr)


# main anagram checker
def anagram_checker(str1, str2):
    """compares the characters between 2 strings
    returns same or different plus character counts"""
    # convert to upper case, remove any non-alphabetic characters, and sort (function call)
    cleana = cap_and_strip(str1)
    cleanb = cap_and_strip(str2)
    a = sorted(cleana)
    b = sorted(cleanb)
    # get dictionaries of characters with counts
    dicta = lettercount(a)
    dictb = lettercount(b)
    sumdicta = sum(dicta.values())
    joinab = " ".join(a)
    joinabch = " ".join(dicta.keys())
    if a == b and sumdicta != 0:
        result1 = "{} and {} contain the SAME letters:".format(cleana, cleanb)
        result2 = "{} total characters ({})".format(sumdicta, joinab)
        result3 = "{} different letters ({})".format(len(dicta), joinabch)
        return result1, result2, result3
    common, uniquea, uniqueb = comparecounts(dicta, dictb)
    sumcom = sum(common.values())
    suma = sum(uniquea.values())
    sumb = sum(uniqueb.values())
    joincom = " ".join(string_from_dict(common))
    joina = " ".join(string_from_dict(uniquea))
    joinb = " ".join(string_from_dict(uniqueb))
    if suma == 0 or sumb == 0:
        result1 = "Please enter alphabetic characters in both strings"
        result2 = ''
        result3 = ''
        return result1, result2, result3
    result1 = "{} and {} contain DIFFERENT letters with {} character(s) in common: {} \n".format(cleana, cleanb, sumcom,
                                                                                                 joincom)
    result2 = "{} character(s) unique to first string: {} \n ".format(suma, joina)
    result3 = " {} character(s) unique to second string: {} \n".format(sumb, joinb)
    return result1, result2, result3


# caesar rotation
def caesar_all(text):
    """returns all 26 Caesar rotations of an input string
    returns a list of tuples with rotation # and the new string
    return of a dictionary was difficult to send along in html"""
    # str = cap_and_strip(text) # include before sending to this function
    english_words = load_words()
    english = []
    resultlist = []
    for key in range(1, 27):
        newstr = ''
        for char in text:
            newchar = ord(char) + key
            if newchar > 90:
                newchar = newchar - 26
            newstr += chr(newchar)
        if newstr.lower() in english_words:
            english.append(newstr)
        resultlist.append((key, newstr))
        length = len(english)
        if length > 0 and english[length - 1] == text:
            english = english[:-1]  # don't include the entered word itself in the matching list

    return resultlist, english


# from https://github.com/dwyl/english-words/blob/master/read_english_dictionary.py
def load_words():
    with open('/Users/tamarab/Documents/Programming/cs50/Project/practice/words_alpha.txt') as file:
        valid_words = set(file.read().split())
    return valid_words


def check_english(list):
    english_words = load_words()
    return [word for word in list if word in english_words]
