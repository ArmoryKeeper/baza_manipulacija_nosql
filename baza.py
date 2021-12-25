from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.test
filmovi = db.filmovi

def unos_filma():
    ime     = input('Unesi ime filma: ')
    zanr    = input('Unesi zanr filma: ')
    godina  = input('Unesi godinu filma: ')

    filmovi_details = {
        'ime':ime,
        'zanr':zanr,
        'godina':godina
    }

    filmovi.insert_one(filmovi_details)

def prikaz_filmova():
    queryresult = filmovi.find()
    for r in queryresult:
        print('Film: {}, zanr: {}, godina: {}'.format(r['ime'],r['zanr'],r['godina']))



