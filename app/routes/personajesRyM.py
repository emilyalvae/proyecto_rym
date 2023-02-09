from flask import Blueprint,render_template, request, flash
from app.models.personajes import Personajes
from app.db import db, perfil_id
import requests

personajes_ruta=Blueprint("personajes_ruta", __name__)

@personajes_ruta.route("/")
def index():
    personajes=db.personajes.find()
    return render_template("index.html", personajes=personajes)

@personajes_ruta.route("/profile/<id>")
def profile(id):
    id=int(id)
    data=db.personajes.find({"id":id})

    perfil = perfil_id(id)
    return render_template("perfil.html", perfil=perfil, data=data)

@personajes_ruta.route("/insert")
def inserPersonaje():
    n=1
    url="https://rickandmortyapi.com/api/character?page="
        
    url_personaje=url+ str(n)
    response = requests.get(url_personaje)
    datos=response.json()

    lista_personajes=[]
    for y in datos["results"]:
        infor=Personajes(y["id"], y["name"], 
        y["status"], y["species"], 
        y["type"], y["gender"], 
        y["origin"]["url"], y["location"]["name"], 
        y["image"], y["episode"], y["url"], y["created"])

        db.personajes.insert_one(infor.to_json())

    flash("Personajes insertados","success")

    return "Personajes insertados"

@personajes_ruta.route("/Perfil")
def perfil():
    return render_template("perfil.html")