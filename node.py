from enum import Enum


class Color(Enum):
    RED = "red"
    BLACK = "black"


class Node:

    def __init__(self, value):
        self.__parent = None
        self.__color = Color.RED
        self.__rightChild = None
        self.__leftChild = None
        self.__value = value

    def get_leftChild(self):
        return self.__leftChild

    def get_rightChild(self):
        return self.__rightChild

    def get_parent(self):
        return self.__parent

    def get_color(self):
        return self.__color

    def get_value(self):
        return self.__value

    def set_leftChild(self, leftChild):
        self.__leftChild = leftChild

    def set_rightChild(self, rightChild):
        self.__rightChild = rightChild

    def set_color(self, color):
        self.__color = color

    def set_parent(self, parent):
        self.__parent = parent
