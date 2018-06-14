import itertools
import re

def _get_word_score(word):
    scores = {'a':1, 'b':4, 'c':4, 'd':2, 'e':1, 'f':4, 'g':3, 'h':3, 'i':1, 'j':10, 'k':5, 'l':2, 'm':4, 'n':2, 'o':2, 'p':4, 'q':10, 'r':1, 's':4, 't':1, 'u':2, 'v':5, 'w':4, 'x':8, 'y':3, 'z':10}

    sum = 0
    for letter in word:
        sum += scores[letter]
    return sum

def _get_combinations(letters_string):
    result = []
    for i in range(2, len(letters_string) + 1):
        for combination in itertools.combinations(letters_string, i):
            result.append(''.join(combination))
    return result

def _get_words(self, letters_string):
    result = set()
    letters_string = '\\b' + letters_string + '\\b'
    words = self._anagram_finder._words
    for word in words:
        match = re.match(letters_string, word, re.IGNORECASE)
        if match:                      
            result.add(word + ': ' + str(_get_word_score(word)))
    #print('result',result)
    return result

class WordFinder(object):
    def __init__(self, anagram_finder):
        self._anagram_finder = anagram_finder

    def get_words(self, letters_string):
        words = set()
        for word in _get_words(self, letters_string):
            words.update([word])
        return sorted(words, key=lambda word: (-len(word), word))
