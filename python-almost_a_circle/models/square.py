#!/usr/bin/python3
"""Square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getting the good stuf"""
        return self.width

    @size.setter
    def size(self, value):
        """setting the good stuf"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """defining self"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
