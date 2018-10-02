'''
this python code applies max match algorithm to a string and \
then calculates word error rate with the original string
'''

__author__='nishant'

from max_match_algorithm import max_match
from edit_distance_and_alignment import edit_distance

def word_error_rate(source):
    '''
    :param source: original string in which words are separated by commas
    :return: wer = (S+D+I)/words in source
    '''
    original_words = source.split()
    if len(original_words) == 0:
        return "empty string"

    target = source.replace(" ","")
    target_words = max_match(target)

    total_operations, movement = edit_distance(original_words, target_words, words=True)

    wer = total_operations*1.0/len(original_words)
    return wer

if __name__=="__main__":

    print word_error_rate("thirty percent non granulating pale pink tissue wound bed")

