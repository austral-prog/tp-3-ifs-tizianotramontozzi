import io
import unittest
import unittest.mock
import exercise_calculator as ex8


class TP3CalculatorTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_addition(self, mock_stdout):
        inputs = iter(["10", "5", "+"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex8.calculator()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Resultado: 15.0")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_subtraction(self, mock_stdout):
        inputs = iter(["10", "5", "-"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex8.calculator()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Resultado: 5.0")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_multiplication(self, mock_stdout):
        inputs = iter(["10", "5", "*"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex8.calculator()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Resultado: 50.0")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_division(self, mock_stdout):
        inputs = iter(["10", "2", "/"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex8.calculator()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Resultado: 5.0")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_division_by_zero(self, mock_stdout):
        inputs = iter(["10", "0", "/"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex8.calculator()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Error: division por cero")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_operation(self, mock_stdout):
        inputs = iter(["10", "5", "x"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex8.calculator()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Operacion invalida")


if __name__ == '__main__':
    unittest.main()
