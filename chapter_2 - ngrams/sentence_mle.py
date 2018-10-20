'''
this code takes in a corpus and creates an n-gram model.
it also generate n-gram probability for a sequence of words
'''

__author__ = 'nishant'

from clean_input import insert_start_and_end_sentence_symbol, word_tokenization, sentence_tokenization

def mle(text, ngram=2):
    '''
    :param sentence_list: list of list of normalized words
    :param ngram: integer - denotes the ngram model to be used - bigram, trigram, etc.
    :return: dictionary if maximum likelihood of each word given previous words
    '''

    sentence_list = sentence_tokenization(text)
    sentence_list = [word_tokenization(sentence) for sentence in sentence_list]

    for i in range(len(sentence_list)):
        sentence_list[i] = insert_start_and_end_sentence_symbol(sentence_list[i],ngram)
    mle_dictionary = {}

    for sentence in sentence_list:
        sent_length = len(sentence)
        if sent_length > 0:
            for i in range(0,sent_length-ngram+1):
                current_part = sentence[i:i+ngram]
                history = " ".join(current_part[:-1])  # converting list to string
                word = current_part[-1]

                if history not in mle_dictionary:
                    mle_dictionary[history] = {}
                mle_dictionary[history][word] = mle_dictionary[history].get(word,0) + 1

    return mle_dictionary

def predict_sentence_probability(sentence, mle_dictionary, n_gram):
    '''
    :param sentence: sentence string
    :param mle_dictionary: dictionary containing n gram probabilities
    :param n_gram: integer - denoting ngram probability
    :return: sentence probability
    '''

    word_list = word_tokenization(sentence)
    word_list = insert_start_and_end_sentence_symbol(word_list, n_gram)
    sentence_probability = 1

    sent_length = len(word_list)
    for i in range(0,sent_length-n_gram+1):
        current_part = word_list[i:i + n_gram]
        history = " ".join(current_part[:-1])  # converting list to string
        word = current_part[-1]

        current_sequence_probability = mle_dictionary[history][word]*1.0/sum(mle_dictionary[history].values())
        sentence_probability *= current_sequence_probability

    return sentence_probability

if __name__=="__main__":

    text = "I am Sam. Sam am I. I like peas and ham."
    n_gram = 3

    mle_dictionary = mle(text,n_gram)
    print predict_sentence_probability("I am Sam.",mle_dictionary,n_gram)