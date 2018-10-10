'''
this python code calculates the maximum likelihood estimation of a word w given previous word history h based on n-gram model.
P(w/h)
'''

__author__ = 'nishant'

def sentence_tokenization(text):
    '''
    :param text: entire text in which sentences are separated by full stop '.'
    :return: list of sentences
    '''

    text_length = len(text)
    if text_length == 0:
        return []

    sentence_list = [i for i in text.split(".") if len(i) > 0]
    return sentence_list

def word_normalization(word):
    '''
    :param word: normalizes each word to lowercase. removes numbers and special characters
    :return: normalized word
    '''

    normalized_word = ""
    if len(word) == 0:
        return normalized_word

    for char in word:
        if char.isalpha():
            normalized_word+=char.lower()
    return normalized_word

def word_tokenization(sentence):
    '''
    :param sentence: sentence of words separated by space.
    :return: set of normalized words
    '''

    normalized_word_list = []
    if len(sentence) == 0:
        return normalized_word_list

    word_list = sentence.split(" ")
    for i in range(len(word_list)):
        normalized_word = word_normalization(word_list[i])
        if len(normalized_word) > 0:
            normalized_word_list.append(normalized_word)

    return normalized_word_list

def mle(sentence_list, ngram=2):
    '''
    :param sentence_list: list of list of normalized words
    :param ngram: integer - denotes the ngram model to be used - bigram, trigram, etc.
    :return: dictionary if maximum likelihood of each word given previous words
    '''

    for i in range(len(sentence_list)):
        sentence_list[i] = insert_start_and_end_sentence_symbol(sentence_list[i],ngram)
    mle_dictionary = {}

    for sentence in sentence_list:
        sent_length = len(sentence)
        if sent_length > 0:
            for i in range(0,sent_length-ngram+1):
                current_part = sentence[i:i+ngram]
                history = tuple(current_part[:-1])  # converting list to tuple
                word = current_part[-1]

                if history not in mle_dictionary:
                    mle_dictionary[history] = {}
                mle_dictionary[history][word] = mle_dictionary[history].get(word,0) + 1
                mle_dictionary[history]['total'] = mle_dictionary[history].get('total',0) + 1

    return mle_dictionary

def insert_start_and_end_sentence_symbol(word_list, ngram):

    if len(word_list) == 0:
        return []
    return ['<s>']*(ngram-1) + word_list + ['</s>']

def predict_sentence_probability(sentence, mle_dictionary, n_gram):

    word_list = word_tokenization(sentence)
    word_list = insert_start_and_end_sentence_symbol(word_list, n_gram)
    sentence_probability = 1

    sent_length = len(word_list)
    for i in range(0,sent_length-n_gram+1):
        current_part = word_list[i:i + n_gram]
        history = tuple(current_part[:-1])  # converting list to tuple
        word = current_part[-1]

        current_sequence_probability = mle_dictionary[history][word]*1.0/mle_dictionary[history]['total']
        sentence_probability *= current_sequence_probability

    return sentence_probability


if __name__ == "__main__":

    text = "I am Sam. Sam am I. I like peas and ham."
    sentence_list =  sentence_tokenization(text)
    for i in range(len(sentence_list)):
        sentence_list[i] = word_tokenization(sentence_list[i])

    mle_dictionary = mle(sentence_list,2)
    for i,j in mle_dictionary.items():
        print i,j
    print predict_sentence_probability("I am Sam.",mle_dictionary,2)

