import xml.etree.ElementTree as ET
import json

class Flurstueck():
    
    def __init__(self, filename, type):
        if type != 'json':
            self.xmlfile = ET.parse( '.\\files\\' + filename ).getroot()
            self.dict = {'Numer działki': '', 
                'Wielkość działki': '', 
                'Numer landu': '', 
                'Numer okręgu': '', 
                'Numer powiatu': '',    
                'Numer gemarkung': '' }
        self.type = type

        if type == 'nas':
            self.listType = [ 'flurstueckskennzeichen', 'amtlicheFlaeche', 'land', 'kreis', 'gemeinde', 'gemarkungsnummer' ]
            self.xmlns = '{http://www.adv-online.de/namespaces/adv/gid/6.0}'
        elif type == 'aaa':
            self.listType = [ 'flstkennz', 'flaeche', 'landschl', 'kreisschl', 'gmdschl', 'gemaschl' ]
            self.xmlns = '{http://repository.gdi-de.org/schemas/adv/produkt/alkis-vereinfacht/2.0}'
        else:
            file = open( '.\\files\\' + filename, )
            self.jsonfile = json.load(file)
            self.listType = [ 'cadastreNo', 'area', 'landKey', 'kreisKey', 'gemeindeKey', 'gemarkungKey']
            self.xmlns = ''
            self.dict = {'Numer działki': '', 
            'Wielkość działki': '', 
            'Numer landu': '',
            'Numer gemarkung': '', 
            'Numer okręgu': '', 
            'Numer powiatu': ''}

    def search_in_file(self):
        dictNames = iter(list(self.dict))
        if self.type == 'json':
            for attribute, value in self.jsonfile.items():
                if attribute in self.listType:
                    self.dict.update({next(dictNames): value})
        else:
            for elem in self.listType:
                for tag in list(self.xmlfile.iter(self.xmlns + elem)):
                    if self.xmlns + elem == tag.tag:
                        self.dict.update({next(dictNames): tag.text})
                        break

    def get_dict(self):
        for attribute, value in self.dict.items():
            print(attribute, ': ', value)