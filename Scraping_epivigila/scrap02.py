# -*- coding: latin-1 -*-
import pandas as pd
from selenium import webdriver
import time

#Funcion que transforma el texto a una lista de listas y luego a un DF para casos por notificar

def aLista_por_notif(text):
    if "NO CONCLUYENTE" in text:
        tres_ult=text[len(text)-36:]
        tres_ult=tres_ult.split(' ')
        tres_ult=[tres_ult[0],tres_ult[1]," ".join(tres_ult[-2:])]
        X=text[:len(text)-36]
    else:
        tres_ult=text[len(text)-30:]
        tres_ult=tres_ult.split(' ')
        X=text[:len(text)-30]
    nums=['1','2','3','4','5','6','7','8','9','0']
    ind=100
    for i in nums:
        if X.find(i)>0:
            if X.find(i)<ind:
                ind=X.find(i)

    nombre=X[:ind]
    rut=X.replace(nombre,"").split(' ')[0]
    lab=" ".join(X.replace(nombre,"").split(' ')[1:])
    l=[nombre,rut,lab]
    L=l+tres_ult
    return L

def aTabla_por_notif(texto):
    lista=texto.split('\n')
    LLL=[]
    for i in lista[6:]:
        ll=aLista_por_notif(i)
        LLL.append(ll)
    DF=pd.DataFrame(LLL,columns=lista[:6])
    return DF

#Funcion que transforma el texto a una lista de listas y luego a un DF para Casos Confirmados

def aLista_caso(string):
    if 'En proceso de' in string:
        if 'Contactos' in string:
            lis=string.split(' ')
            prim2=lis[:2]
            ult2=lis[-2:]
            caso=" ".join(lis[2:3])
            inst=" ".join(lis[3:6])
            rut=lis[6]
            estado=" ".join(lis[-6:-2])
            nombre=" ".join(lis[7:-6])
            L=[prim2[0],prim2[1],caso,inst,rut,nombre,estado,ult2[0],ult2[1]]
            return L
        
        else:
            lis=string.split(' ')
            prim2=lis[:2]
            ult2=lis[-2:]
            caso=" ".join(lis[2:4])
            inst=" ".join(lis[4:7])
            rut=lis[7]
            estado=" ".join(lis[-6:-2])
            nombre=" ".join(lis[8:-6])
            L=[prim2[0],prim2[1],caso,inst,rut,nombre,estado,ult2[0],ult2[1]]
            return L
    
    elif 'sintomático' in string:
        if 'Contactos' in string:
            lis=string.split(' ')
            prim2=lis[:2]
            ult2=lis[-2:]
            caso=" ".join(lis[2:3])
            inst=" ".join(lis[3:6])
            rut=lis[6]
            estado=" ".join(lis[-4:-2])
            nombre=" ".join(lis[8:-4])
            L=[prim2[0],prim2[1],caso,inst,rut,nombre,estado,ult2[0],ult2[1]]
            return L

    elif 'no contactado' in string:
        if 'Contactos' in string:
            lis=string.split(' ')
            prim2=lis[:2]
            ult=lis[-1]
            caso=" ".join(lis[2:3])
            inst=" ".join(lis[3:6])
            rut=lis[6]
            estado=" ".join(lis[-4:-1])
            nombre=" ".join(lis[8:-4])
            L=[prim2[0],prim2[1],caso,inst,rut,nombre,estado,"",ult]
            return L
        else:
            lis=string.split(' ')
            prim2=lis[:2]
            ult=lis[-1]
            caso=" ".join(lis[2:4])
            inst=" ".join(lis[4:7])
            rut=lis[7]
            estado=" ".join(lis[-4:-1])
            nombre=" ".join(lis[8:-4])
            L=[prim2[0],prim2[1],caso,inst,rut,nombre,estado,"",ult]
            return L
    
    elif 'Contactos' in string:
        lis=string.split(' ')
        prim2=lis[:2]
        ult=lis[-1]
        caso=" ".join(lis[2:3])
        inst=" ".join(lis[3:6])
        rut=lis[6]
        estado=" ".join(lis[-4:-1])
        nombre=" ".join(lis[7:-4])
        L=[prim2[0],prim2[1],caso,inst,rut,nombre,estado,"",ult]
        return L

    
    elif 'localizado' in string:
            lis=string.split(' ')
            prim2=lis[:2]
            ult2=lis[-2:]
            caso=" ".join(lis[2:4])
            inst=" ".join(lis[4:7])
            rut=lis[7]
            estado=" ".join(lis[-4:-2])
            nombre=" ".join(lis[8:-4])
            L=[prim2[0],prim2[1],caso,inst,rut,nombre,estado,ult2[0],ult2[1]]
            return L
    
    else:
        lis=string.split(' ')
        prim2=lis[:2]
        ult2=lis[-2:]
        caso=" ".join(lis[2:4])
        inst=" ".join(lis[4:7])
        rut=lis[7]
        estado=" ".join(lis[-4:-2])
        nombre=" ".join(lis[8:-4])
        L=[prim2[0],prim2[1],caso,inst,rut,nombre,estado,ult2[0],ult2[1]]
        return L
        

