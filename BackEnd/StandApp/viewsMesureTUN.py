import time
from django.http import HttpResponse
import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime


def MesureTUN(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        ecart = request.POST["ecart"]

        df_sauv = pd.read_csv(File1,sep=";", index_col=False)
        df_JOUR = pd.read_csv(File2,sep=";", index_col=False)

        # mesure 1
        df_sauv=pd.pivot_table(df_sauv[(df_sauv.RESEAU == "TUNISIE") &(df_sauv.ARMATEUR == "CL")], index=['SAIL_ID','NAVIRE','MOIS','DATE_DEPART','PORT_DEPART','PORT_ARRIVEE'],aggfunc={'PAX':np.sum})
        df_sauv.reset_index(inplace=True)
        datetimes = pd.to_datetime(df_sauv["DATE_DEPART"],format='%d/%m/%Y %H:%M')
        df_sauv[['year','month','day']] = datetimes.dt.date.astype(str).str.split('-',expand=True)
        datetimes = pd.to_datetime(df_JOUR["DATE_DEPART"],format='%d/%m/%Y %H:%M')
        df_JOUR[['year','month','day']] = datetimes.dt.date.astype(str).str.split('-',expand=True)
        df_sauv = df_sauv[(df_sauv["day"].astype(int) >= datetime.now().day) & (df_sauv["month"].astype(int) >= datetime.now().month) & (df_sauv["year"].astype(int) >= datetime.now().year)]
        df_JOUR = df_JOUR[(df_JOUR["day"].astype(int) >= datetime.now().day) & (df_JOUR["month"].astype(int) >= datetime.now().month) & (df_JOUR["year"].astype(int) >= datetime.now().year)]
        df_JOUR.reset_index(inplace=True, drop=True)
        df_sauv.reset_index(inplace=True, drop=True)
        for i in range(len(df_JOUR)):
            if df_JOUR["SAIL_ID"][i] not in df_sauv["SAIL_ID"].values:
                df_sauv=df_sauv.append({"SAIL_ID":df_JOUR["SAIL_ID"][i],'NAVIRE':df_JOUR['NAVIRE'][i],'MOIS':df_JOUR['MOIS'][i],'DATE_DEPART':df_JOUR['DATE_DEPART'][i],'PORT_DEPART':df_JOUR['PORT_DEPART'][i],'PORT_ARRIVEE':df_JOUR['PORT_ARRIVEE'][i],'PAX':0,'year':df_JOUR['year'][i],'month':df_JOUR['month'][i],'day':df_JOUR['day'][i]},ignore_index=True)
        df_sauv=df_sauv.sort_values(by = 'SAIL_ID')
        mycolumns = ['SAIL_ID','NAVIRE','MOIS','DATE_DEPART','PORT_DEPART','PORT_ARRIVEE','PAX'] 
        df_sauv=df_sauv[mycolumns]
        df_sauv["DATE_DEPART"] = pd.to_datetime(df_sauv["DATE_DEPART"],format='%d/%m/%Y %H:%M')
        #df_sauv['DATE_DEPART'] = df_sauv["DATE_DEPART"].map(str)

        df_sauv.reset_index(drop=True, inplace=True)
        df_sauv.dropna(inplace=True)
        print(df_sauv)

        # mesure 2
        df_JOUR=pd.pivot_table(df_JOUR[(df_JOUR.RESEAU == "TUNISIE") &(df_JOUR.ARMATEUR == "CL")], index=['SAIL_ID','NAVIRE','MOIS','DATE_DEPART','PORT_DEPART','PORT_ARRIVEE'],aggfunc={'PAX':np.sum})
        df_JOUR.reset_index(inplace=True)
        df_JOUR=df_JOUR.sort_values(by = 'SAIL_ID')
        mycolumns = ['SAIL_ID','NAVIRE','MOIS','DATE_DEPART','PORT_DEPART','PORT_ARRIVEE','PAX'] 
        df_JOUR=df_JOUR[mycolumns]
        df_JOUR["DATE_DEPART"] = pd.to_datetime(df_JOUR["DATE_DEPART"],format='%d/%m/%Y %H:%M')
        #df_JOUR['DATE_DEPART'] = df_JOUR["DATE_DEPART"].map(str)
        df_JOUR.dropna(inplace=True)
        df_JOUR.reset_index(inplace=True, drop=True)
        print(df_JOUR)

        # Mesure final
        df=pd.merge(df_JOUR, df_sauv, on=['SAIL_ID','NAVIRE','MOIS','PORT_DEPART','PORT_ARRIVEE'])
        df["ECART"]=df["PAX_x"]-df["PAX_y"]
        df = df[(df["ECART"] >= float(ecart))]
        df.reset_index(drop=True, inplace=True)
        df['SENS'] = ["N" if sens =="MRS" else "S" for sens in df['PORT_DEPART']]
        df = df.drop(['DATE_DEPART_y'], axis=1) 
        df=df.sort_values(["SENS","MOIS","DATE_DEPART_x",], ascending = (True, True,True))
        df.reset_index(drop=True, inplace=True)
        df.columns = [
                    'ID', 'NAVIRE','MOIS', 'DATE', 'DEPART','ARRIVEE', 'VENTEJ','VENTE','ECART','SENS']
        print("------------------")
        df['DATE'] = df["DATE"].map(str)
        print(df.dtypes)
        print(df)

    total = time.time() - start_time
    print(total)
    return HttpResponse(df.to_json(orient='records'))