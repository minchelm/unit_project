from unit_conversion import conversion
import tkinter as tk
import sys
import re
import math


def tokenize(expression):
    pattern = r"sin|cos|\d+\.?\d*|[+\-*/^()]"  #  searches for these symbols in expression
    raw_tokens = re.findall(
        pattern, expression.replace(" ", "")
    )  # removes white space
    tokens = []  # initializes token list
    i = 0
    while i < len(raw_tokens):  # loops through all tokens
        token = raw_tokens[i]

        if token == "-" and (
            i == 0 or raw_tokens[i - 1] in "+-*/("
        ):  # detects negative numbers
            tokens.append("u-")

        else:
            tokens.append(token)
        i += 1
    return tokens


def to_postfix(tokens):  # sets order
    precedence = {  # expression prececence... PEMDAS
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "u-": 3,
        "^": 4,
        "sin": 5,
        "cos": 5,
    }

    right_associative = {"^", "u-"}  # these are rightmost evaluations

    output = []
    operators = []

    for token in tokens:
        if token.replace(
            ".", "", 1
        ).isdigit():  # if it is a digit, appends to output
            output.append(token)

        elif token in (
            "sin",
            "cos",
        ):  # if it is an operator, appends to operator
            operators.append(token)

        elif token in precedence:  # sets order
            while (
                operators
                and operators[-1] in precedence
                and (
                    (
                        token not in right_associative
                        and precedence[operators[-1]] >= precedence[token]
                    )
                    or (
                        token in right_associative
                        and precedence[operators[-1]] > precedence[token]
                    )
                )
            ):
                output.append(operators.pop())

            operators.append(token)

        elif token == "(":  # detects parenthesis
            operators.append(token)

        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            operators.pop()  # remove '('

            if operators and operators[-1] in ("sin", "cos"):
                output.append(operators.pop())

    while operators:
        output.append(operators.pop())

    return output


def evaluate_postfix(postfix):  # evaluates the order and reformats
    stack = []

    for token in postfix:  # loops through all tokens
        if token.replace(
            ".", "", 1
        ).isdigit():  # if it is just a digit, appends that
            stack.append(float(token))

        elif token == "u-":  # if it is negative makes it negative
            stack.append(-stack.pop())

        elif token == "+":  # adds first two tokens
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)

        elif token == "-":  # subtracts first two tokens
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)

        elif token == "*":  # multplies first two tokens
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)

        elif token == "/":  # divides first two tokens
            b, a = stack.pop(), stack.pop()
            stack.append(a / b)

        elif token == "^":  # exponents
            b, a = stack.pop(), stack.pop()
            stack.append(a**b)

        elif token == "sin":  # sin
            stack.append(math.sin(stack.pop()))

        elif token == "cos":  # cos
            stack.append(math.cos(stack.pop()))

    return stack[0]


def calculations(user_input):  # pipeline for evaluating expression
    tokens = tokenize(user_input)  # turns each into token list
    postfix = to_postfix(tokens)  # sets order
    result = evaluate_postfix(postfix)  # evaluates based on order
    return result


class Calculator_Window:
    root = tk.Tk()  # creates window
    root.geometry("1000x500")  # sets window size
    root.title("Calculator")  # names window
    input_var = tk.StringVar()  # initialized variable instance of input
    output_var = tk.StringVar()  # initialized variable instance of output
    input_entries = []
    output_labels = []

    def calculate(
        self, event=None
    ):  # if any button pressed, attempts to calculate expression
        try:
            self.output_var.set(calculations(self.input_var.get()))
        except Exception:
            self.output_var.set("Calc Error")

    def new_expression(self, event=None, count=0):  # adds new expression
        self.input_entries.append(  # adds entry one row below last
            tk.Entry(
                self.root,
                textvariable=self.input_var,
                bg="white",
                fg="black",
                width=30,
            )
        )
        self.input_entries[self.count].grid(
            row=self.count, column=0
        )  # input entry
        self.input_entries[self.count].focus_set()  # sets focus to this entry
        self.output_labels.append(  # adds label one row below last
            tk.Label(
                self.root,
                textvariable=self.output_var,
                bg="white",
                fg="black",
                width=30,
            )
        )
        self.output_labels[self.count].grid(row=self.count, column=1)
        self.count += 1  # increases count

    def delete_expression(
        self, event=None, count=0
    ):  # deletes added expressions
        if self.count == 1:  # if there is only one, wont delete it
            return
        entry = self.input_entries.pop()  # removes last entry from list
        label = self.output_labels.pop()  # removes last label from list
        entry.destroy()  # destroys it from window
        label.destroy()  # destroys it from window
        self.count -= 1  # decreases count

    def make_window(self):  # makes initial window
        self.count = 0
        self.root.lift()  # lifts window to front
        self.root.focus_force()  # forces it into focus
        self.root.bind(
            "<Return>", self.new_expression
        )  # enter button calls calculate
        self.root.bind("<Escape>", self.end_program)  # escape ends program
        self.root.bind("<Command-x>", self.delete_expression)
        self.root.bind(
            "<Command-c>", self.copy_output
        )  # command c copies output
        self.root.bind("<Key>", self.calculate)
        # Labels
        self.new_expression()

    def end_program(self, event=None):  # function to quit program
        self.root.destroy()
        sys.exit()

    def copy_output(self, event=None):  # function to copy output
        self.root.clipboard_clear()  # clears clipboard
        value = self.output_var.get().split()[-2]  # only copies value
        self.root.clipboard_append(value)
