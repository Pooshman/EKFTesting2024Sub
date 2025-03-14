"""
Various simple and tedious functions for getting data from ROS topics (used a lot in pix_standalone.py)
"""

class TopicService:
    def __init__(self, name: str, classType):
        self.__name = name
        self.__classType = classType
        self.__data = None

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        data = self.__data
        self.__data = None
        return data

    def get_data_last(self):
        return self.__data

    def get_type(self):
        return self.__classType

    def get_name(self):
        return self.__name
