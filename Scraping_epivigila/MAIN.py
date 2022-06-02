# -*- coding: latin-1 -*-

#import requests
import Funciones_Scraping as FS
import pandas as pd
import time
import math

nav=FS.Navegador()
nav.custom_print('****INICIANDO PROGRAMA DE DESCARGA BDs EPIVIGILIA ****')

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

#Aca deberia estar el menú que haga elegir que info y cuanto

nav.custom_print('**** A CONTINUACION SE VAN A DESCARGAR LOS SIGUIENTES DATOS ****\n')

nav.custom_print('**** NOTIF1 : lista de notificaciones en gestion de notificaciones ****')

nav.custom_print('**** NOTIF2 : muestras por notificar en gestion de notificaciones ****')

nav.custom_print('**** SEG : contactos covid en gestion de seguimiento ****\n')

nav.custom_print(nav.TS())

nav.custom_print('**** A CONTINUACION SE SOLICITARA LA CANTIDAD DE ENTRADAS DE DATOS A DESCARGAR ****')

casos=float(input('Ingrese la cantidad de casos a descargar: '))
casos_fix=int(math.ceil(casos/100)*100)

nav.custom_print(f'**** SE HAN INGRESADO {casos} CASOS ****')
nav.custom_print(f'**** SE PROCEDE A DESCARGAR {casos_fix} CASOS ****\n')

nav.descargar_info('SEG',casos)
nav.custom_print(nav.TS())

nav.descargar_info('NOTIF2',casos)
nav.custom_print(nav.TS())

nav.descargar_info('NOTIF1',casos)
nav.custom_print(nav.TS())

nav.resumen()

nav.custom_print('**** FIN DEL PROGRAMA ****')

nav.custom_print(nav.TS())