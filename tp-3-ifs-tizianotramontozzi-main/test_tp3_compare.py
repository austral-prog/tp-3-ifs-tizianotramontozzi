import io
import unittest
import unittest.mock
import exercise_compare as ex4


class TP3CompareTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_first_greater(self, mock_stdout):
        inputs = iter(["10", "5"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex4.compare()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "10 es mayor que 5")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_first_smaller(self, mock_stdout):
        inputs = iter(["3", "8"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex4.compare()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "3 es menor que 8")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_equal(self, mock_stdout):
        inputs = iter(["7", "7"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex4.compare()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "7 es igual a 7")


if __name__ == '__main__':
    unittest.main()
