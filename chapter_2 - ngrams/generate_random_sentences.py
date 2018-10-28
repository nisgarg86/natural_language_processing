'''
this code generates random sentences based on ngram model
'''

__author__ = 'nishant'

from numpy.random import choice
from sentence_mle import mle

def generate_next_word(current_history, mle_dictionary):
    '''
    :param current_history: string of words separated by space
    :param mle_dictionary: n-gram dictionary
    :return: next word as a list
    '''
    if current_history not in mle_dictionary.keys():
        print current_history, "key not found"
        return -1
    return list(choice(mle_dictionary[current_history].keys(),1))

def generate_string(start_sequence, sentence_count=5):
    '''
    :param start_sequence: starting words of the first sentence
    :param sentence_count: number of sentences to generate
    :return: text of random sentences
    '''
    start_sequence = start_sequence.lower().strip()
    start_sequence_list = start_sequence.split()

    random_sentence_list = generate_string_list(start_sequence_list,
                                                sentence_count)
    random_sentence = " ".join(random_sentence_list)
    random_sentence = random_sentence.replace("<s>","")
    random_sentence = random_sentence.replace("</s>", ".")

    return random_sentence


def generate_string_list(start_sequence_list,
                         sentence_count):
    '''
    :param start_sequence: list of starting words of the first sentence
    :param sentence_count: number of sentences to generate
    :return: list of tokens of random sentences
    '''

    # appendind <s> in front of sentence if length of start sequence is not enough
    if len(start_sequence_list) < n_gram - 1:
        start_sequence_list = ['<s>']*(n_gram-1-len(start_sequence_list)) + start_sequence_list

    random_sentence_list = start_sequence_list
    i,last_end_position = 0, 0
    current_history = random_sentence_list[1 - n_gram:]

    while i < sentence_count:
        next_word = generate_next_word(" ".join(current_history),
                                       mle_dictionary)
        if next_word == -1:
            return random_sentence_list
        random_sentence_list += next_word
        # starting sentence from scratch if </s> is met
        if random_sentence_list[-1] == '</s>':
            last_end_position = n_gram-2
            i += 1
        else:
            last_end_position -= 1

        current_history = random_sentence_list[1 - n_gram:]  # taking last ngram-1 words
        if last_end_position >= 0:
            current_history = current_history[last_end_position+1:]

        current_history = ['<s>']*(n_gram-1-len(current_history)) + current_history
    return random_sentence_list


if __name__ == '__main__':

    with open('shakespeare.txt','r') as f_:
        text = f_.read()

    # text = "I am Sam. Sam am I. I like peas and ham."
    n_gram = 5
    mle_dictionary = mle(text, n_gram)
    start_sequence = 'i'
    random_sentence = generate_string(start_sequence)
    print random_sentence




    