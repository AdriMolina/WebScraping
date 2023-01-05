import requests
from bs4 import BeautifulSoup #pip3 install beautifulsoup4

#USER AGENTE PARA PROTEGERNOS DE BANEOS
headers1={
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.03578.80 Safari/537.36"
    }

#URL SEMILLA
url ='https://stackoverflow.com/questions'

#REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url , headers=headers1)

#PASEO DEL ARBOL CON BEAUTIFUL SOUP
soup = BeautifulSoup(respuesta.text)

contenedor_respuestas = soup.find(id="questions")
lista_preguntas = contenedor_respuestas.find_all('div', class_= "s-post-summary")

for pregunta in lista_preguntas:
    texto_pregunta = pregunta.find('h3').text
    descripcion_pregunta = pregunta.find(class_='s-post-summary--content-excerpt').text

    print(texto_pregunta)
    print(descripcion_pregunta)
