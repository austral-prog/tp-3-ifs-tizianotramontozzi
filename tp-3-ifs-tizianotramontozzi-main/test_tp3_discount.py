import io
import unittest
import unittest.mock
import exercise_discount as ex10


class TP3DiscountTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_discount_20_percent(self, mock_stdout):
        inputs = iter(["100", "12"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex10.discount()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Subtotal: 1200.0")
            self.assertEqual(results[1], "Descuento aplicado: 20%")
            self.assertEqual(results[2], "Monto de descuento: 240.0")
            self.assertEqual(results[3], "Total final: 960.0")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_no_discount(self, mock_stdout):
        inputs = iter(["50", "3"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex10.discount()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Subtotal: 150.0")
            self.assertEqual(results[1], "Descuento aplicado: 0%")
            self.assertEqual(results[2], "Monto de descuento: 0.0")
            self.assertEqual(results[3], "Total final: 150.0")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_discount_10_percent(self, mock_stdout):
        inputs = iter(["80", "7"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex10.discount()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Subtotal: 560.0")
            self.assertEqual(results[1], "Descuento aplicado: 10%")
            self.assertEqual(results[2], "Monto de descuento: 56.0")
            self.assertEqual(results[3], "Total final: 504.0")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_discount_boundary_10(self, mock_stdout):
        inputs = iter(["100", "10"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex10.discount()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Subtotal: 1000.0")
            self.assertEqual(results[1], "Descuento aplicado: 20%")
            self.assertEqual(results[2], "Monto de descuento: 200.0")
            self.assertEqual(results[3], "Total final: 800.0")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_discount_boundary_5(self, mock_stdout):
        inputs = iter(["100", "5"])
        with unittest.mock.patch('builtins.input', side_effect=lambda: next(inputs)):
            ex10.discount()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Subtotal: 500.0")
            self.assertEqual(results[1], "Descuento aplicado: 10%")
            self.assertEqual(results[2], "Monto de descuento: 50.0")
            self.assertEqual(results[3], "Total final: 450.0")


if __name__ == '__main__':
    unittest.main()
