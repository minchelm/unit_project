from unit_dict import unit_dict  # connects other file w/ dictionary

dictionaries = unit_dict()


def input_to_list(user_input):
    # input from user [value (type float), initial units (type string), final units (type string)]
    user_input = user_input.split()
    if len(user_input) != 3:  # if there is not three inputs will loop again
        return None, None, None
    else:
        value = float(user_input[0])  # float value
        units_from = str(user_input[1])  # initial units
        units_to = str(user_input[2])  # final units
        return value, units_from, units_to


