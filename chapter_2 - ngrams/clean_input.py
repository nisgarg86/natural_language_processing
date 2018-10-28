'''
this python code cleans and tokenizes input text.
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
    :return: list of normalized words
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

def insert_start_and_end_sentence_symbol(word_list, ngram):
    '''
    :param word_list: list of words
    :param ngram: list of words preceded  by <s> and followed by </s>
    :return:
    '''

    if len(word_list) == 0:
        return []
    return ['<s>']*(ngram-1) + word_list + ['</s>']

if __name__ == "__main__":

    text = "I am Sam. Sam am I. I like peas and ham."
    sentence_list =  sentence_tokenization(text)
    sentence_list = [word_tokenization(sentence) for sentence in sentence_list]