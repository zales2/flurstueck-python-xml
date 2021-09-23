from flurstueck import Flurstueck

filenameInput = input('Podaj nazwę pliku wraz z jego rozszerzniem (przyklad.xml): ')
if '.json' in filenameInput:
    filetypeInput = 'json'
else:
    filetypeInput = input('Podaj format danych (nas / aaa): ')

flurstueck = Flurstueck(filenameInput, filetypeInput)
flurstueck.search_in_file()
flurstueck.get_dict()

