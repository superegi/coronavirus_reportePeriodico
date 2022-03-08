# -*- coding: latin-1 -*-

import requests
import Funciones_Scraping as FS
import pandas as pd
import time

nav=FS.Navegador()
nav.custom_print('Consiguiendo ultima version')

url = "http://raw.githubusercontent.com/superegi/coronavirus_reportePeriodico/main/Scraping_epivigila/Funciones_Scraping.py"
resp = requests.get(url)
with open("Funciones_Scraping.py", "w", encoding="utf-8") as f:
     f.write(resp.text)


nav.custom_print(nav.TS())

up=pd.read_excel('User-Pass.xlsx')

nav.custom_print(nav.TS())

nav.user_passw(up['User:'][0],up['Pass:'][0])

nav.custom_print(nav.TS())

nav.abre_pag('https://epivigila.minsal.cl/index.php')

nav.custom_print(nav.TS())

nav.ingreso()

nav.custom_print('TIENE 15 SEG PARA RESOLVER EL CAPTCHA DE FORMA MANUAL EN CASO DE SER NECESARIO ****')

time.sleep(15)

nav.custom_print(nav.TS())

nav.click_seremi()

#Aca deberia estar el men� que haga elegir que info y cuanto

nav.custom_print('**** A CONTINUACION SE VAN A DESCARGAR 500 ENTRADAS PARA LOS SIGUIENTES DATOS ****\n')

nav.custom_print('**** NOTIF1 : lista de notificaciones en gestion de notificaciones ****')

nav.custom_print('**** NOTIF2 : muestras por notificar en gestion de notificaciones ****')

nav.custom_print('**** SEG : contactos covid en gestion de seguimiento ****\n')

nav.custom_print(nav.TS())

nav.descargar_info('NOTIF1',500)
nav.descargar_info('NOTIF2',500)
nav.descargar_info('SEG',500)

nav.custom_print(nav.TS())

nav.custom_print('**** FIN DEL PROGRAMA ****')

nav.custom_print(nav.TS())