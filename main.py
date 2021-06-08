import os #czyszczenie ekranu w pythonie
from lotnisko import Lotnisko
from linialotnicza import Linialotnicza
from klient import Klient

#tu bedzie trzeba importowac wszysko
from samolot import Samolot

linialotnicza = Linialotnicza('', [], [], [], [])
linialotnicza.odczyt()

wejscie=1
przejscie=1
while(wejscie!=0):
    if(przejscie==1):
        print("""Witaj w SYSTEMIE REZERWACJI BILETÓW!!
Razem z naszą aplikacją pomożemy Ci załatwić wszystkie obowiązki związane z rezerwacją biletów lotniczych.""")
   #moze jeszcze cos z trasami lotnisk zrobic, nie wiem co o tym myslisz
    #w sumie mozna ale nie wiem co z tymi trasami moznaby było zrobic
    # a i cos z zapisywaniem danych na dysk trzeba zrobic(i odczytywanie w sumie tez)
    #i jak czyscic ekran konsoli w tym pythonie smierdzacym
    print("""1. Zarządzaj lotniskiem
2. Zarządzaj samolotem
3. Zarządzaj klientem
4. Zarządzaj trasami
5. Zarządzaj biletem
6. Operacja na pliku
0. Zakończ program
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
    #w c da sie zrobic switch ale niew iemjak to jest w pythonie wiec zrobie na if-ach
    przejscie+=1
    wybor=input()

    if(wybor=="0"):
        print("Do zobaczenia!")
        break

    if(wybor=="1"):
        print("""1. Wyświetl liste lotnisk
2. Wyświetl ilosc lotnisk w bazie
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
        lotniskowywybor=input()
        if(lotniskowywybor=="1"):
            trasy=linialotnicza.getTrasy()

            licznik=0
            for i in trasy:
                a=i.getLotniska()
                for lotnisko in a:
                    licznik += 1
                    print("Lotnisko numer ", licznik)
                    print('Kraj:',lotnisko.getKraj())
                    print('Miasto: ',lotnisko.getMiasto())
                    print('ID: ',lotnisko.getId())
                    print('\n')

        if(lotniskowywybor=="2"):
            licznik = 0
            for i in trasy:
                a = i.getLotniska()
                licznik+=len(a)
            print('Liczba lotnisk jest równa: ',licznik)


    if(wybor=="2"):
        print("""1. Wyświetl liste samolotów
2. Wyświetl ilosc samolotów w bazie
3. Dodaj samolot
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
        samolotowywybor = input()
        if (samolotowywybor == "1"):
            samoloty = linialotnicza.getSamoloty()
            licznik = 0
            for samolot in samoloty:
                licznik += 1
                print("Samolot numer ", licznik)
                print('Zasieg samolotu:', samolot.getZasieg())
                print('ID: ', samolot.getId())
                print('Liczba miejsc: ', samolot.getLiczbamiejsc())
                print('\n')
            print()
        if (samolotowywybor == "2"):
            licznik = 0
            samoloty = linialotnicza.getSamoloty()
            for samolot in samoloty:
                licznik += 1
            print('Samolotow jest: ',licznik)

        if (samolotowywybor == "3"):
            zasieg = input('Podaj zasieg samolotu: ')
            id = input('Podaj ID samolotu: ')
            liczbamiejsc = input('Podaj liczbę miejsc w samolocie: ')
            linialotnicza.dodajSamolot(Samolot(zasieg,id,liczbamiejsc))




    if(wybor=="3"):
        print("""1. Wyświetl listę osób
2. Dodaj osobę
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
        coosoba=input()
        if(coosoba=="1"):
            print("Lista osob:")
            osoby = linialotnicza.getKlienci()
            licznik = 0
            for osoba in osoby:
                licznik += 1
                print("Osoba numer ", licznik)
                print('ID osoby: ', osoba.getId())

        if(coosoba=="2"):
            idklienta=input('Podaj ID Klienta: ')
            linialotnicza.dodajKlienta(Klient(idklienta))

    if(wybor=="4"):
        print("cos z trasami")

    if(wybor=="5"):
        print("""1. Wyświetl listę biletów
2. Dodaj bilet
3. Usuń bilet
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
        cobilet = input()
        if (cobilet == "1"):
            print("Listaosob: ")
        if (cobilet == "2"):
            print("Dodawanie osoby: ")
        if (cobilet == "3"):
            print("Usuwanie osoby: ")

    if (wybor == "6"):
        print("""1. Zapisz do pliku
2. Odczytaj z pliku
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
        plikwybor = input()
        if (plikwybor == "1"):
            linialotnicza.zapis()
        if (plikwybor == "2"):
            linialotnicza.odczyt()


    for i in range(2):
        print("\n")