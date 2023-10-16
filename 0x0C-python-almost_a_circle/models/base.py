#!/usr/bin/python3
""" define base module """

import json
import csv
import turtle
import time


class Base:
    """ define Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """" initializing the instance """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file """

        filename = cls.__name__ + ".json"
        list_data = []
        if list_objs is not None:
            for i in list_objs:
                list_data.append(i.to_dictionary())

        text = cls.to_json_string(list_data)

        with open(filename, "w") as file:
            file.write(text)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representations"""
        json_list = []
        if json_string is None or json_string == "":
            return []
        else:
            json_list = json.loads(json_string)
            return json_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set """

        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        else:
            return None

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                text = file.read()
        except FileNotFoundError:
            return []
        list_dict = Base.from_json_string(text)
        list_instance = []
        for dictionary in list_dict:
            list_instance.append(cls.create(**dictionary))

        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs and saves to file """
        filename = cls.__name__ + ".csv"
        list_dict = []

        with open(filename, "w") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())

                headers = list(list_dict[0].keys())

                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""

        try:
            filename = cls.__name__ + ".csv"
            list_data = []
            list_dict = []
            list_obj = []
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for r in reader:
                    list_data.append(r)
                for i in list_data[1:]:
                    d = {}
                    for index, value in enumerate(i):
                        d.update({list_data[0][index]: int(value)})
                    list_dict.append(d)
                # print(list_dict)

                for dictionary in list_dict:
                    list_obj.append(cls.create(**dictionary))

                return list_obj

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""

        list_rect = []
        for rec in list_rectangles:
            list_rect.append(rec.to_dictionary())

        list_sq = []
        for sq in list_squares:
            list_sq.append(sq.to_dictionary())

        # drawing
        sc = turtle.Screen()
        tr = turtle.Turtle()
        tr.speed(3)
        tr.fillcolor("green")

        for rec in list_rect:
            tr.setposition(rec["x"], rec["y"])
            tr.begin_fill()
            for i in range(2):
                tr.fd(rec["width"])
                tr.right(90)
                tr.fd(rec["height"])
                tr.right(90)

            tr.end_fill()
            time.sleep(1)
            tr.clear()

        for sq in list_sq:
            tr.setposition(sq["x"], sq["y"])
            tr.begin_fill()
            for i in range(2):
                tr.fd(sq["size"])
                tr.right(90)
                tr.fd(sq["size"])
                tr.right(90)

            tr.end_fill()
            time.sleep(1)
            tr.clear()
