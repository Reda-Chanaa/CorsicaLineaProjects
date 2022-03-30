import time
from django.http import HttpResponse
from datetime import datetime
from datetime import timedelta, date
import pandas as pd
import numpy as np
import datetime

def concoCSC(data):
    
    df1=df1[['ARM','JOUR','NAV','DATE','HEURE','DEP','ARR','ID','PackageId']]
    df2=df2[['ARM','JOUR','NAV','DATE','HEURE','DEP','ARR','ID','PackageId']]

    df1["MOIS"]=pd.DatetimeIndex(df1['DATE']).month
    df1['DAY'] = pd.DatetimeIndex(df1['DATE']).day
    df1['YEAR'] = pd.DatetimeIndex(df1['DATE']).year

    df_new = df2.rename(columns={'ID': 'ID REF','NAV':'NAV REF','DATE':'DATE REF'})
    df_new["MOIS"]=pd.DatetimeIndex(df_new['DATE REF']).month
    df_new['DAY'] = pd.DatetimeIndex(df_new['DATE REF']).day
    df_new['YEAR'] = pd.DatetimeIndex(df_new['DATE REF']).year

    return data
def ConcoCSC(request):
    start_time = time.time()
    if request.method == 'POST':
        xls = pd.ExcelFile('CONCO Brut Colab.xlsx')
        df1 = pd.read_excel(xls, 'CSC 2021')
        df2 = pd.read_excel(xls, 'CSC 2022')
    total = time.time() - start_time
    print(total)
    return HttpResponse(df.to_json(orient='records'))