from unit_dict import unit_dict  # connects other file w/ dictionary

dictionaries = unit_dict()


def input_to_list(user_input):
    # input from user [value (type float), initial units (type string), final units (type string)]
    user_input = user_input.split()
    if user_input[0] == "end":  # if user types "end", exits loop
        return None, None, None
    elif len(user_input) != 3:  # if there is not three inputs will loop again
        print(
            "Not enough values: '<value> <initial units> <final units>' "
        )  # error stated
        return -1, -1, -1
    else:
        value = float(user_input[0])  # float value
        units_from = str(user_input[1])  # initial units
        units_to = str(user_input[2])  # final units
        return value, units_from, units_to


def print_conversion():
    value, units_from, units_to = input_to_list(input())
    if value is None:
        return False
    if units_from != -1:
        try:
            print_test = False  # for parsing through dictionaries
            for (
                dictionary
            ) in dictionaries:  # goes through the dictionaries (currently only two)
                if (  # if either of the unit values are unknown
                    dictionary.get(units_from) is None
                    or dictionary.get(units_to) is None
                ):
                    continue
                else:  # if both units are in one dictionary, converts
                    units_standard = (
                        dictionary.get(units_from) * value
                    )  # converts to standard value (m, kg)
                    unit_final = units_standard / dictionary.get(
                        units_to
                    )  # converts standard value to final value
                    print(unit_final, units_to)  # prints desired value and units
                    print_test = True  # notifies if conversion happens
                    return True
            if (
                print_test is False
            ):  # if no print happens, the units were unknown somehow
                print("Unknown units")
        except ValueError:
            print(
                "Incorrect format: '<value> <initial units> <final units>'"
            )  # shows correct format
            return True
    return True


run = True
while run:
    run = print_conversion()
