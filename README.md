Sposób uruchomienia programu:

1. Wpisanie do wiersza poleceń następującej formuły: 'cd "ścieżka docelowa folderu, w którym znajduje się program"'
2. Zatwierdzenie enterem
3. Wpisanie do wiersza poleceń następującej formuły: 'python main.py'
4. Zatwierdzenie enterem
5. Wykonywanie poleceń pojawiających się w konsoli i zatwierdzanie ich enterem.

Opis działania programu:

W pliku flurstueck.py znajduje się stowrzona klasa Flurstueck zaopatrzona w funkcje.
Jej celem jest przechowywanie danych jakie użytkownik wprowadza do konsoli, korzystanie z nich, a następnie umożliwienie ich wywołania.
Funkcja search_in_file służaca do wyciągania danych z plików korzysta z wbudowanych bilbiotek xml.etree.ElementTree oraz json, które pozwalają obsługiwać pliki .xml oraz .json.
W pliku main.py zostają wywołane polecenia takie jak pobranie danych od użytkownika, sworzenie obiektu klasy Flurstueck i wywołanie jego funkcji.
