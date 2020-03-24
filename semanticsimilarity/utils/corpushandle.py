"""This module handles all relevant functions for reading the passed corpus"""
import os


def open_corpus(path: str):
    if not isinstance(path, str):
        raise TypeError(f"Expecting path as a string, argument given was of type {type(path)}")

    if len(path) < 1:
        raise ValueError(f"Error handling the argument passed, was given {path}")


