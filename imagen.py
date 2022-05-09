import requests
import matplotlib.pyplot as plt
import matplotlib.image as img
from requests.api import request
from requests.models import Response


#Devuelve una imagen 
if __name__== '__main__':
    url='https://imgur.com/aJjAf4M.jpg'

    response= requests.get(url,stream=True)
    with open('image.jpg', 'wb') as file :
            for chunk in response.iter_content():
                file.write(chunk)

    response.close()
##################################################
