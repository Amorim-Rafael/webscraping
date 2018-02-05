import requests
import json
from time import sleep
from random import randint
from bs4 import BeautifulSoup

page = requests.get("https://www.airbnb.com.br/s/Aracati--CE/homes?place_id=ChIJux4AVuexuQcRubp62W-WefY&refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=XYrjc6V_")

soup = BeautifulSoup(page.content, 'html.parser')
# Tag script onde está o retorno após o request
scripts = soup.find('script', {"data-hypernova-key":"spaspabundlejs"}).get_text().replace("<!--","").replace("-->","")
# Lista da paginação
ul = soup.find('ul', {"data-id":"SearchResultsPagination"})

# Link de passa para a proxima pagina
# li = ul.find(class_="_b8vexar")
# a = li.find(class_="_1ip5u88")

# Pega a ultima pagina
li = ul.find_all('li', class_="_1am0dt")[-1]
a = li.find(class_="_1ip5u88")
last_page = int(a.find('div', class_='_1bdke5s').get_text())

print(last_page)

pages = [str(i) for i in range(1,last_page)]

print(pages)


# js = json.loads(scripts)
# listings = js['bootstrapData']['reduxData']['exploreTab']['response']['explore_tabs'][0]['sections'][0]['listings']

# for listing in listings:
#     print("Nome:{0}\nEndereço:{1}\nLatitude:{2}\nLongitude:{3}\nValor:{4}".format(listing['listing']['name'], listing['listing']['neighborhood_overview'], listing['listing']['lat'], listing['listing']['lng'], listing['pricing_quote']['rate']['amount_formatted']))
#     print("-----------------------------------------------------------------------------\n")
# nome, endereço, latlgn, valor, de onde vem