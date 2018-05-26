from . import constants


def calculate_rectangle_area(width, height):
    return width * height


def calculate_triangle_area(base, height):
    return base * height / 2


def calculate_circle_area(radius):
    return radius * (constants.PI ** 2)
