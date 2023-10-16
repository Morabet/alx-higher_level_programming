#!/usr/bin/python3
""" defile square module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ define class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """  overloading __str__ method """

        return f"[{self.__class__.__name__}] ({self.id}) " + \
            f"{self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, size):
        """ set size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Updates attributes of an instance """

        if args and len(args) != 0:
            list_args = list(args)
            if len(args) >= 2:
                list_args.insert(1, args[1])

            super().update(*list_args, **kwargs)

        elif kwargs and len(kwargs) != 0:
            if "size" in kwargs:
                kwargs["width"] = kwargs["size"]
                kwargs["height"] = kwargs.pop("size")

            super().update(*args, **kwargs)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        my_dict = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

        return my_dict
