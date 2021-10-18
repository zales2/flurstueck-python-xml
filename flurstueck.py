import xml.etree.ElementTree as ET
import json
import os

PATH = os.path.join('./files/')

class File():
    def __init__(self, filename):
        self.filename = filename
        self.dict = {'Numer działki': '', 
                'Wielkość działki': '', 
                'Numer landu': '', 
                'Numer okręgu': '', 
                'Numer powiatu': '',    
                'Numer gemarkung': '' }

    def search_in_file(self):
        dictNames = iter(list(self.dict))
        if hasattr(self, 'xmlns') == False:
            for attribute, value in self.file.items():
                if attribute in self.listType:
                    self.dict.update({next(dictNames): value})
        else:
            for elem in self.listType:
                for tag in list(self.file.iter(self.xmlns + elem)):
                    if self.xmlns + elem == tag.tag:
                        self.dict.update({next(dictNames): tag.text})
                        break
        
    def get_dict(self):
        for attribute, value in self.dict.items():
            print(attribute, ': ', value)

class NasType(File):
    def __init__(self, filename):
        super().__init__(filename)
        self.file = ET.parse( PATH + filename ).getroot()
        self.listType = [ 'flurstueckskennzeichen', 'amtlicheFlaeche', 'land', 'kreis', 'gemeinde', 'gemarkungsnummer' ]
        self.xmlns = '{http://www.adv-online.de/namespaces/adv/gid/6.0}'

class AaaType(File):
    def __init__(self, filename):
        super().__init__(filename)
        self.file = ET.parse( PATH + filename ).getroot()
        self.listType = [ 'flstkennz', 'flaeche', 'landschl', 'kreisschl', 'gmdschl', 'gemaschl' ]
        self.xmlns = '{http://repository.gdi-de.org/schemas/adv/produkt/alkis-vereinfacht/2.0}'

class JsonType(File):
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



