from datetime import date
import time
import pandas as pd
from django.http import HttpResponse
from datetime import datetime


def MesureCSC(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        ecart = request.POST["ecart"]

        # mesure 1
        df_sauv = pd.read_excel(File1, sheet_name=0, skiprows=4)
        df_sauv.query(' ARM == ["CL"]', inplace=True)
        df_sauv = df_sauv.iloc[:, 0:53]
        df_sauv["DATE"] = pd.to_datetime(df_sauv["DATE"]).dt.date
        df_sauv = df_sauv[(df_sauv["DATE"] > date.today())]
        df_sauv = df_sauv.sort_values(by='ID')
        mycolumns = [
            'ID', 'NAV', 'SENS', 'DATE', 'NVX', 'Ventes Pax Brutes'
        ]
        df_sauv = df_sauv[mycolumns]
        df_sauv["DATE"] = pd.to_datetime(df_sauv["DATE"])
        df_sauv.dropna(inplace=True)
        df_sauv.reset_index(inplace=True, drop=True)
        print(df_sauv)

        # mesure 2
        df_JOUR = pd.read_excel(File2, sheet_name=0, skiprows=4)
        df_JOUR.query(' ARM == ["CL"]', inplace=True)
        df_JOUR = df_JOUR.iloc[:, 0:53]
        df_JOUR = df_JOUR.sort_values(by='ID')
        mycolumns = [
            'ID', 'NAV', 'SENS', 'DATE', 'NVX', 'Ventes Pax Brutes'
        ]
        df_JOUR = df_JOUR[mycolumns]
        df_JOUR.dropna(inplace=True)
        df_JOUR.reset_index(inplace=True, drop=True)
        print(df_JOUR)

        # Mesure
        df_JOUR.columns = [
            'ID', 'NAVIRE', 'SENS', 'DATE', 'NIVEAU', 'VENTEJ'
        ]
        df_JOUR["VENTE"] = df_sauv["Ventes Pax Brutes"]
        df_JOUR["ECART"] = df_JOUR["VENTEJ"] - df_JOUR["VENTE"]
        df_JOUR['DATE'] = df_JOUR["DATE"].map(str)
        df_JOUR['NIVEAU'] = df_JOUR["NIVEAU"].map(str)
        df_JOUR = df_JOUR[(df_JOUR["ECART"] >= float(ecart))]
        df_JOUR=df_JOUR.sort_values(["SENS", "DATE"], ascending = (True, True))
        df_JOUR.dropna(inplace=True)
        df_JOUR.reset_index(inplace=True, drop=True)
        print("------------------")
        print(df_JOUR)

    total = time.time() - start_time
    print(total)
    return HttpResponse(df_JOUR.to_json(orient='records'))