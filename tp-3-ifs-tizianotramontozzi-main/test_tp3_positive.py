import io
import unittest
import unittest.mock
import exercise_positive as ex1


class TP3PositiveTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_positive_number(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="5"):
            ex1.positive()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El numero es positivo")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_number(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="-3"):
            ex1.positive()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El numero es negativo")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_zero(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="0"):
            ex1.positive()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El numero es cero")


if __name__ == '__main__':
    unittest.main()
