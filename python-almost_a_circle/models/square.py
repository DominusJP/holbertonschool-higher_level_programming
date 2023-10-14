#!/usr/bin/python3
from models.rectangle import Rectangle
"""Square that inherits from rectangle"""


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """defining self"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
