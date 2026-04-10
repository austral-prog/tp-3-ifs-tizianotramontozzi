import io
import unittest
import unittest.mock
import exercise_even_odd as ex2


class TP3EvenOddTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_even_number(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="8"):
            ex2.even_odd()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El numero 8 es par")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_odd_number(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="7"):
            ex2.even_odd()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El numero 7 es impar")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_zero(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="0"):
            ex2.even_odd()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El numero 0 es par")


if __name__ == '__main__':
    unittest.main()
