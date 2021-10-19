from abc import abstractmethod
import os

PATH = os.path.join('./files/')

class TypeParent():
    
    @abstractmethod
    def get_data():
        pass

    def get_dict(self):
        for attribute, value in self.dict.items():
            print(attribute, ': ', value)

class FileParent(TypeParent):
    def __init__(self, filename):
        self.filename = filename

