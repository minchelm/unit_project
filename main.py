from unit_dict import unit_dict  # connects other file w/ dictionary

dictionaries = unit_dict()

while True:  # for repeatability and exiting program
    # input from user [value (type float), initial units (type string), final units (type string)]
    number_initial = input().split()
    if number_initial[0] == "end":  # if user types "end", exits loop
        break
    elif len(number_initial) != 3:  # if there is not three inputs will loop again
        print(
            "Not enough values: '<value> <initial units> <final units>' "
        )  # error stated
    else:
        try:
            number = float(number_initial[0])  # float value
            units_from = str(number_initial[1])  # initial units
            units_to = str(number_initial[2])  # final units
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
                        dictionary.get(units_from) * number
                    )  # converts to standard value (m, kg)
                    unit_final = units_standard / dictionary.get(
                        units_to
                    )  # converts standard value to final value
                    print(unit_final, units_to)  # prints desired value and units
                    print_test = True  # notifies if conversion happens
                    break
            if (
                print_test is False
            ):  # if no print happens, the units were unknown somehow
                print("Unknown units")
        except ValueError:
            print(
                "Incorrect format: '<value> <initial units> <final units>' "
            )  # shows correct format
            continue
