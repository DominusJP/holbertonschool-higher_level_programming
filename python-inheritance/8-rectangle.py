#!/usr/bin/python3
"""querido python inheritance"""


class BaseGeometry:
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        :raises Exception: Always raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value for being an integer and greater than 0.
        :param name: The name of the value (a string).
        :param value: The value to validate.
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with the given width and height.
        :param width: The width of the rectangle (must be a positive integer).
        :param height: The height of the rectangmust be a positive integer).
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
