# -*- coding: latin-1 -*-
import pandas as pd

primera  = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_1eraDosis.csv")
segunda  = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_2daDosis.csv")
refuerzo = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_Refuerzo.csv")
cuarta   = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_4taDosis.csv")
unica   = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_UnicaDosis.csv")

def indicador(df):
    DF=pd.DataFrame()
    prim=df.loc[df['Region']=='Valparaiso']
    l_comunas=prim.Comuna
    prim=prim.T
    prim.columns=l_comunas
    prim['Fecha']=prim.index
    l_poblacion=prim[4:5]
    prim=prim[5:]
    prim.Fecha=pd.to_datetime(prim.Fecha)
    suma_atras=prim.groupby([pd.Grouper(key='Fecha', freq='W-SUN')]).sum()[:-10].sum()
    cola=prim.groupby([pd.Grouper(key='Fecha', freq='W-SUN')]).sum().tail(10)
    for i in range(1,11):
        DF=DF.append((cola[:i].sum()+suma_atras)/l_poblacion)
    DF.index=cola.index
    DF=DF.drop(['Desconocido Valparaiso','Fecha'],axis=1)
    return DF

indicador(primera).to_excel('primera_dosis.xlsx')
indicador(segunda).to_excel('segunda_dosis.xlsx')
indicador(refuerzo).to_excel('refuerzo_dosis.xlsx')
indicador(cuarta).to_excel('cuarta_dosis.xlsx')
indicador(unica).to_excel('unica_dosis.xlsx')

