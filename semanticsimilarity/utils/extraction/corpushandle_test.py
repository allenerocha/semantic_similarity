import unittest
import corpushandle


class TestCorpusHandle(unittest.TestCase):
    def corpus_test(self):
        # check for int
        with self.assertRaises(TypeError):
            corpushandle.corpus(1)

        # check for float
        with self.assertRaises(TypeError):
            corpushandle.corpus(1.0)

        # check for object
        with self.assertRaises(TypeError):
            corpushandle.corpus(object)

        # check for dict
        with self.assertRaises(TypeError):
            corpushandle.corpus({"test": 123})

        # check for list
        with self.assertRaises(TypeError):
            corpushandle.corpus([1, 2, 3])

        # check for tuple
        with self.assertRaises(TypeError):
            corpushandle.corpus((1, 2, 3))

        # check for empty string
        with self.assertRaises(TypeError):
            corpushandle.corpus("")

        # check if file exists
        with self.assertRaises(FileNotFoundError):
            corpushandle.corpus("notafile.py")

        # check if file exists
        with self.assertRaises(FileNotFoundError):
            corpushandle.corpus("notadir/")

