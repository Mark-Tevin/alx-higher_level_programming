# functions.py

from typing import List, Union

def islower(c: str) -> bool:
    """
    Check if a character is lowercase.

    Parameters:
    c (str): The character to check.

    Returns:
    bool: True if the character is lowercase, False otherwise.
    """
    return c.islower()

def uppercase(s: str) -> str:
    """
    Convert a string to uppercase.

    Parameters:
    s (str): The string to convert.

    Returns:
    str: The string converted to uppercase.
    """
    return s.upper()

def print_last_digit(number: int) -> None:
    """
    Print the last digit of a number.

    Parameters:
    number (int): The number to extract the last digit from.
    """
    print(abs(number) % 10)

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The result of adding a and b.
    """
    return a + b

def pow(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculate the power of a number.

    Parameters:
    a (int or float): The base.
    b (int or float): The exponent.

    Returns:
    int or float: The result of a raised to the power of b.
    """
    return a ** b

def insert_node(head: List[int], number: int) -> List[int]:
    """
    Insert a node in a linked list.

    Parameters:
    head (List[int]): The head of the linked list.
    number (int): The number to insert.

    Returns:
    List[int]: The head of the linked list after insertion.
    """
    if not head:
        head.append(number)
    else:
        i = 0
        while i < len(head) and head[i] < number:
            i += 1
        head.insert(i, number)
    return head
