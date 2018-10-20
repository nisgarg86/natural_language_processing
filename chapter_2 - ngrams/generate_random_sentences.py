'''
this code generates random sentences based on ngram model
'''

__author__ = 'nishant'

from random import choice
from sentence_mle import mle

def generate_next_word(current_history, mle_dicttionary):
    pass

if __name__ == '__main__':
    text = "I am Sam. Sam am I. I like peas and ham."
    n_gram = 3
    mle_dictionary = mle(text, n_gram)

    start_sequence = 'I'
    