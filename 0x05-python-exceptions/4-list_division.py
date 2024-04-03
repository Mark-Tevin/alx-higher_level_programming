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
            result.append(0)  # Set result to 0 when division by 0 occurs
        except IndexError:
            errors.append("out of range")
            result.append(0)  # Set result to 0 when index is out of range
        except TypeError:
            errors.append("wrong type")
            result.append(0)  # Set result to 0 when there is a type error
        except Exception as e:
            errors.append("an error occurred: {}".format(e))
            result.append(0)  # Set result to 0 when other exceptions occur

    if errors:
        for error in errors:
            print(error)

    return result
