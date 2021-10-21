from flurstueck import *
import json

class JsonType(FileParent):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.file = json.load( open( filepath ) )
        self.listType = [ 'cadastreNo', 'area', 'landKey', 'kreisKey', 'gemeindeKey', 'gemarkungKey']
        self.dict = {'Numer działki': '', 
            'Wielkość działki': '', 
            'Numer landu': '',
            'Numer gemarkung': '', 
            'Numer okręgu': '', 
            'Numer powiatu': ''}

    def execute(self):
        dictNames = iter(list(self.dict))
        for attribute, value in self.file.items():
            if attribute in self.listType:
                self.dict.update({next(dictNames): value})
        super().execute()
