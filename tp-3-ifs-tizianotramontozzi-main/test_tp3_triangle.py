import io
import unittest
import unittest.mock
import exercise_triangle as ex9


class TP3TriangleTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_triangle(self, mock_stdout):
        inputs = iter(["3", "4", "5"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex9.triangle()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Los lados forman un triangulo valido")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_triangle(self, mock_stdout):
        inputs = iter(["1", "2", "5"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex9.triangle()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Los lados no forman un triangulo valido")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_equilateral_triangle(self, mock_stdout):
        inputs = iter(["5", "5", "5"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex9.triangle()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Los lados forman un triangulo valido")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_triangle_zero(self, mock_stdout):
        inputs = iter(["1", "2", "3"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex9.triangle()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Los lados no forman un triangulo valido")


if __name__ == '__main__':
    unittest.main()
