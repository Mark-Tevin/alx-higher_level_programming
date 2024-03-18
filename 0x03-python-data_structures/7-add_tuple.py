#!/usr/bin/python3

def add_tuple(tuple1=(), tuple2=()):
    # Ensure each tuple has at least 2 integers by padding with zeros if necessary
    tuple1 = tuple1[:2] + (0,) * (2 - len(tuple1))
    tuple2 = tuple2[:2] + (0,) * (2 - len(tuple2))

    # Add the first 2 integers of each tuple
    result = (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
    return result
