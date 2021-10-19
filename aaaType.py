from xmlfiles import XmlFiles

class AaaType(XmlFiles):
    def __init__(self, filename):
        super().__init__(filename)
        self.listType = [ 'flstkennz', 'flaeche', 'landschl', 'kreisschl', 'gmdschl', 'gemaschl' ]
        self.xmlns = '{http://repository.gdi-de.org/schemas/adv/produkt/alkis-vereinfacht/2.0}'
        