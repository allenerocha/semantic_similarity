#!/usr/bin/env python3
# encoding: utf-8

import os
import sys


if __name__ == "__main__":
    # variable to keep track of the absolute path of this file
    current_path = os.path.dirname(os.path.abspath(__file__))
    # check if the corpus directory exists
    if not os.path.isdir('corpus'):
        raise FileNotFoundError("The corpus directory must exist with text files in order to run this application!")

