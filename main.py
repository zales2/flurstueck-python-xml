from flurstueck import *

file_list = os.listdir(PATH)
while(True):
    filenameInput = input('Podaj nazwę pliku wraz z jego rozszerzniem: ')
    if filenameInput in file_list:
        break
    else:
        print('Zła nazwa pliku, spróbuj ponownie!')

while(True):
    filetypeInput = input( 'Podaj format danych (nas / aaa / json): ')
    if filetypeInput in ['nas', 'aaa', 'json']:
        break
    else:
        print('Nieprawidłowy format, spróbuj ponownie!')

if filetypeInput == 'nas':
    fluerstueck = NasType( filenameInput )
elif filetypeInput == 'aaa':
    fluerstueck = AaaType( filenameInput )
elif filetypeInput == 'json':
    fluerstueck = JsonType( filenameInput )

fluerstueck.search_in_file()
fluerstueck.get_dict()
