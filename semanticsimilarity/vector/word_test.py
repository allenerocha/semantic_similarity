import unittest
import word


class TestWord(unittest.TestCase):
    def test_creation(self):
        # test with str
        word_test = word.Word("man")
        self.assertEqual(list(word_test.descriptor.keys())[0], "man")

        # test with integer
        with self.assertRaises(TypeError):
            word.Word(1)

        # test with float
        with self.assertRaises(TypeError):
            word.Word(1.0)

        # test with object
        with self.assertRaises(TypeError):
            word.Word(object)

        # test with dict
        with self.assertRaises(TypeError):
            word.Word({"test": 123})

        # test with list
        with self.assertRaises(TypeError):
            word.Word([1])

        # test with tuple
        with self.assertRaises(TypeError):
            word.Word((1, 2))

        # test with empty string
        with self.assertRaises(ValueError):
            word.Word("")


    def test_adding_components(self):
        # add new component
        word_test = word.Word("man")
        self.assertEqual(len(word_test.descriptor_components), 0)

        # test with integer
        with self.assertRaises(TypeError):
            word_test.append(1)

        # test with float
        with self.assertRaises(TypeError):
            word_test.append(1.0)

        # test with object
        with self.assertRaises(TypeError):
            word_test.append(object)

        # test with dict
        with self.assertRaises(TypeError):
            word_test.append({"test": 123})

        # test with list
        with self.assertRaises(TypeError):
            word_test.append([1])

        # test with tuple
        with self.assertRaises(TypeError):
            word_test.append((1, 2))

        # test with empty string
        with self.assertRaises(ValueError):
            word_test.append("")

        # increment existing component
        word_test.append("i")
        self.assertEqual(len(word_test.descriptor_components), 1)

        word_test.append("i")
        self.assertEqual(len(word_test.descriptor_components), 1)

        # add new component
        word_test.append("am")
        self.assertEqual(len(word_test.descriptor_components), 2)

        # increment existing component
        word_test.append("am")
        self.assertEqual(len(word_test.descriptor_components), 2)



