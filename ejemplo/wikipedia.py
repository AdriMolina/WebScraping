import requests
from lxml import html #pip3 install lxml

#Generamos un encabezado con la información de los navegadores y sistemas operativos que asemejan el uso como un usuario común
encabezado={
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.03578.80 Safari/537.36"
}

url = "https://www.wikipedia.org/"


respuesta = requests.get(url,headers=encabezado)
#print(respuesta.text)

parser = html.fromstring(respuesta.text)
español = parser.get_element_by_id("js-link-box-es")
print (español.text_content())