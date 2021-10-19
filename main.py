from flurstueck import *
from jsonType import JsonType
from aaaType import AaaType
from nasType import NasType


types = { 'nas': NasType, 
    'aaa': AaaType, 
    'json': JsonType } # add new type

while(True):
    filetypeInput = input( 'Podaj format danych (nas / aaa / json): ')
    if filetypeInput in types:
        if issubclass(types[filetypeInput], FileParent):
            file_list = os.listdir(PATH)
            while(True):
                filenameInput = input('Podaj nazwę pliku wraz z jego rozszerzniem: ')
                if filenameInput in file_list:
                    fluerstueck = types[filetypeInput](filenameInput)
                    break
                else:
                    
                    print('Zła nazwa pliku, spróbuj ponownie!')
            break
        
        else:
            # other type than file
            # fluerstueck = types[filetypeInput](some new parameter/parameters)
            break
    else:
        print('Nieprawidłowy format, spróbuj ponownie!')

fluerstueck.get_data()
fluerstueck.get_dict()
