#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    errors = []

    min_length = min(len(my_list_1), len(my_list_2))
    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
            result.append(division_result)
        except ZeroDivisionError:
            errors.append("division by 0")
            result.append(None)
        except IndexError:
            errors.append("out of range")
            result.append(None)
        except TypeError:
            errors.append("wrong type")
            result.append(None)
        except Exception as e:
            errors.append("an error occurred: {}".format(e))
            result.append(None)

    if errors:
        for error in errors:
            print(error)

    # Replace None values with 0
    result = [0 if value is None else value for value in result]

    return result
