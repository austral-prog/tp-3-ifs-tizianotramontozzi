import io
import unittest
import unittest.mock
import exercise_password as ex11


class TP3PasswordTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_password(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="abc12345"):
            ex11.password()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Contraseña valida")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_password_too_short(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="abc123"):
            ex11.password()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Contraseña muy corta")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_password_no_number(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="abcdefgh"):
            ex11.password()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Debe contener un numero")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_password_multiple_errors(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="abc"):
            ex11.password()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Contraseña muy corta")
            self.assertEqual(results[1], "Debe contener un numero")


if __name__ == '__main__':
    unittest.main()
