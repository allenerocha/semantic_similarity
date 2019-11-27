import re
import sys


class word:
    def __init__(self, word: str, sentence: str) -> None:
        """
        :param word: main word
        :param sentence: sentence the word appears in
        """
        self.word = word
        self.semantic_descriptor_vector = dict()
        self.sentence = sentence.replace(self.word, '')
        self.sentence = self.__filter(self.sentence)
        self.__add(self.sentence)
        for key, value in self.semantic_descriptor_vector.items():
            print("{}: {}".format(key, value))

    def __add(self, items: list) -> bool:
        """
        :param items: items from the filtered sentence to add to the semantic descriptor vector
        :return: successfully added to the dictionary
        """
        # iterate through the list of items to add them to the dictionary
        for item in items:
            # item already in the dictionary
            if item in self.semantic_descriptor_vector:
                self.semantic_descriptor_vector[item] += 1
            # item is not in the dictionary
            else:
                self.semantic_descriptor_vector[item] = 1
        # successfully added to the dictionary
        return True

    def __filter(self, sentence: str) -> list:
        """
        :param sentence: sentence to be filtered
        :return: list of the words split by the space character
        """
        regex = re.compile(r'@*#*\$*%*\^*&*\**\(*\)*/*-*\+*,*\\*[0-9]*')
        filtered = regex.sub('-', sentence)
        filtered = re.sub('\s+', ' ', filtered)
        filtered = re.sub('-{2,}', ' ', filtered)
        filtered = re.sub('-', '', filtered)
        filtered = filtered.split(' ')
        auxiliary_filtered = []
        for f in filtered:
            if f != '':
                auxiliary_filtered.append(f)
        return auxiliary_filtered


