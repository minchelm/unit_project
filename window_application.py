from unit_conversion import conversion
import tkinter as tk
import sys


class Unit_Window:
    history_count = 3  # initial row number of the history count
    root = tk.Tk()  # creates window
    root.geometry("475x600")  # sets window size
    root.title("Unit Converter")  # names window
    input_var = tk.StringVar()  # initialized variable instance of input
    output_var = tk.StringVar()  # initialized variable instance of output
    history_array = [None] * 28

    def calculate(self, event=None):
        if self.history_count == 28:
            self.history_count -= 25
        if self.history_count != 3:  # only begins after first conversion
            self.history_array[self.history_count - 3] = tk.Label(
                self.root,
                text=" " * 75,
                anchor="w",
            ).grid(
                row=self.history_count, column=1
            )  # creates history of output
            self.history_array[self.history_count - 3] = tk.Label(
                self.root, text=self.output_var.get(), anchor="w"
            ).grid(
                row=self.history_count, column=1
            )  # creates history of output
        self.history_count += 1
        self.output_var.set(
            conversion(self.input_var.get())
        )  # calls conversion function
        self.input_var.set("")  # resets input

    def make_window(self):
        self.root.lift()  # lifts window to front
        self.root.focus_force()  # forces it into focus
        self.root.bind(
            "<Return>", self.calculate
        )  # enter button calls calculate
        self.root.bind("<Escape>", self.end_program)  # escape ends program
        self.root.bind(
            "<Command-c>", self.copy_output
        )  # command c copies output
        # Labels
        tk.Label(self.root, text="Input", anchor="w").grid(
            row=1, column=0
        )  # input label

        tk.Label(self.root, text="Output", anchor="w").grid(
            row=2, column=0
        )  # output label

        tk.Label(
            self.root,
            textvariable=self.output_var,
            bg="white",
            fg="black",
            width=30,
        ).grid(
            row=2, column=1
        )  # conversion label

        tk.Label(self.root, text="History:", anchor="w").grid(
            row=4, column=0
        )  # history label
        # Buttons
        tk.Button(
            self.root, text="Stop", width=3, command=self.end_program
        ).grid(
            row=2, column=3
        )  # quit program button
        tk.Button(
            self.root, text="Enter", width=3, command=self.calculate
        ).grid(
            row=1, column=2
        )  # calculate button
        tk.Button(
            self.root, text="Copy?", width=3, command=self.copy_output
        ).grid(
            row=2, column=2
        )  # copy conversion button
        # Entries
        input_entry = tk.Entry(
            self.root,
            textvariable=self.input_var,
            bg="white",
            fg="black",
            width=30,
        )
        input_entry.grid(row=1, column=1)  # input entry
        input_entry.focus_set()

    def end_program(self, event=None):  # function to quit program
        self.root.destroy()
        sys.exit()

    def copy_output(self, event=None):  # function to copy output
        self.root.clipboard_clear()  # clears clipboard
        value = self.output_var.get().split()[-2]  # only copies value
        self.root.clipboard_append(value)
