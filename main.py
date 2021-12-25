from baza import *


if __name__ == '__main__':

    izbor = ''
    while izbor != 'y':
        opcija = input('Ako zelite da unesete film izaberite opciju 1, da izlistate sve filmove opcija 2, za izlaz iz programa opcija "y": ')
        if opcija == '1':
            unos_filma()
        elif opcija == '2':
            prikaz_filmova()
        elif opcija == 'y':
            print('Dovidjenja!')
            izbor = 'y'
        else:
            print('Niste odabrali ni jednu ponudjenu opciju!')



