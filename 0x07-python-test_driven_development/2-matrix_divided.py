#!/usr/bin/python3
""" Defines a function: matrix_divided
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
"""


def matrix_divided(matrix, div):
    """Divides all element of a matrix by a divisor
    Args:
        matrix (list): A list of lists of ints or floats
        div (int/float): The divisor
    Returns:
        A new matrix representing the result of the division"""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    return [(list(map(lambda x: round(x / div, 2), row))) for row in matrix]

