import unittest
import word
import math


class TestWord(unittest.TestCase):
    def test___init__(self):
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


    def test_append(self):
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


    def test_descriptor(self):
        word_test = word.Word("man")
        word_test.append("i")
        word_test.append("i")
        word_test.append("i")

        word_test.append("am")
        word_test.append("am")
        word_test.append("am")

        word_test.append("a")
        word_test.append("a")

        word_test.append("sick")

        word_test.append("spiteful")

        word_test.append("an")

        word_test.append("unattractive")


        # hard coded version of the dictionary created above
        hard_coded = {
                        "man": {
                                "i": 3,
                                "am": 3,
                                "a": 2,
                                "sick": 1,
                                "spiteful": 1,
                                "an": 1,
                                "unattractive": 1,
                        }
                    }

        # these have the same value
        self.assertEqual(word_test.descriptor, hard_coded)

        # these no longer have the same value
        word_test.append("unattractive")
        self.assertNotEqual(word_test.descriptor, hard_coded)

        # now they both have the same value again
        hard_coded["man"]["unattractive"] += 1
        self.assertEqual(word_test.descriptor, hard_coded)

        # these no longer have the same value
        hard_coded["man"]["unattractive"] += 1
        self.assertNotEqual(word_test.descriptor, hard_coded)



    def test_magnitude(self):
        word_test = word.Word("man")

        # test with no components
        with self.assertRaises(IndexError):
            word_test.magnitude

        # test with 1 component with a value of 3
        word_test.append("i")
        word_test.append("i")
        word_test.append("i")

        self.assertAlmostEqual(word_test.magnitude, 3.0)

        # test with 2 components both with values of 3
        word_test.append("am")
        word_test.append("am")
        word_test.append("am")

        self.assertAlmostEqual(word_test.magnitude, math.sqrt(18.0))

        # test with 3 components with a total value of 22
        word_test.append("a")
        word_test.append("a")

        self.assertAlmostEqual(word_test.magnitude, math.sqrt(22.0))


