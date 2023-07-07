#!/usr/bin/env python3


def return_evens(num_list):
    even_lc = [n for n in num_list if n % 2 == 0]
    print(even_lc)
    return even_lc


return_evens([0, 1, 3, 5, 7, 8, 9])


def make_exclamation(sentence_list):
    word_lc = [word + "!" for word in sentence_list]
    print(word_lc)
    return word_lc


make_exclamation(["Hello", "I'm doing great", "Python is fun"])
