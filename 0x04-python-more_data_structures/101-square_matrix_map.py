#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda submat: list(map(lamda e: e**2, submat)),matrix))
