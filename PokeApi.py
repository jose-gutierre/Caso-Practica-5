#Uso de la PokeApi
#Instalamos la libreria con ->pip install requests
import requests
import matplotlib.pyplot as plt
import matplotlib.image as img
from requests.api import request
from requests.models import Response

#Devuelve un pokemon de aucerdo a su nombre
pokemon = input("Introduce el nombre del POKEMON: ")
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon

respuesta= requests.get(url)

if respuesta.status_code !=200 :
    print("Pokemon no encontrado")
    exit()

imagen = img.imread(respuesta.json()['sprites']['front_default'])
plt.title(respuesta.json()['name'])
imgplot=plt.imshow(imagen)
plt.show()
#########################################




