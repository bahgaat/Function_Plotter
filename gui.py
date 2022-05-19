from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# This class when calling "show_graph_on_the_screen" function shows a form to the user to choose the desired x_axis range
# and function and then show the desired graph on the screen if there is no error."show_graph_on_the_screen" function has to be called only
# once and then the user can enter as many times as he wants his desired x_axis and function and the graph will be shown.
class Gui:

    # get min_x, max_x, and function from the user and either
    # print appropriate error message if there is an error or show graph on the screen
    def show_graph_on_the_screen(self):
        root = Tk()
        root.title("Fill the form")
        root.geometry("300x200")
        Label(root,text="min_x").place(x=20,y=20)
        Label(root,text="max_x").place(x=20,y=70)
        Label(root,text="function").place(x=20,y=110)
        global min_x_entry
        global max_x_entry
        global function_entry

        min_x_entry = Entry(root,bd=5)
        min_x_entry.place(x=140, y=20)

        max_x_entry = Entry(root,bd=5)
        max_x_entry.place(x=140, y=70)

        function_entry = Entry(root,bd=5)
        function_entry.place(x=140, y=110)

        Button(root,text="Show graph",command=self.show_graph, height=2, width=17, bd=6).place(x=100,y=140)
        root.mainloop()

    # When the user clicks "Show graph" this function either shows appropriate error message
    # if there is an error or shows the graph
    def show_graph(self):
        min_x = min_x_entry.get()
        max_x = max_x_entry.get()
        function = function_entry.get()
        is_valid = self.validate_inputs(min_x, max_x, function)
        if is_valid:
            self.plot(min_x, max_x, function)
            self.show()
        else:
            self.print_appropriate_error_message(min_x, max_x, function)

    # check that the user fill all the fields correctly
    def validate_inputs(self, min_x, max_x, function):
        if min_x == "" or max_x == "" or function == "":
            return False
        elif not min_x.isdigit() and (min_x.startswith("-") and min_x[1:].isdigit()) == False:
            return False
        elif not max_x.isdigit():
            return False
        elif int(min_x) >= int(max_x):
            return False
        elif not self.validate_function(function) or not self.validate_x(function):
            return False
        else:
            return True

    # print appropriate error message to the user if there is an error
    def print_appropriate_error_message(self, min_x, max_x, function):
        if min_x == "":
            messagebox.showinfo("","min_x can't be empty")
        elif max_x == "":
            messagebox.showinfo("","max_x can't be empty")
        elif function == "":
            messagebox.showinfo("","function can't be empty")
        elif not min_x.isdigit() and (min_x.startswith("-") and min_x[1:].isdigit()) == False:
            messagebox.showinfo("","min_x must be a number")
        elif not max_x.isdigit():
            messagebox.showinfo("","max_x must be a positive number")
        elif int(min_x) >= int(max_x):
            messagebox.showinfo("","max_x must be greater than min_x")
        elif not self.validate_function(function):
            messagebox.showinfo("","Please write valid function, Only acceptable inputs are digit, space, '+', '-', '*', '**', '/', 'x'")
        elif not self.validate_x(function):
            messagebox.showinfo("",'A function must include x')

    # check that that the function doesn't contain any invalid symbols
    def validate_function(self, function):
        valid_symbols = {'+', '-', '*', '**', 'x', '/'}
        for element in function:
            if (not element.isspace() and not element.isdigit() and element not in valid_symbols):
                return False
        return True

    # check that the function contains x
    def validate_x(self, function):
        result = False
        for element in function:
            if (element == 'x'):
                result = True
        return result

    # treat min_x and max_x as the x_axis and the function as the y_axis and plot them
    def plot(self, min_x, max_x, function):
        plot = plt.figure()
        # x axis values
        x = np.linspace(int(min_x), int(max_x), int(max_x))
        # corresponding y axis values
        y = eval(function)
        # plotting the points
        return plt.plot(x, y)

    # show the graph
    def show(self):
        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')
        # giving a title to my graph
        plt.title('My first graph!')
        plt.show()


def main():
    gui = Gui()
    gui.show_graph_on_the_screen()

if __name__ == "__main__":
    main()
