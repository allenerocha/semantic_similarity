#!/usr/bin/env python3
# encoding: utf-8

import os


if __name__ == "__main__":
    # check if the corpus directory exists
    if not os.path.isdir('corpus'):
        raise FileNotFoundError("The corpus directory must exist with text files in order to run this application!")

