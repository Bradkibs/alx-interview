#!/usr/bin/python3
""" 90 deg clockwise matrix rotation"""


def rotate_2d_matrix(matrix):
    """An inplace 90 deg rotation of an N X N matrix"""
    matrix[:] = list(zip(*matrix[::-1]))
