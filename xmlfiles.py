from flurstueck import *
import xml.etree.ElementTree as ET

class XmlFiles(FileParent):
    def __init__(self, filename):
        super().__init__(filename)
        self.file = ET.parse( PATH + filename ).getroot()
        self.dict = {'Numer działki': '', 
                'Wielkość działki': '', 
                'Numer landu': '', 
                'Numer okręgu': '', 
                'Numer powiatu': '',    
                'Numer gemarkung': '' }

    def get_data(self):
        dictNames = iter(list(self.dict))        
        for elem in self.listType:
            for tag in list(self.file.iter(self.xmlns + elem)):
                if self.xmlns + elem == tag.tag:
                    self.dict.update({next(dictNames): tag.text})
                    break

