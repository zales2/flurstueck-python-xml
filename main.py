from flurstueck import Flurstueck

filenameInput = input('Podaj nazwę pliku: ')
if '.json' in filenameInput:
    filetypeInput = 'json'
else:
    filetypeInput = input('Podaj format danych (nas / aaa): ')

flurstueck = Flurstueck(filenameInput, filetypeInput)
flurstueck.search_xml()
flurstueck.get_dict()

