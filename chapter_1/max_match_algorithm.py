'''
this python code implements max match algorithm - it segments/tokenizes words from a sentence without any spaces/delimeters.
Uses a pre defined dictionary of words
uses a greedy approach - tries to match the longest possible word from string. if no word matches, creates single character as a word
works very well on chinese language, not so well on english
'''

__author__ = 'nishant'

from nltk.corpus import cmudict

WORD_LIST = cmudict.words()

def max_match(string):

    length = len(string)
    # base condition of recursion
    if length == 0:
        return []

    for i in range(length):
        first_word = string[:length-i]
        remaining_string = string[length-i:]

        if first_word in WORD_LIST:
            return [first_word] + max_match(remaining_string)

    # if no word matches, we consider the first character as a single word and apply max match recursively on remaining string
    first_word = string[0]
    remaining_string = string[1:]

    return [first_word]+max_match(remaining_string)

if __name__=="__main__":
    print max_match("wecanonlyseeashortdistanceahead")
