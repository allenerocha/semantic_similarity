import unittest
import case_change


class TestChangeCase(unittest.TestCase):
    def change_case_test(self):
        # check for int
        with self.assertRaises(TypeError):
            case_change.change_case(1)

        with self.assertRaises(TypeError):
            case_change.change_case(1.0)

        with self.assertRaises(TypeError):
            case_change.change_case(True)

        with self.assertRaises(TypeError):
            case_change.change_case("")

        with self.assertRaises(TypeError):
            case_change.change_case(object)

        with self.assertRaises(TypeError):
            case_change.change_case({"test": 123})

        with self.assertRaises(TypeError):
            case_change.change_case([1, 2, 3])

        with self.assertRaises(TypeError):
            case_change.change_case((1, 2, 3))

        with self.assertRaises(TypeError):
            case_change.change_case("test", 1)

        with self.assertRaises(TypeError):
            case_change.change_case("test", 1.0)

        with self.assertRaises(TypeError):
            case_change.change_case("test", "test")

        with self.assertRaises(TypeError):
            case_change.change_case("test", "")

        with self.assertRaises(TypeError):
            case_change.change_case("test", object)

        with self.assertRaises(TypeError):
            case_change.change_case("test", {"test": 123})

        with self.assertRaises(TypeError):
            case_change.change_case("test", [1, 2, 3])

        with self.assertRaises(TypeError):
            case_change.change_case("test", (1, 2, 3))

        self.assertEqual(case_change.change_case("Test"), "test")
        self.assertEqual(case_change.change_case("Test", False), "TEST")


