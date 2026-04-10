import io
import unittest
import unittest.mock
import exercise_leap_year as ex6


class TP3LeapYearTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_leap_year_2000(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="2000"):
            ex6.leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 2000 es bisiesto")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_not_leap_year_2001(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="2001"):
            ex6.leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 2001 no es bisiesto")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_not_leap_year_1700(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="1700"):
            ex6.leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 1700 no es bisiesto")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_leap_year_2024(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="2024"):
            ex6.leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 2024 es bisiesto")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_not_leap_year_100(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="100"):
            ex6.leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 100 no es bisiesto")


if __name__ == '__main__':
    unittest.main()
