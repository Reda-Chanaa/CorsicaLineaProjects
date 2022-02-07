import time
from django.http import HttpResponse
import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime


def MesureCSC(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        ecart = request.POST["ecart"]

        df_sauv = pd.read_csv(File1,sep=";", index_col=False)
        df_JOUR = pd.read_csv(File2,sep=";", index_col=False)

        # mesure 1
        df_sauv=pd.pivot_table(df_sauv[(df_sauv.RESEAU == "CORSE") &(df_sauv.ARMATEUR == "CL")], index=['SAIL_ID','NAVIRE','MOIS','DATE_DEPART','PORT_DEPART','PORT_ARRIVEE'],aggfunc={'PAX':np.sum})
        df_sauv.reset_index(inplace=True)
        for i in range(len(df_JOUR)):
            if df_JOUR["SAIL_ID"][i] not in df_sauv["SAIL_ID"].values:
                df_sauv=df_sauv.append({"SAIL_ID":df_JOUR["SAIL_ID"][i],'NAVIRE':df_JOUR['NAVIRE'][i],'MOIS':df_JOUR['MOIS'][i],'DATE_DEPART':df_JOUR['DATE_DEPART'][i],'PORT_DEPART':df_JOUR['PORT_DEPART'][i],'PORT_ARRIVEE':df_JOUR['PORT_ARRIVEE'][i],'PAX':0},ignore_index=True)
        df_sauv["DATE_DEPART"] = pd.to_datetime(df_sauv["DATE_DEPART"]).dt.date
        df_sauv = df_sauv[(df_sauv["DATE_DEPART"] > date.today())]
        df_sauv.dropna(inplace=True)
        df_sauv=df_sauv.sort_values(by = 'SAIL_ID')
        mycolumns = ['SAIL_ID','NAVIRE','MOIS','DATE_DEPART','PORT_DEPART','PORT_ARRIVEE','PAX'] 
        df_sauv=df_sauv[mycolumns]
        df_sauv["DATE_DEPART"] = pd.to_datetime(df_sauv["DATE_DEPART"])
        df_sauv['DATE_DEPART'] = df_sauv["DATE_DEPART"].map(str)
        df_sauv.dropna(inplace=True)
        df_sauv.reset_index(drop=True, inplace=True)
        print(df_sauv)

        # mesure 2
        df_JOUR=pd.pivot_table(df_JOUR[(df_JOUR.RESEAU == "CORSE") &(df_JOUR.ARMATEUR == "CL")], index=['SAIL_ID','NAVIRE','MOIS','DATE_DEPART','PORT_DEPART','PORT_ARRIVEE'],aggfunc={'PAX':np.sum})
        df_JOUR.reset_index(inplace=True)
        df_JOUR=df_JOUR.sort_values(by = 'SAIL_ID')
        mycolumns = ['SAIL_ID','NAVIRE','MOIS','DATE_DEPART','PORT_DEPART','PORT_ARRIVEE','PAX'] 
        df_JOUR=df_JOUR[mycolumns]
        df_JOUR.dropna(inplace=True)
        df_JOUR.reset_index(inplace=True, drop=True)
        print(df_JOUR)

        # Mesure final
        df=pd.merge(df_JOUR, df_sauv, on=['SAIL_ID','NAVIRE','MOIS','PORT_DEPART','PORT_ARRIVEE'])
        df["ECART"]=df["PAX_x"]-df["PAX_y"]
        df = df[(df["ECART"] >=15)]
        df.reset_index(drop=True, inplace=True)
        df['SENS'] = ["N" if sens =="MRS" else "S" for sens in df['PORT_DEPART']]
        df = df.drop(['DATE_DEPART_y'], axis=1) 
        df=df.sort_values(["SENS","MOIS","DATE_DEPART_x",], ascending = (True, True,True))
        df.reset_index(drop=True, inplace=True)
        df.columns = [
                    'ID', 'NAVIRE','MOIS', 'DATE', 'DEPART','ARRIVEE', 'VENTEJ','VENTE','ECART','SENS']
        print("------------------")
        print(df)

    total = time.time() - start_time
    print(total)
    return HttpResponse(df.to_json(orient='records'))