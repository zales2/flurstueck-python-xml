from flurstueck import *
import xml.etree.ElementTree as ET

class XmlFiles(FileParent):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.file = ET.parse( filepath ).getroot()
        self.dict = {'Numer działki': '', 
                'Wielkość działki': '', 
                'Numer landu': '', 
                'Numer okręgu': '', 
                'Numer powiatu': '',    
                'Numer gemarkung': '' }

    def execute(self):
        dictNames = iter(list(self.dict))        
        for elem in self.listType:
            for tag in list(self.file.iter(self.xmlns + elem)):
                if self.xmlns + elem == tag.tag:
                    self.dict.update({next(dictNames): tag.text})
                    break
        super().execute()
