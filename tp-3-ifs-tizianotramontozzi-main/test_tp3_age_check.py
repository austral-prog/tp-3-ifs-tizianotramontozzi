import io
import unittest
import unittest.mock
import exercise_age_check as ex3


class TP3AgeCheckTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_adult(self, mock_stdout):
        inputs = iter(["20", "18"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex3.age_check()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Eres mayor de edad")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_minor(self, mock_stdout):
        inputs = iter(["16", "18"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex3.age_check()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Eres menor de edad")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_exactly_limit(self, mock_stdout):
        inputs = iter(["18", "18"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex3.age_check()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Eres mayor de edad")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_negative_age(self, mock_stdout):
        inputs = iter(["-5", "18"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex3.age_check()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Entrada invalida")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_zero(self, mock_stdout):
        inputs = iter(["0", "18"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex3.age_check()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Entrada invalida")


if __name__ == '__main__':
    unittest.main()
