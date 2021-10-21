from abc import abstractmethod

class TypeParent():  
    @abstractmethod
    def execute(self):
        for attribute, value in self.dict.items():
            print(attribute, ': ', value)

class FileParent(TypeParent):
    def __init__(self, filepath):
        self.filepath = filepath
    
