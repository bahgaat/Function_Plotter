import unittest
from Gui import *
import numpy as np
from matplotlib import pyplot as plt

# This class is responsible to test that the inputs from the user are handeled correctly.
class TestInputs(unittest.TestCase):
    def test_empty_min_x(self):
        gui = Gui()
        is_valid = gui.validate_inputs("","3","2 * x")
        self.assertFalse(is_valid)

    def test_empty_max_x(self):
        gui = Gui()
        is_valid = gui.validate_inputs("6","","2 * x")
        self.assertFalse(is_valid)

    def test_empty_function(self):
        gui = Gui()
        is_valid = gui.validate_inputs("6","9","")
        self.assertFalse(is_valid)

    def test_min_x_is_not_digit(self):
        gui = Gui()
        is_valid = gui.validate_inputs("t","9","2*x")
        self.assertFalse(is_valid)

    def test_max_x_is_not_digit(self):
        gui = Gui()
        is_valid = gui.validate_inputs("4","p","2*x")
        self.assertFalse(is_valid)

    def test_min_x_greater_than_max_x(self):
        gui = Gui()
        is_valid = gui.validate_inputs("7","4","6-x*2")
        self.assertFalse(is_valid)

    def test_only_numbers_function(self):
        gui = Gui()
        is_valid = gui.validate_x("7857")
        self.assertFalse(is_valid)

    def test_invalid_character_in_function(self):
        gui = Gui()
        is_valid = gui.validate_function("7*v")
        self.assertFalse(is_valid)

    def test_invalid_symbols_in_function(self):
        gui = Gui()
        is_valid = gui.validate_function("8#x")
        self.assertFalse(is_valid)

    def test_all_valid_inputs_simple(self):
        gui = Gui()
        is_valid = gui.validate_inputs("4","9","5*x**3 + 2*x")
        self.assertTrue(is_valid)

    def test_all_valid_inputs_complex(self):
        gui = Gui()
        is_valid = gui.validate_inputs("7","900","2*x-6 ** 3 / x + x -3+6+0/2-x")
        self.assertTrue(is_valid)

    def test_all_valid_inputs_negative_min_x(self):
        gui = Gui()
        is_valid = gui.validate_inputs("-9","89","0 * 8888 + x - x / 1 + - 4")
        self.assertTrue(is_valid)

# This class assumes that the user inputs are correct and it tests the plotting.
class TestPlotting(unittest.TestCase):

    def test_plot_simple(self):
        gui = Gui()
        x = np.linspace(2, 6, 6)
        y = np.square(x)
        plot, = gui.plot("2", "6", "x**2")
        y_data = plot.get_data()[1]
        x_data = plot.get_data()[0]
        self.assertTrue((y == y_data).all())
        self.assertTrue((x == x_data).all())

    def test_plot_medium(self):
        gui = Gui()
        x = np.linspace(3, 90, 90)
        y = x+2
        plot, = gui.plot("3", "90", "x+2")
        y_data = plot.get_data()[1]
        x_data = plot.get_data()[0]
        self.assertTrue((y == y_data).all())
        self.assertTrue((x == x_data).all())

    def test_plot_complex(self):
        gui = Gui()
        x = np.linspace(-9, 130, 130)
        y = x+2-4/3+x
        plot, = gui.plot("-9", "130", "x+2-4/3+x")
        y_data = plot.get_data()[1]
        x_data = plot.get_data()[0]
        self.assertTrue((y == y_data).all())
        self.assertTrue((x == x_data).all())

    def test_plot_very_complex(self):
        gui = Gui()
        x = np.linspace(23, 240, 240)
        y = x+2-4/3+x-0+5*x-1+0*9
        plot, = gui.plot("23", "240", "x+2-4/3+x-0+5*x-1+0*9")
        y_data = plot.get_data()[1]
        x_data = plot.get_data()[0]
        self.assertTrue((y == y_data).all())
        self.assertTrue((x == x_data).all())





if __name__ == '__main__':
    unittest.main()