def aTabla_caso(texto):
    lista=texto.split('\n')
    LLL=[]
    for i in lista[18:]:
        ll=aLista_caso(i)
        LLL.append(ll)
    DF=pd.DataFrame(LLL,columns=['Folio','Fecha de Ingreso','Tipo de Seguimiento','Nombre Institución','Identificación','Nombre','Estado','Fecha último contacto','Seguimientos Realizados'])
    print('df listoko')
    return DF

print('**** SE PROCEDE A IMPORTAR USER Y CLAVE ****')
#Usuario y Clave
up=pd.read_excel('User-Pass.xlsx')

user  = str(up['User:'][0])
passw = str(up['Pass:'][0])

print('**** SE PROCEDE A ABRIR EL NAVEGADOR E INGRSAR USER Y CLAVE ****')
driver = webdriver.Chrome()
driver.get('https://epivigila.minsal.cl/index.php')
time.sleep(2)

#Ingresar Usuario
user_Box = driver.find_element_by_xpath('//*[@id="rutL"]')
user_Box.send_keys(user)
time.sleep(2)
pass_Box = driver.find_element_by_xpath('//*[@id="password_login"]')
pass_Box.send_keys(passw)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="form_login"]/div[5]/div/input').click()
time.sleep(2)

print('FAVOR DE RESOLVER EL CAPTCHA DE FORMA MANUAL EN CASO DE SER NECESARIO ****')
#Resolver Captcha
time.sleep(15)

print('**** SE PROCEDE A DAR CLICK EN "SEREMI" ****')
driver.find_element_by_xpath('//*[@id="formularioSeleccionarRol"]/div[2]/label').click()
time.sleep(3)

print('**** SE PROCEDE A ABRIR EL ACORDEON DE GESTION DE NOTIFICACIONES Y DAR CLICK EN MUESTRAS POR NOTIFICAR **** ')
#Abrir Acordeón Gestion de Notif
driver.find_element_by_xpath('//*[@id="accordion"]/div[2]/div[1]').click()
time.sleep(3)

#Click lista de muestras por notificar
driver.find_element_by_xpath('//*[@id="usuarioPanel"]/div/ul/li[2]/a').click()
time.sleep(3)

print('**** SE DA CLICK PARA QUE MUESTRE LAS 100 ENTRADAS Y LUEGO SE GUARDA LA INFO')
#Seleccionar 100 primeras Opciones
driver.find_element_by_xpath('//*[@id="tabla_boletin_eno_nuevas_length"]/label/select/option[4]').click()
time.sleep(3)

#Muestra la tabla en texto a descargar
texto=driver.find_element_by_xpath('//*[@id="tabla_boletin_eno_nuevas"]').text

print('**** SE DA CLICK EN "SIGUIENTE" Y SE GUARDAN LAS 100 NUEVAS ENTRADAS ****')
#Dar Click en Siguiente
driver.find_element_by_xpath('//*[@id="tabla_boletin_eno_nuevas_next"]').click()
time.sleep(3)

#Muestra la tabla en texto a descargar
texto2=driver.find_element_by_xpath('//*[@id="tabla_boletin_eno_nuevas"]').text

print("Elementos guardados en variables!")

print('**** SE PROCEDE A GUARDAR LA INFORMACION DE LOS CASOS POR NOTIFICAR ****')
por_notif_100=aTabla_por_notif(texto)
por_notif_200=aTabla_por_notif(texto2)
por_notif_final=por_notif_100.append(por_notif_200, ignore_index =True)
por_notif_final.to_excel('Listado por Notificar.xlsx')
print('**-------LISTOOOOO--------**!!')

print('**** SE DA CLICK EN EL ACORDEON DE GESTION DE NOTIFICACIONES Y LUEGO CLICK EN LA LISTA DE CONTACTOS ****')
#Dar Click en Gestion de Seguimiento
driver.find_element_by_xpath('//*[@id="accordion"]/div[3]/div[1]/h5/a').click()
time.sleep(7)

#Dar Click en Lista de Contactos
driver.find_element_by_xpath('//*[@id="contactosPanel"]/div/li/a').click()

print('**** SE DA CLICK PARA QUE MUESTRE LAS 100 ENTRADAS Y LUEGO SE GUARDA LA INFO')
#Seleccionar 100 primeras Opciones
driver.find_element_by_xpath('//*[@id="tabla_boletin_eno_nuevas_length"]/label/select/option[4]').click()
time.sleep(3)

#Muestra la tabla en texto a descargar
texto3=driver.find_element_by_xpath('//*[@id="tabla_boletin_eno_nuevas"]').text

print('**** SE DA CLICK EN "SIGUIENTE" Y SE GUARDAN LAS 100 NUEVAS ENTRADAS ****')
# #Dar Click en Siguiente
driver.find_element_by_xpath('//*[@id="tabla_boletin_eno_nuevas_next"]').click()
time.sleep(3)

#Muestra la tabla en texto a descargar
texto4=driver.find_element_by_xpath('//*[@id="tabla_boletin_eno_nuevas"]').text

print('**** SE PROCEDE A GUARDAR LA INFORMACION DE LOS CASOS CONFIRMADOS ****')
caso_100=aTabla_caso(texto3)
caso_200=aTabla_caso(texto4)
caso_final=caso_100.append(caso_200, ignore_index =True)
caso_final.to_excel('Listado Caso Activos.xlsx')
print('**-------LISTOOOOO--------**!!')
