import requests
import matplotlib.pyplot as plt
import matplotlib.image as img
from requests.api import request
from requests.models import Response

#Devuelve un listado de peliculas con informacion
respuesta= requests.get('https://yts.mx/api/v2/list_movies.json')
data=respuesta.json()
result =data['data']
movies=result ['movies']


for movie  in movies:
        titulo =movie['title']
        anio=movie['year'] 
        genero=movie['genres']
        print('Titulo:', titulo)
        print('Genero:', genero)
        print('Año:', anio)
        print("\n")
#####################################################  
