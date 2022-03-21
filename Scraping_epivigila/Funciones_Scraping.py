# -*- coding: latin-1 -*-
import datetime as dt
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium import webdriver
import time
import sys
from datetime import datetime

class Navegador:
    def __init__(self):
        print('**Inicio Modulo Navegador**\n')
        self.TS_inicial=dt.datetime.now()
        self.user  = ""
        self.passw = ""
        self.driver = webdriver.Chrome()
        self.Tabla=pd.DataFrame()
        self.hoy=datetime.today().strftime('%d-%m-%Y').replace('-',"")
    
    def TS(self):
       	t = dt.datetime.now().strftime('%m/%d %H:%M:%S')
       	evol = str((dt.datetime.now() - self.TS_inicial).seconds)
       	return str(t + '| [' + evol + 's]:')

    def custom_print(self,message_to_print, log_file='LOG_'+datetime.today().strftime('%d-%m-%Y').replace('-',"")+'.txt'):
        print(message_to_print)
        with open(log_file, 'a') as of:
            of.write('\n' + message_to_print)
  
    #Funcion que extrae tabla de notif1.
    def notif1_tabla(self):
        folios = self.driver.find_elements(By.XPATH,'//tbody/tr/td[1]')
        ids    = self.driver.find_elements(By.XPATH,'//tbody/tr/td[2]')
        names  = self.driver.find_elements(By.XPATH,'//tbody/tr/td[3]')
        enfer  = self.driver.find_elements(By.XPATH,'//tbody/tr/td[4]')
        fecha  = self.driver.find_elements(By.XPATH,'//tbody/tr/td[5]')
        etapa  = self.driver.find_elements(By.XPATH,'//tbody/tr/td[6]')
        estado = self.driver.find_elements(By.XPATH,'//tbody/tr/td[7]')
        nomnot = self.driver.find_elements(By.XPATH,'//tbody/tr/td[8]')
        estab  = self.driver.find_elements(By.XPATH,'//tbody/tr/td[11]')
        
        entradas=[]
        
        if self.driver.find_element(By.XPATH,'//tbody/tr/td[1]') == 'No se encontraron resultados':
            self.custom_print('**** No se encontraron más resultados ****\n')
            return pd.DataFrame()
            
        for i in range(len(folios)):
            data={'Folio': folios[i].text,
                 'Identificación paciente': ids[i].text,
                 'Nombre completo': names[i].text,
                 'Enfermedad': enfer[i].text,
                 'Fecha notificación': fecha[i].text,
                 'Etapa clínica': etapa[i].text,
                 'Estado validación': estado[i].text,
                 'Nombre notificador': nomnot[i].text,
                 'Establecimiento': estab[i].text}
            entradas.append(data)
        df_data=pd.DataFrame(entradas)
        return df_data
    
    #Funcion que extrae tabla de notif2.
    def notif2_tabla(self):
        name        = self.driver.find_elements(By.XPATH,'//tbody/tr/td[1]')
        ids         = self.driver.find_elements(By.XPATH,'//tbody/tr/td[2]')
        lab         = self.driver.find_elements(By.XPATH,'//tbody/tr/td[3]')
        fecha_toma  = self.driver.find_elements(By.XPATH,'//tbody/tr/td[4]')
        fecha_resul = self.driver.find_elements(By.XPATH,'//tbody/tr/td[5]')
        resul       = self.driver.find_elements(By.XPATH,'//tbody/tr/td[6]')
    
        entradas=[]
        
        if self.driver.find_element(By.XPATH,'//tbody/tr/td[1]') == 'No se encontraron resultados':
            self.custom_print('**** No se encontraron más resultados ****\n')
            return pd.DataFrame()
        
        for i in range(len(name)):
            data={'Nombre paciente': name[i].text,
                 'Número identificación': ids[i].text,
                 'laboratorio': lab[i].text,
                 'Fecha toma muestra': fecha_toma[i].text,
                 'Fecha resultados': fecha_resul[i].text,
                 'Resultado': resul[i].text}
            entradas.append(data)
        df_data=pd.DataFrame(entradas)
        return df_data
    
    #Funcion que extrae tabla de seg.
    def seg_tabla(self):
        folio     = self.driver.find_elements(By.XPATH,'//tbody/tr/td[1]')
        fecha_ing = self.driver.find_elements(By.XPATH,'//tbody/tr/td[2]')
        tipo      = self.driver.find_elements(By.XPATH,'//tbody/tr/td[3]')
        inst      = self.driver.find_elements(By.XPATH,'//tbody/tr/td[4]')
        ids       = self.driver.find_elements(By.XPATH,'//tbody/tr/td[5]')
        name      = self.driver.find_elements(By.XPATH,'//tbody/tr/td[6]')
        est       = self.driver.find_elements(By.XPATH,'//tbody/tr/td[7]')
        fecha_ult = self.driver.find_elements(By.XPATH,'//tbody/tr/td[8]')
        segs      = self.driver.find_elements(By.XPATH,'//tbody/tr/td[9]')
    
        entradas=[]
        
        if self.driver.find_element(By.XPATH,'//tbody/tr/td[1]') == 'No se encontraron resultados':
            self.custom_print('**** No se encontraron más resultados ****\n')
            return pd.DataFrame()
        
        for i in range(len(name)):
            data={'Folio': folio[i].text,
                 'Fecha de ingreso': fecha_ing[i].text,
                 'Tipo de seguimiento': tipo[i].text,
                 'Nombre institución': inst[i].text,
                 'Identificación': ids[i].text,
                 'Nombre': name[i].text,
                 'Estado': est[i].text,
                 'Fecha último contacto': fecha_ult[i].text,
                 'Seguimientos realizados': segs[i].text}
            entradas.append(data)
        df_data=pd.DataFrame(entradas)
        return df_data
    
    def bac_tabla(self):
        folio = self.driver.find_elements(By.XPATH,'//tbody/tr/td[1]')
        ids   = self.driver.find_elements(By.XPATH,'//tbody/tr/td[2]')
        name  = self.driver.find_elements(By.XPATH,'//tbody/tr/td[3]')
        Fecha = self.driver.find_elements(By.XPATH,'//tbody/tr/td[4]')
        reg   = self.driver.find_elements(By.XPATH,'//tbody/tr/td[5]')
        
        entradas=[]
        
        if self.driver.find_element(By.XPATH,'//tbody/tr/td[1]') == 'No se encontraron resultados':
            self.custom_print('**** No se encontraron más resultados ****\n')
            return pd.DataFrame()
        
        for i in range(len(name)):
            data={'Folio BAC': folio[i].text,
                 'Número de identificación': ids[i].text,
                 'Nombre completo': name[i].text,
                 'Fecha toma muestra': Fecha[i].text,
                 'Región BAC': reg[i].text}
            entradas.append(data)
        df_data=pd.DataFrame(entradas)
        return df_data

    def user_passw(self,us,pa):
        self.custom_print('**** SE PROCEDE A IMPORTAR USUARIO Y CLAVE ****\n')
        self.user  = str(us)
        self.passw = str(pa)
        self.custom_print('**** LISTO ****\n')

    def abre_pag(self,url):
        self.custom_print('**** SE PROCEDE A ABRIR EL NAVEGADOR ****\n')
        self.driver.get(url)
        time.sleep(2)
        self.custom_print('**** LISTO ****\n')

    def ingreso(self):
        self.custom_print('**** SE PROCEDE A INGRESAR USUARIO Y CLAVE ****\n')
        user_Box = self.driver.find_element(By.XPATH,'//*[@id="rutL"]')
        user_Box.send_keys(self.user)
        time.sleep(2)
        pass_Box = self.driver.find_element(By.XPATH,'//*[@id="password_login"]')
        pass_Box.send_keys(self.passw)
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="form_login"]/div[5]/div/input').click()
        time.sleep(2)
        self.custom_print('**** LISTO ****\n')

    def click_seremi(self):
        try:
            self.custom_print('**** SE PROCEDE A DAR CLICK EN "SEREMI" ****\n')
            self.driver.find_element_by_xpath('//*[@id="formularioSeleccionarRol"]/div[2]/label').click()
            time.sleep(3)
            self.custom_print('**** LISTO ****\n') 
        except NoSuchElementException:
            self.custom_print('**** ERROR ERROR ERROR! No se resolvió el captcha en el tiempo necesario ****')
            self.custom_print(f'**** El error fue: {str(NoSuchElementException)} ****\n')

    def gestion_notif(self,opcion=None):
        try:
            self.custom_print('**** SE PROCEDE A ABRIR EL ACORDEON DE GESTION DE NOTIFICACIONES **** ')
            self.driver.find_element(By.XPATH,'//*[@id="accordion"]/div[2]/div[1]').click()
            time.sleep(3)
            if opcion==1:
                self.custom_print('**** SE CLICKEA EN LISTA NOTIFICACIONES **** ')
                self.driver.find_element(By.XPATH,'//*[@id="usuarioPanel"]/div/ul/li[1]/a').click()
                time.sleep(3)
                self.custom_print('**** LISTO ****\n')
            elif opcion == 2:
                self.custom_print('**** SE CLICKEA EN LISTA DE MUESTRAS POR NOTIFICAR **** ')
                self.driver.find_element(By.XPATH,'//*[@id="usuarioPanel"]/div/ul/li[2]/a').click()
                time.sleep(3)
                self.custom_print('**** LISTO ****\n')
        except NoSuchElementException:
            self.custom_print('**** ERROR ERROR ERROR! No se abrió el acordeón de gestion de notificaciones  ****')
            self.custom_print(f'**** El error fue: {str(NoSuchElementException)} ****\n')
            

    def gestion_seg(self):
        try:
            self.custom_print('**** SE PROCEDE A ABRIR EL ACORDEON DE GESTION DE SEGUIMIENTO **** ')
            self.driver.find_element(By.XPATH,'//*[@id="accordion"]/div[3]/div[1]/h5/a').click()
            time.sleep(2)
            self.custom_print('**** SE CLICKEA EN LISTA DE CONTACTOS PACIENTES COVID-19 **** ')
            self.driver.find_element(By.XPATH,'//*[@id="contactosPanel"]/div/li/a').click()
            self.custom_print('**** LISTO ****\n')
        except NoSuchElementException:
            self.custom_print('**** ERROR ERROR ERROR! No se abrió el acordeón de gestion de seguimiento  ****')
            self.custom_print(f'**** El error fue: {str(NoSuchElementException)} ****\n')

    def gestion_bac(self):
        try:
            self.custom_print('**** SE PROCEDE A ABRIR EL ACORDEON DE GESTION DE BAC COVID-19 **** ')
            self.driver.find_element(By.XPATH,'//*[@id="accordion"]/div[5]/div[1]/h5/a').click()
            time.sleep(4)
            self.custom_print('**** SE CLICKEA EN LISTAR **** ')
            self.driver.find_element(By.XPATH,'//*[@id="analisis"]/div/ul/li/a').click()
            self.custom_print('**** LISTO ****\n')
            time.sleep(2)
        except NoSuchElementException:
            self.custom_print('**** ERROR ERROR ERROR! No se abrió el acordeón de gestion de BAC  ****')
            self.custom_print(f'**** El error fue: {str(NoSuchElementException)} ****\n')

    def registros(self,opc=None):
        self.custom_print('**** SE CLICKEA EN LA CANTIDAD DE REGISTROS **** ')
        if opc==10:
            self.custom_print('**** 10 REGISTROS ****')
            self.driver.find_element(By.XPATH,'//label/select/option[1]').click()
            time.sleep(3)
            self.custom_print('**** LISTO ****\n')
        elif opc==25:
            self.custom_print('**** 25 REGISTROS ****')
            self.driver.find_element(By.XPATH,'//label/select/option[2]').click()
            time.sleep(3)
            self.custom_print('**** LISTO ****\n')
        elif opc==50:
            self.custom_print('**** 50 REGISTROS ****')
            self.driver.find_element(By.XPATH,'//label/select/option[3]').click()
            time.sleep(3)
            self.custom_print('**** LISTO ****\n')
        elif opc==100:
            self.custom_print('**** 100 REGISTROS ****')
            self.driver.find_element(By.XPATH,'//label/select/option[4]').click()
            time.sleep(3)
            self.custom_print('**** LISTO ****\n')

    def siguiente(self):
        try:
            self.custom_print('**** SE DA CLICK EN BOTON "SIGUIENTE" AL FINAL DE LA PAGINA ****')
            self.driver.find_element(By.XPATH,'//*[@id="tabla_boletin_eno_nuevas_next"]').click()
            time.sleep(3)
            self.custom_print('**** LISTO ****\n')
        except NoSuchElementException:
            self.custom_print('**** ERROR ERROR ERROR! No se dió click en siguiente  ****')
            self.custom_print(f'**** El error fue: {str(NoSuchElementException)} ****\n')
    
    def siguiente_bac(self):
        try:
            self.custom_print('**** SE DA CLICK EN BOTON "SIGUIENTE" AL FINAL DE LA PAGINA ****')
            self.driver.find_element(By.XPATH,'//*[@id="tabla_formularios_bac_next"]').click()
            time.sleep(3)
            self.custom_print('**** LISTO ****\n')
        except NoSuchElementException:
            self.custom_print('**** ERROR ERROR ERROR! No se dió click en siguiente  ****')
            self.custom_print(f'**** El error fue: {str(NoSuchElementException)} ****\n')
    
    def siguiente_inmediata(self):
        try:
            self.custom_print('**** SE DA CLICK EN BOTON "SIGUIENTE" AL FINAL DE LA PAGINA ****')
            self.driver.find_element(By.XPATH,'//*[@id="tabla_boletin_eno_inmediatas_next"]').click()
            time.sleep(3)
            self.custom_print('**** LISTO ****\n')
        except NoSuchElementException:
            self.custom_print('**** ERROR ERROR ERROR! No se dió click en siguiente  ****')
            self.custom_print(f'**** El error fue: {str(NoSuchElementException)} ****\n')

    def descargar_info(self,dat=None,can=None):
        if dat:
            dato=dat
            cant=can
        else:
            dato=str(input("Ingrese tipo de dato: "))
            cant=int(input('Ingrese cantidad de datos: '))
            self.custom_print('')
        
        if dato=='NOTIF2':
            self.custom_print('**** HA SELECCIONADO LISTA DE MUESTRAS POR NOTIFICAR ****')
            self.gestion_notif(2)
            self.registros(100)
            for i in range(0,int(cant/100)):
                try:
                    time.sleep(1)
                    self.Tabla=pd.concat([self.Tabla,self.notif2_tabla()],ignore_index =True)
                    self.siguiente()
                except IndexError:
                    self.custom_print('**** ERROR ERROR ERROR! No se abrió el acordeón de gestion de BAC  ****')
                    self.custom_print(f'**** El error fue: {sys.exc_info()[0]} ****')      
            tt=str(f'**** SE HA CREADO LA TABLA CON: {self.Tabla.shape[0]} ENTRADAS ****\n')
            self.r11=str(f'**** CON: {self.Tabla.shape[0]} ENTRADAS ****')
            self.custom_print(tt)
            self.Tabla.head()
            self.custom_print('')
            name=self.TS()[:5]+'/2022'
            name=name.replace('/','')
            self.Tabla.to_excel('LISTADO MUESTRAS POR NOTIFICAR '+name+'.xlsx')
            self.r12=f'**** SE HA GUARDADO EL ARCHIVO "LISTADO MUESTRAS POR NOTIFICAR {name}" EXITOSAMENTE ****'
            self.custom_print(f'**** SE HA GUARDADO EL ARCHIVO "LISTADO MUESTRAS POR NOTIFICAR {name}" EXITOSAMENTE ****\n')
            self.Tabla=pd.DataFrame()

        elif dato=='SEG':
            self.custom_print('**** HA SELECCIONADO LISTA DE CONTACTOS DE GESTION DE SEGUIMIENTO ****')
            self.gestion_seg()
            self.registros(100)
            for i in range(0,int(cant/100)):
                try:
                    time.sleep(5)
                    self.Tabla=pd.concat([self.Tabla,self.seg_tabla()],ignore_index =True)
                    self.siguiente()
                except IndexError:
                    self.custom_print('**** ERROR ERROR ERROR! No se abrió el acordeón de gestion de BAC  ****')
                    self.custom_print(f'**** El error fue: {sys.exc_info()[0]} ****\n')
            tt=str(f'**** SE HA CREADO LA TABLA CON: {self.Tabla.shape[0]} ENTRADAS ****')
            self.r21=str(f'**** CON: {self.Tabla.shape[0]} ENTRADAS ****')
            self.custom_print(tt)
            self.Tabla.head()
            self.custom_print('')
            name=self.TS()[:5]+'/2022'
            name=name.replace('/','')
            self.Tabla.to_excel('LISTADO CONTACTOS PACIENTES COVID19 '+name+'.xlsx')
            self.r22=f'**** SE HA GUARDADO EL ARCHIVO "LISTADO CONTACTOS PACIENTES COVID19 {name}" EXITOSAMENTE ****'
            self.custom_print(f'**** SE HA GUARDADO EL ARCHIVO "LISTADO CONTACTOS PACIENTES COVID19 {name}" EXITOSAMENTE ****\n')
            self.Tabla=pd.DataFrame()

        elif dato=='NOTIF1':
            self.custom_print('**** HA SELECCIONADO LISTA DE NOTIFICACIONES ****')
            self.gestion_notif(1)
            self.registros(100)
            for i in range(0,int(cant/100)):
                try:
                    time.sleep(1)
                    self.Tabla=pd.concat([self.Tabla,self.notif1_tabla()],ignore_index =True)
                    self.siguiente_inmediata()
                except IndexError:
                    self.custom_print('**** ERROR ERROR ERROR! No se abrió el acordeón de gestion de BAC  ****')
                    self.custom_print(f'**** El error fue: {sys.exc_info()[0]} ****')
            tt=str(f'**** SE HA CREADO LA TABLA CON: {self.Tabla.shape[0]} ENTRADAS ****\n')
            self.r31=str(f'**** CON: {self.Tabla.shape[0]} ENTRADAS ****')
            self.custom_print(tt)
            self.custom_print('')
            name=self.TS()[:5]+'/2022'
            name=name.replace('/','')
            self.Tabla.to_excel('LISTADO DE NOTIFICACIONES '+name+'.xlsx')
            self.r32=f'**** SE HA GUARDADO EL ARCHIVO "LISTADO DE NOTIFICACIONES {name}" EXITOSAMENTE ****'
            self.custom_print(f'**** SE HA GUARDADO EL ARCHIVO "LISTADO DE NOTIFICACIONES {name}" EXITOSAMENTE ****\n')
            self.Tabla=pd.DataFrame()

        elif dato=='BAC':
            self.custom_print('**** HA SELECCIONADO LISTA DE GESTION DE BAC ****')
            self.gestion_bac()
            self.registros(100)
            for i in range(0,int(cant/100)):
                try:
                    time.sleep(1)
                    self.Tabla=pd.concat([self.Tabla,self.notif1_tabla()],ignore_index =True)
                    self.siguiente_bac()
                except IndexError:
                    self.custom_print('**** ERROR ERROR ERROR! No se abrió el acordeón de gestion de BAC  ****')
                    self.custom_print(f'**** El error fue: {sys.exc_info()[0]} ****\n')
            tt=str(f'**** SE HA CREADO LA TABLA CON: {self.Tabla.shape[0]} ENTRADAS ****')
            self.r41=str(f'**** CON: {self.Tabla.shape[0]} ENTRADAS ****')
            self.custom_print(tt)
            self.custom_print('')
            name=self.TS()[:5]+'/2022'
            name=name.replace('/','')
            self.Tabla.to_excel('LISTADO DE GESTION DE BAC '+name+'.xlsx')
            self.r42=f'**** SE HA GUARDADO EL ARCHIVO "LISTADO DE GESTION DE BAC {name}" EXITOSAMENTE ****'
            self.custom_print(f'**** SE HA GUARDADO EL ARCHIVO "LISTADO DE GESTION DE BAC {name}" EXITOSAMENTE ****\n')
            self.Tabla=pd.DataFrame()
    
    def resumen(self):
        self.custom_print('**** EL RESUMEN DE LA EJECUCIÓN DEL PROGRAMA FUE: ****\n')
        self.custom_print(self.r12)
        self.custom_print(self.r11)
        self.custom_print('\n')
        self.custom_print(self.r22)
        self.custom_print(self.r21)
        self.custom_print('\n')
        self.custom_print(self.r32)
        self.custom_print(self.r31)
        self.custom_print('\n')
        #self.custom_print(self.r41)
        #self.custom_print(self.r42)
        
        





        