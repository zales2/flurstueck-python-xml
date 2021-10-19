from xmlfiles import XmlFiles

class NasType(XmlFiles):
    def __init__(self, filename):
        super().__init__(filename)
        self.listType = [ 'flurstueckskennzeichen', 'amtlicheFlaeche', 'land', 'kreis', 'gemeinde', 'gemarkungsnummer' ]
        self.xmlns = '{http://www.adv-online.de/namespaces/adv/gid/6.0}'

