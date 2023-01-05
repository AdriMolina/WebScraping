import requests
from lxml import html #pip3 install lxml

#USER AGENTE PARA PROTEGERNOS DE BANEOS

encabezado={
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.03578.80 Safari/537.36"
}

url = "https://www.wikipedia.org/"


respuesta = requests.get(url,headers=encabezado)
#print(respuesta.text)

parser = html.fromstring(respuesta.text)
#Información del ID
#español = parser.get_element_by_id("js-link-box-es")
#print (español.text_content())

#Información de Strong
español = parser.xpath("//a[@id='js-link-box-es']/strong/text()")

#Información de la clase
idiomas = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")

for idioma in idiomas:
    print (idioma)

print(idiomas)
