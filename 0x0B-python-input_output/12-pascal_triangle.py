#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    ls = [[0 for x in range(i + 1)] for i in range(n)]
    ls[0] = [1]

    for i in range(1, n):
        ls[i][0] = 1
        for j in range(1, i + 1):
            if j < len(ls[i - 1]):
                ls[i][j] = ls[i - 1][j - 1] + ls[i - 1][j]
            else:
                ls[i][j] = ls[i - 1][0]
    return ls
