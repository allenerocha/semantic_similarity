"""This module is the descriptor vector and contains all relevant functions"""
import math


class Word:
    def __init__(self, word: str) -> None:
        """
        This function assigns self.word to the passed word argument
        :param word: string to assign to self.word
        """
        if not isinstance(word, str):
            raise TypeError(f"Expected value to be str type, got {type(word)}.")

        if len(word) < 1:
            raise ValueError(f"Error creating an instance with the arguement: {word}.")

        self.word = word

        self.vector = dict()
        self.vector[self.word] = dict()


    def append(self, word: str):
        if not isinstance(word, str):
            raise TypeError(f"Expected value to be str type, got {type(word)}.")

        if len(word) < 1:
            raise ValueError(f"Error adding to vector with the arguement: {word}.")

        if word in self.descriptor_components:
            self.vector[self.word][word] += 1
        else:
            self.vector[self.word][word] = 1


    @property
    def descriptor(self):
        """This function returns the entire descriptor vector"""
        return self.vector


    @property
    def descriptor_components(self):
        """This function returns the components of this descriptor vector"""
        return self.vector[self.word]


    @property
    def magnitude(self):
        """Calculates the magnitude of this vector"""
        if len(self.descriptor_components) < 1:
            raise IndexError(f"{self.word} must have at least one component in order to calculate its magnitude.")

        squares = [value * value for value in self.descriptor_components.values()]
        return math.sqrt(sum(squares))


