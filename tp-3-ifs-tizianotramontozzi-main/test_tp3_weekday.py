import io
import unittest
import unittest.mock
import exercise_weekday as ex7


class TP3WeekdayTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_monday(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="lunes"):
            ex7.weekday()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Dia habil")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_friday(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="viernes"):
            ex7.weekday()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Dia habil")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_saturday(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="sabado"):
            ex7.weekday()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Fin de semana")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_sunday(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="domingo"):
            ex7.weekday()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Fin de semana")


if __name__ == '__main__':
    unittest.main()
