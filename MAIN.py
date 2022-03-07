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

nav.custom_print('**** A CONTINUACION INGRESE TIPO  Y CANTIDAD DE DATOS A DESCARGAR ****\n')

nav.custom_print('**** PARA TIPO DE DATO INGRESE: ****')

nav.custom_print('**** NOTIF1 : para accdeder a la lista de notificaciones en gestion de notificaciones ****')

nav.custom_print('**** NOTIF2 : para accdeder a muestras por notificar en gestion de notificaciones ****')

nav.custom_print('**** SEG : para accdeder a contactos covid en gestion de seguimiento ****')

nav.custom_print('**** BAC : para accdeder a listar en gestion de BAC COVID19 ****\n')



nav.custom_print('**** PARA CANTIDAD DE DATO INGRESE UN NUMERO DE LAS SIGUIENTES OPCIONES: ****')

nav.custom_print('**** 100 - 200 - 300 - 400 - 500 ****\n')

nav.custom_print(nav.TS())



nav.descargar_info()

nav.custom_print(nav.TS())



nav.custom_print('**** FIN DEL PROGRAMA ****')

nav.custom_print(nav.TS())