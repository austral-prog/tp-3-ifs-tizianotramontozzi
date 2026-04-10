import io
import unittest
import unittest.mock
import exercise_grades as ex5


class TP3GradesTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_excellent(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="9"):
            ex5.grades()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Excelente")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_excellent_10(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="10"):
            ex5.grades()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Excelente")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_good(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="8"):
            ex5.grades()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Bueno")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_regular(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="6"):
            ex5.grades()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Regular")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_insufficient(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="3"):
            ex5.grades()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Insuficiente")


if __name__ == '__main__':
    unittest.main()
