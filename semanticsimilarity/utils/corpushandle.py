"""This module handles all relevant functions for reading the passed corpus"""
import os
import tqdm
import time


def corpus(path: str):
    """
    This function opens the passed corpus path
    :param path: Path of file(s):
        If the path given ends in a directory, it will iterate over all files in that directory
        Otherwise it will only work with that file
    """
    total_time = time.time()
    # checks if the path is a string
    if not isinstance(path, str):
        raise TypeError(f"Expecting path as a string, argument given was of type {type(path)}")

    # checks for empty string
    if len(path) < 1:
        raise ValueError(f"Error handling the argument passed, was given {path}")

    # check if path is not file or directory
    if not os.path.isdir(path) and not os.path.isfile(path):
        raise FileNotFoundError(f'Error looking for file or path. The given {path} was not found.')

    # path is a directory
    if os.path.isdir(path):

        # get the start of the time
        print(f"Looking for files in {path}")
        start_time = time.time()
        # get all paths of the files as a list
        paths = dir_iter(path)
        print(f"Found {len(paths)} in {time.time() - start_time} seconds.\n")

        dataset = list()

        # iterate the list of strings
        start_time = time.time()
        print(f"Parsing {len(paths)} files in {path}...")
        failed_files = 0
        completed_files = 0
        for p in tqdm.tqdm(paths):
            try:
                # append the text of the current file to the list
                dataset.append(parse(p))
                completed_files += 1
            except:
                failed_files += 1
        # return the list
        print(f"{completed_files} were successfully extracted and {failed_files} failed to be extracted in {time.time() - start_time}!\n")
        print(f"Operation completed in {time.time() - total_time} seconds!")
        return dataset

    #path is a file
    else:
        # return the text of the file
        print(f"Operation completed in {time.time() - total_time} seconds!")
        return [parse(path)]

def dir_iter(path: str) -> list:
    """
    This function iterates over all of the files in the directory and returns them as a list of file paths
    :param path: directory to iterate over
    :return: List of file paths in path given
    """
    paths = list()
    for filename in tqdm.tqdm(os.listdir(path)):
        paths.append(f"{path}/{filename}")

    return paths


def parse(path: str) -> str:
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

    with open(path, "r") as file_data:
        corpus = file_data.readlines()
    # merge all the strings to one string
    return ' '.join(corpus)


