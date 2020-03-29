"""This module contains a the functions for filtering characters"""
import re


def punctuation(text: str) -> str:
    """
    Removes punctuations from text
    :param text: text to remove all the punctuations from text
    :return: punctuation filtered text
    """
    punctuation_regex = re.compile(r'[\.\?\!\,]\s*')
    return re.sub(punctuation_regex, ' ', text)


def multiple_spaces(text: str) -> str:
    """
    This function replaces all repeating spaces and strips the text
    :param text: text to filter and strip
    :return: filtered and stripped text
    """
    return re.sub(r'\s+', ' ', text).strip()

