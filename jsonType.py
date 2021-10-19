from flurstueck import *
import json

class JsonType(FileParent):
    def __init__(self, filename):
        super().__init__(filename)
        self.file = json.load( open( PATH + filename) )
        self.listType = [ 'cadastreNo', 'area', 'landKey', 'kreisKey', 'gemeindeKey', 'gemarkungKey']
        self.dict = {'Numer działki': '', 
            'Wielkość działki': '', 
            'Numer landu': '',
            'Numer gemarkung': '', 
            'Numer okręgu': '', 
            'Numer powiatu': ''}

    def get_data(self):
        dictNames = iter(list(self.dict))
        for attribute, value in self.file.items():
            if attribute in self.listType:
                self.dict.update({next(dictNames): value})

