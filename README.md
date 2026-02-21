# unit_project
A software to go hand and hand with Desmos to quickly convert between units without searching

Purpose: takes one user input in the format of value, initial units, final units, and converts to final units, prints.

- Functions:
	- input_to_list(str): 
		- splits string up by whitespace
		- converts str to necessary variable type
		- returns all three variables
		- Error Prevention:
			- detects if user types "end", ends program
			- detects if user did not state input in right format
	- print_conversions():
		- calls input_to_string with user input
		- detects if user ended program or if input was incorrect continues loop or not respectively
		- parses through unit conversion dictionaries in unit_dict.py
		- converts value to requested units
		- Error Prevention:
			- detects if the units were unknown or incorrect
			- detects if value is not a number
	- main():
		- loops while run is true, only false when user types "end"

- FUTURE GOALS:
	- interface
	- handwritten Desmos-like program
	- able to take any unit names
		- like km, kilometers, kilometres
	- program ends when escape is pressed
- My issues with Desmos:
	- lack of constants, cant call them when needed, have to pull them individually
	- cant have separate windows for different calculations, all in one line
	- graph is separate program, cant run concurrently
	- multiple answers, only one above.
	
