"""This module handles all relevant functions for reading the passed corpus"""
import os


def open_corpus(path: str):
    """
    This function opens the passed corpus path
    :param path: Path of file(s):
        If the path given ends in a directory, it will iterate over all files in that directory
        Otherwise it will only work with that file
    """
    # checks if the path is a string
    if not isinstance(path, str):
        raise TypeError(f"Expecting path as a string, argument given was of type {type(path)}")

    # checks for empty string
    if len(path) < 1:
        raise ValueError(f"Error handling the argument passed, was given {path}")

    # check if path is not file or directory
    if not os.path.isdir(path) or not os.path.isfile(path):
        raise FileNotFoundError(f'Error looking for file or path. The given {path} was not found.')

    # path is a directory
    if os.path.isdir(path):
        pass

    #path is a file
    else:
        pass

def dir_iter(path: str) -> list:
    """
    This function iterates over all of the files in the directory and returns them as a list of file paths
    :param path: directory to iterate over
    :return: List of file paths in path given
    """
    paths = list()
    for filename in os.listdir(path):
        paths.append(f"{path}/{filename}")

    return paths


def corpus_parse(path: str) -> str:
    """
    Opens the given path and returs its contents as a string
    :param path: File path
    :retrun: File contents as string
    """
    # checks if the path is a string
    if not isinstance(path, str):
        raise TypeError(f"Expecting path as a string, argument given was of type {type(path)}")

    # checks for empty string
    if len(path) < 1:
        raise ValueError(f"Error handling the argument passed, was given {path}")


