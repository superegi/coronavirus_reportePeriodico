# -*- coding: latin-1 -*-















import datetime as dt







from selenium.webdriver.common.by import By







import pandas as pd







from selenium import webdriver







import time















class Navegador:







    def __init__(self):







        print('**Inicio Modulo Navegador**\n')







        self.TS_inicial=dt.datetime.now()







        self.user  = ""







        self.passw = ""







        self.driver = webdriver.Chrome()







        self.Tabla=pd.DataFrame()















#Funcion para transformar el texto de lista por notificar en tabla    







    def aTabla_por_notif(self,texto): 







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







            







        lista=texto.split('\n')







        LLL=[]







        for i in lista[6:]:







            ll=aLista_por_notif(i)







            LLL.append(ll)







        DF=pd.DataFrame(LLL,columns=lista[:6])







        return DF















#Funcion que transforma el texto a un DF para Casos Confirmados







    def aTabla_caso(self,texto):







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







            







            elif 'sintom�tico' in string:







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







                















        lista=texto.split('\n')







        LLL=[]







        for i in lista[18:]:







            ll=aLista_caso(i)







            LLL.append(ll)







        DF=pd.DataFrame(LLL,columns=['Folio','Fecha de Ingreso','Tipo de Seguimiento','Nombre Institucion','Identificacion','Nombre','Estado','Fecha ultimo contacto','Seguimientos Realizados'])







        return DF







    







    def TS(self):







       	t = dt.datetime.now().strftime('%m/%d %H:%M:%S')







       	evol = str((dt.datetime.now() - self.TS_inicial).seconds)







       	return str(t + '| [' + evol + 's]:')

       

    def custom_print(self,message_to_print, log_file='LOG.txt'):

        print(message_to_print)

        with open(log_file, 'a') as of:

            of.write('\n' + message_to_print)







        







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







        self.custom_print('**** SE PROCEDE A DAR CLICK EN "SEREMI" ****\n')







        self.driver.find_element_by_xpath('//*[@id="formularioSeleccionarRol"]/div[2]/label').click()







        time.sleep(3)







        self.custom_print('**** LISTO ****\n')







    







    def gestion_notif(self,opcion=None):







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







    







    def gestion_seg(self):







        self.custom_print('**** SE PROCEDE A ABRIR EL ACORDEON DE GESTION DE SEGUIMIENTO **** ')







        self.driver.find_element(By.XPATH,'//*[@id="accordion"]/div[3]/div[1]/h5/a').click()







        time.sleep(2)







        self.custom_print('**** SE CLICKEA EN LISTA DE CONTACTOS PACIENTES COVID-19 **** ')







        self.driver.find_element(By.XPATH,'//*[@id="contactosPanel"]/div/li/a').click()







        self.custom_print('**** LISTO ****\n')







    







    def gestion_bac(self):







        self.custom_print('**** SE PROCEDE A ABRIR EL ACORDEON DE GESTION DE BAC COVID-19 **** ')







        self.driver.find_element(By.XPATH,'//*[@id="accordion"]/div[5]/div[1]/h5/a').click()







        time.sleep(2)







        self.custom_print('**** SE CLICKEA EN LISTAR **** ')







        self.driver.find_element(By.XPATH,'//*[@id="analisis"]/div/ul/li/a').click()







        self.custom_print('**** LISTO ****\n')







        







        







    def registros(self,opc=None):







        self.custom_print('**** SE CLICKEA EN LA CANTIDAD DE REGISTROS **** ')







        if opc==10:







            self.custom_print('**** 10 REGISTROS ****')







            self.driver.find_element(By.XPATH,'//*[@id="tabla_boletin_eno_nuevas_length"]/label/select/option[1]').click()







            time.sleep(3)







            self.custom_print('**** LISTO ****\n')







            







        elif opc==25:







            self.custom_print('**** 25 REGISTROS ****')







            self.driver.find_element(By.XPATH,'//*[@id="tabla_boletin_eno_nuevas_length"]/label/select/option[2]').click()







            time.sleep(3)







            self.custom_print('**** LISTO ****\n')







            







        elif opc==50:







            self.custom_print('**** 50 REGISTROS ****')







            self.driver.find_element(By.XPATH,'//*[@id="tabla_boletin_eno_nuevas_length"]/label/select/option[3]').click()







            time.sleep(3)







            self.custom_print('**** LISTO ****\n')







            







        elif opc==100:







            self.custom_print('**** 100 REGISTROS ****')







            self.driver.find_element(By.XPATH,'//*[@id="tabla_boletin_eno_nuevas_length"]/label/select/option[4]').click()







            time.sleep(3)







            self.custom_print('**** LISTO ****\n')







    







    def siguiente(self):







        self.custom_print('**** SE DA CLICK EN BOTON "SIGUIENTE" AL FINAL DE LA PAGINA ****')







        self.driver.find_element(By.XPATH,'//*[@id="tabla_boletin_eno_nuevas_next"]').click()







        time.sleep(3)







        self.custom_print('**** LISTO ****\n')







    







    def descargar_info(self):







        dato=str(input("Ingrese tipo de dato: "))







        cant=int(input('Ingrese cantidad de datos: '))







        self.custom_print('')







        if dato=='NOTIF2':







            self.custom_print('**** HA SELECCIONADO LISTA DE MUESTRAS POR NOTIFICAR ****')







            self.gestion_notif(2)







            self.registros(100)







            for i in range(0,int(cant/100)):







                texto=self.driver.find_element(By.XPATH,'//*[@id="tabla_boletin_eno_nuevas"]').text







                df=self.aTabla_por_notif(texto)







                self.Tabla=pd.concat([self.Tabla,df],ignore_index =True)







                self.siguiente()







            self.custom_print('**** SE HA CREADO LA TABLA CON: ',self.Tabla.shape[0],' ENTRADAS ****')







            self.Tabla.head()







            self.custom_print('')







            self.Tabla.to_excel('LISTADO MUESTRAS POR NOTIFICAR.xlsx')







            self.custom_print('**** SE HA GUARDADO EL ARCHIVO "LISTADO MUESTRAS POR NOTIFICAR" EXITOSAMENTE ****\n')







            self.Tabla=pd.DataFrame()







        







        elif dato=='SEG':







            self.custom_print('**** HA SELECCIONADO LISTA DE CONTACTOS DE GESTION DE SEGUIMIENTO ****')







            self.gestion_seg()







            self.registros(100)







            for i in range(0,int(cant/100)):







                texto=self.driver.find_element(By.XPATH,'//*[@id="tabla_boletin_eno_nuevas"]').text







                df=self.aTabla_caso(texto)







                self.Tabla=pd.concat([self.Tabla,df],ignore_index =True)







                self.siguiente()







            self.custom_print('**** SE HA CREADO LA TABLA CON: ',self.Tabla.shape[0],' ENTRADAS ****')







            self.Tabla.head()







            self.custom_print('')







            self.Tabla.to_excel('LISTADO CONTACTOS PACIENTES COVID19.xlsx')







            self.custom_print('**** SE HA GUARDADO EL ARCHIVO "LISTADO CONTACTOS PACIENTES COVID19" EXITOSAMENTE ****\n')







            self.Tabla=pd.DataFrame()







        







        #Hacer funci�n pa las notif1







        elif dato=='NOTIF1':







            self.custom_print('**** HA SELECCIONADO LISTA DE NOTIFICACIONES ****')







            self.gestion_notif(1)







            self.registros(100)







            self.custom_print('**** Funcion en proceso... ****')







        







        #Hacer funcion de tablas para BAC







        elif dato=='BAC':







            self.custom_print('**** HA SELECCIONADO LISTA DE GESTION DE BAC ****')







            self.gestion_notif(2)







            self.custom_print('**** Funcion en proceso.... ****')







                







                







                







            







        















        