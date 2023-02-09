from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["RickAndMorty"] #nombre de mi BBDD

def perfil_id(id=""):
    url = "https://rickandmortyapi.com/api/character/avatar/"
    url=url + str(id) + ".jpeg"

    return "{url}".format(url=url)