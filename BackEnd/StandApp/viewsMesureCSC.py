from optparse import Values
import time
from django.http import HttpResponse
import pandas as pd
import numpy as np
from datetime import date
import psycopg2 
from datetime import datetime
from StandApp.models import MesureCorse
from StandApp.serializers import MesureCSCSerializer
from config import config

from django.http import HttpResponse

""" Connect to the PostgreSQL database server """
conn = None
cur = None
try:
    # read connection parameters
    params = config()

    # connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
		
    # create a cursor
    cur = conn.cursor()
        
	# execute a statement
    cur.execute('SELECT version()')
       
except (Exception, psycopg2.DatabaseError) as error:
    print(error)


def MesureCSC(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        ecart = request.POST["ecart"]

        df_sauv = pd.read_csv(File1, sep=";", index_col=False)
        df_JOUR = pd.read_csv(File2, sep=";", index_col=False)

        # mesure 1
        df_sauv = pd.pivot_table(
            df_sauv[(df_sauv.RESEAU == "CORSE") & (df_sauv.ARMATEUR == "CL")],
            index=[
                'SAIL_ID', 'NAVIRE', 'MOIS', 'DATE_DEPART', 'PORT_DEPART',
                'PORT_ARRIVEE'
            ],
            aggfunc={'PAX': np.sum})
        df_sauv.reset_index(inplace=True)
        datetimes = pd.to_datetime(df_sauv["DATE_DEPART"],
                                   format='%d/%m/%Y %H:%M')
        df_sauv[['year', 'month',
                 'day']] = datetimes.dt.date.astype(str).str.split('-',
                                                                   expand=True)
        datetimes = pd.to_datetime(df_JOUR["DATE_DEPART"],
                                   format='%d/%m/%Y %H:%M')
        df_JOUR[['year', 'month',
                 'day']] = datetimes.dt.date.astype(str).str.split('-',
                                                                   expand=True)
        df_sauv = df_sauv[
            ((df_sauv["year"].astype(int) == datetime.now().year) &
             (df_sauv["month"].astype(int) == datetime.now().month) &
             (df_sauv["day"].astype(int) > datetime.now().day)) |
            ((df_sauv["year"].astype(int) == datetime.now().year) &
             (df_sauv["month"].astype(int) > datetime.now().month)) |
            ((df_sauv["year"].astype(int) > datetime.now().year))]
        df_JOUR = df_JOUR[
            ((df_JOUR["year"].astype(int) == datetime.now().year) &
             (df_JOUR["month"].astype(int) == datetime.now().month) &
             (df_JOUR["day"].astype(int) > datetime.now().day)) |
            ((df_JOUR["year"].astype(int) == datetime.now().year) &
             (df_JOUR["month"].astype(int) > datetime.now().month)) |
            ((df_JOUR["year"].astype(int) > datetime.now().year))]

        df_JOUR.reset_index(inplace=True, drop=True)
        df_sauv.reset_index(inplace=True, drop=True)
        for i in range(len(df_JOUR)):
            if df_JOUR["SAIL_ID"][i] not in df_sauv["SAIL_ID"].values:
                df_sauv = df_sauv.append(
                    {
                        "SAIL_ID": df_JOUR["SAIL_ID"][i],
                        'NAVIRE': df_JOUR['NAVIRE'][i],
                        'MOIS': df_JOUR['MOIS'][i],
                        'DATE_DEPART': df_JOUR['DATE_DEPART'][i],
                        'PORT_DEPART': df_JOUR['PORT_DEPART'][i],
                        'PORT_ARRIVEE': df_JOUR['PORT_ARRIVEE'][i],
                        'PAX': 0,
                        'year': df_JOUR['year'][i],
                        'month': df_JOUR['month'][i],
                        'day': df_JOUR['day'][i]
                    },
                    ignore_index=True)
        df_sauv = df_sauv.sort_values(by='SAIL_ID')
        mycolumns = [
            'SAIL_ID', 'NAVIRE', 'MOIS', 'DATE_DEPART', 'PORT_DEPART',
            'PORT_ARRIVEE', 'PAX', 'year'
        ]
        df_sauv = df_sauv[mycolumns]
        df_sauv["DATE_DEPART"] = pd.to_datetime(df_sauv["DATE_DEPART"],
                                                format='%d/%m/%Y %H:%M')

        df_sauv.reset_index(drop=True, inplace=True)
        df_sauv.dropna(inplace=True)

        # mesure 2
        df_JOUR = pd.pivot_table(
            df_JOUR[(df_JOUR.RESEAU == "CORSE") & (df_JOUR.ARMATEUR == "CL")],
            index=[
                'SAIL_ID', 'NAVIRE', 'MOIS', 'DATE_DEPART', 'PORT_DEPART',
                'PORT_ARRIVEE'
            ],
            aggfunc={'PAX': np.sum})
        df_JOUR.reset_index(inplace=True)
        datetimes = pd.to_datetime(df_JOUR["DATE_DEPART"],
                                   format='%d/%m/%Y %H:%M')
        df_JOUR[['year', 'month',
                 'day']] = datetimes.dt.date.astype(str).str.split('-',
                                                                   expand=True)
        df_JOUR = df_JOUR[
            ((df_JOUR["year"].astype(int) == datetime.now().year) &
             (df_JOUR["month"].astype(int) == datetime.now().month) &
             (df_JOUR["day"].astype(int) > datetime.now().day)) |
            ((df_JOUR["year"].astype(int) == datetime.now().year) &
             (df_JOUR["month"].astype(int) > datetime.now().month)) |
            ((df_JOUR["year"].astype(int) > datetime.now().year))]

        df_JOUR.reset_index(inplace=True, drop=True)
        df_sauv.reset_index(inplace=True, drop=True)
        df_JOUR = df_JOUR.sort_values(by='SAIL_ID')
        mycolumns = [
            'SAIL_ID', 'NAVIRE', 'MOIS', 'DATE_DEPART', 'PORT_DEPART',
            'PORT_ARRIVEE', 'PAX', 'year'
        ]
        df_JOUR = df_JOUR[mycolumns]
        df_JOUR["DATE_DEPART"] = pd.to_datetime(df_JOUR["DATE_DEPART"],
                                                format='%d/%m/%Y %H:%M')
        df_JOUR.dropna(inplace=True)
        df_JOUR.reset_index(inplace=True, drop=True)

        # Mesure final
        df = pd.merge(df_JOUR,
                      df_sauv,
                      on=[
                          'SAIL_ID', 'NAVIRE', 'MOIS', 'PORT_DEPART',
                          'PORT_ARRIVEE', 'year'
                      ])
        df["ECART"] = df["PAX_x"] - df["PAX_y"]
        # df de report
        df_test = pd.DataFrame(df)
        df_test.reset_index(drop=True, inplace=True)
        df_test['SENS'] = [
            "N" if sens == "MRS" else "S" for sens in df_test['PORT_DEPART']
        ]
        df_test = df_test.drop(['DATE_DEPART_y'], axis=1)
        df_test = df_test.sort_values([
            "SENS",
            "MOIS",
            "DATE_DEPART_x",
        ],
                                      ascending=(True, True, True))
        df_test.reset_index(drop=True, inplace=True)
        df_test.columns = [
            'ID', 'NAVIRE', 'MOIS', 'DATE', 'DEPART', 'ARRIVEE', 'VENTEJ',
            'YEAR', 'VENTE', 'ECART', 'SENS'
        ]
        df_test['DATE'] = df_test["DATE"].map(str)

        # df de mesure
        df = df[(df["ECART"] >= float(ecart))]
        df.reset_index(drop=True, inplace=True)
        df['SENS'] = [
            "N" if sens == "MRS" else "S" for sens in df['PORT_DEPART']
        ]
        df = df.drop(['DATE_DEPART_y'], axis=1)
        df = df.sort_values([
            "SENS",
            "MOIS",
            "DATE_DEPART_x",
        ],
                            ascending=(True, True, True))
        df.reset_index(drop=True, inplace=True)
        df.columns = [
            'ID', 'NAVIRE', 'MOIS', 'DATE', 'DEPART', 'ARRIVEE', 'VENTEJ',
            'YEAR', 'VENTE', 'ECART', 'SENS'
        ]
        df['DATE'] = df["DATE"].map(str)
        print(df)
        # Report
        if str(datetime.now().year) in df_test["YEAR"].values:
            df_report = pd.pivot_table(df_test[(df_test.YEAR == str(
                datetime.now().year))],
                                       index=['MOIS'],
                                       aggfunc={'ECART': np.sum})
            df_report.reset_index(inplace=True)
            for i in range(len(df_report)):
                if 1 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 1,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 2 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 2,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 3 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 3,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 4 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 4,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 5 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 5,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 6 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 6,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 7 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 7,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 8 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 8,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 9 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 9,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 10 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 10,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 11 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 11,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 12 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 12,
                        'ECART': 0
                    },
                                                 ignore_index=True)
            df_report = df_report.sort_values(by='MOIS')
            df_report.reset_index(inplace=True, drop=True)

            if datetime.now().month <= 9:
                month = '0' + str(datetime.now().month)
            else:
                month = str(datetime.now().month)
            if datetime.now().day <= 9:
                day = '0' + str(datetime.now().day)
            else:
                day = str(datetime.now().day)
            date = day + '/' + month + '/' + str(datetime.now().year)
            
            print('------******-------')
            mesurecsc=MesureCorse.objects.filter(Annee_Report=str(datetime.now().year), Date=date)
            df_test_ = pd.DataFrame(list(mesurecsc.values()))
            print(df_test_)
            print(len(df_test_))
            print('------******-------')

            if (len(df_test_) == 0):
                print("Introuvable")
                if ((df_report.ECART[0] != 0) | (df_report.ECART[1] != 0) |
                    (df_report.ECART[2] != 0) | (df_report.ECART[3] != 0) |
                    (df_report.ECART[4] != 0) | (df_report.ECART[5] != 0) |
                    (df_report.ECART[6] != 0) | (df_report.ECART[7] != 0) |
                    (df_report.ECART[8] != 0) | (df_report.ECART[9] != 0) |
                    (df_report.ECART[10] != 0) | (df_report.ECART[11] != 0)):
                    print("rentré")
                    MesureCorse.objects.create(Annee_Report=
                        str(datetime.now().year),
                        Date=date,Annee=str(datetime.now().year),
                        Mois=
                        str(datetime.now().month),
                        Jour=
                        str(datetime.now().day),
                        Jan=
                        str(df_report.ECART[0]),
                        Feb=
                        str(df_report.ECART[1]),
                        Mar=
                        str(df_report.ECART[2]),
                        Apr=
                        str(df_report.ECART[3]),
                        May=
                        str(df_report.ECART[4]),
                        Jun=
                        str(df_report.ECART[5]),
                        Jul=
                        str(df_report.ECART[6]),
                        Aug=
                        str(df_report.ECART[7]),
                        Sep=
                        str(df_report.ECART[8]),
                        Oct=
                        str(df_report.ECART[9]),
                        Nov=
                        str(df_report.ECART[10]),
                        Dec=
                        str(df_report.ECART[11]))
                    
                    print("ajouté")
                else:
                    print("pas ajouté")
            else:
                mesurecsc.update(Annee= str(datetime.now().year),
                            Mois =str(datetime.now().month),
                            Jour= str(datetime.now().day),
                            Jan= str(df_report.ECART[0]),
                            Feb= str(df_report.ECART[1]),
                            Mar= str(df_report.ECART[2]),
                            Apr= str(df_report.ECART[3]),
                            May= str(df_report.ECART[4]),
                            Jun= str(df_report.ECART[5]),
                            Jul= str(df_report.ECART[6]),
                            Aug= str(df_report.ECART[7]),
                            Sep= str(df_report.ECART[8]),
                            Oct= str(df_report.ECART[9]),
                            Nov= str(df_report.ECART[10]),
                            Dec= str(df_report.ECART[11]))
                
                print("trouvable et update")

        if str(datetime.now().year + 1) in df_test["YEAR"].values:
            df_report = pd.pivot_table(
                df_test[(df_test.YEAR == str(datetime.now().year + 1))],
                index=['MOIS'],
                aggfunc={'ECART': np.sum})
            df_report.reset_index(inplace=True)

            for i in range(len(df_report)):
                if 1 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 1,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 2 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 2,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 3 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 3,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 4 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 4,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 5 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 5,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 6 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 6,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 7 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 7,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 8 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 8,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 9 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 9,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 10 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 10,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 11 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 11,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 12 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 12,
                        'ECART': 0
                    },
                                                 ignore_index=True)
            df_report = df_report.sort_values(by='MOIS')
            df_report.reset_index(inplace=True, drop=True)

            if datetime.now().month <= 9:
                month = '0' + str(datetime.now().month)
            else:
                month = str(datetime.now().month)
            if datetime.now().day <= 9:
                day = '0' + str(datetime.now().day)
            else:
                day = str(datetime.now().day)
            date = day + '/' + month + '/' + str(datetime.now().year)

            print('------******-------')
            mesurecsc=MesureCorse.objects.filter(Annee_Report=str(datetime.now().year+1), Date=date)
            df_test_ = pd.DataFrame(list(mesurecsc.values()))
            print(df_test_)
            print(len(df_test_))
            print('------******-------')

            if (len(df_test_) == 0):
                print("introuvable +")
                if ((df_report.ECART[0] != 0) | (df_report.ECART[1] != 0) |
                    (df_report.ECART[2] != 0) | (df_report.ECART[3] != 0) |
                    (df_report.ECART[4] != 0) | (df_report.ECART[5] != 0) |
                    (df_report.ECART[6] != 0) | (df_report.ECART[7] != 0) |
                    (df_report.ECART[8] != 0) | (df_report.ECART[9] != 0) |
                    (df_report.ECART[10] != 0) | (df_report.ECART[11] != 0)):
                    print("rentré+")
                    MesureCorse.objects.create(Annee_Report=
                        str(datetime.now().year + 1),
                        Date=date,Annee=str(datetime.now().year),
                        Mois=
                        str(datetime.now().month),
                        Jour=
                        str(datetime.now().day),
                        Jan=
                        str(df_report.ECART[0]),
                        Feb=
                        str(df_report.ECART[1]),
                        Mar=
                        str(df_report.ECART[2]),
                        Apr=
                        str(df_report.ECART[3]),
                        May=
                        str(df_report.ECART[4]),
                        Jun=
                        str(df_report.ECART[5]),
                        Jul=
                        str(df_report.ECART[6]),
                        Aug=
                        str(df_report.ECART[7]),
                        Sep=
                        str(df_report.ECART[8]),
                        Oct=
                        str(df_report.ECART[9]),
                        Nov=
                        str(df_report.ECART[10]),
                        Dec=
                        str(df_report.ECART[11]))
                    
                    print("ajouté +")
                else:
                    print("pas ajouté +")
            else:
                mesurecsc.update(Annee= str(datetime.now().year),
                            Mois =str(datetime.now().month),
                            Jour= str(datetime.now().day),
                            Jan= str(df_report.ECART[0]),
                            Feb= str(df_report.ECART[1]),
                            Mar= str(df_report.ECART[2]),
                            Apr= str(df_report.ECART[3]),
                            May= str(df_report.ECART[4]),
                            Jun= str(df_report.ECART[5]),
                            Jul= str(df_report.ECART[6]),
                            Aug= str(df_report.ECART[7]),
                            Sep= str(df_report.ECART[8]),
                            Oct= str(df_report.ECART[9]),
                            Nov= str(df_report.ECART[10]),
                            Dec= str(df_report.ECART[11]))
                
                print("trouvable et update +")
    total = time.time() - start_time
    print(total)
    print(df.dtypes)
    return HttpResponse(df.to_json(orient='records'))


def MesureCSCPLUS(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        ecartSup = request.POST["ecartSup"]
        ecartInf = request.POST["ecartInf"]

        df_sauv = pd.read_csv(File1, sep=";", index_col=False)
        df_JOUR = pd.read_csv(File2, sep=";", index_col=False)

        # mesure 1
        df_sauv = pd.pivot_table(
            df_sauv[(df_sauv.RESEAU == "CORSE") & (df_sauv.ARMATEUR == "CL")],
            index=[
                'SAIL_ID', 'NAVIRE', 'MOIS', 'DATE_DEPART', 'PORT_DEPART',
                'PORT_ARRIVEE'
            ],
            aggfunc={'PAX': np.sum})
        df_sauv.reset_index(inplace=True)
        datetimes = pd.to_datetime(df_sauv["DATE_DEPART"],
                                   format='%d/%m/%Y %H:%M')
        df_sauv[['year', 'month',
                 'day']] = datetimes.dt.date.astype(str).str.split('-',
                                                                   expand=True)
        datetimes = pd.to_datetime(df_JOUR["DATE_DEPART"],
                                   format='%d/%m/%Y %H:%M')
        df_JOUR[['year', 'month',
                 'day']] = datetimes.dt.date.astype(str).str.split('-',
                                                                   expand=True)
        df_sauv = df_sauv[
            ((df_sauv["year"].astype(int) == datetime.now().year) &
             (df_sauv["month"].astype(int) == datetime.now().month) &
             (df_sauv["day"].astype(int) > datetime.now().day)) |
            ((df_sauv["year"].astype(int) == datetime.now().year) &
             (df_sauv["month"].astype(int) > datetime.now().month)) |
            ((df_sauv["year"].astype(int) > datetime.now().year))]
        df_JOUR = df_JOUR[
            ((df_JOUR["year"].astype(int) == datetime.now().year) &
             (df_JOUR["month"].astype(int) == datetime.now().month) &
             (df_JOUR["day"].astype(int) > datetime.now().day)) |
            ((df_JOUR["year"].astype(int) == datetime.now().year) &
             (df_JOUR["month"].astype(int) > datetime.now().month)) |
            ((df_JOUR["year"].astype(int) > datetime.now().year))]

        df_JOUR.reset_index(inplace=True, drop=True)
        df_sauv.reset_index(inplace=True, drop=True)
        for i in range(len(df_JOUR)):
            if df_JOUR["SAIL_ID"][i] not in df_sauv["SAIL_ID"].values:
                df_sauv = df_sauv.append(
                    {
                        "SAIL_ID": df_JOUR["SAIL_ID"][i],
                        'NAVIRE': df_JOUR['NAVIRE'][i],
                        'MOIS': df_JOUR['MOIS'][i],
                        'DATE_DEPART': df_JOUR['DATE_DEPART'][i],
                        'PORT_DEPART': df_JOUR['PORT_DEPART'][i],
                        'PORT_ARRIVEE': df_JOUR['PORT_ARRIVEE'][i],
                        'PAX': 0,
                        'year': df_JOUR['year'][i],
                        'month': df_JOUR['month'][i],
                        'day': df_JOUR['day'][i]
                    },
                    ignore_index=True)
        df_sauv = df_sauv.sort_values(by='SAIL_ID')
        mycolumns = [
            'SAIL_ID', 'NAVIRE', 'MOIS', 'DATE_DEPART', 'PORT_DEPART',
            'PORT_ARRIVEE', 'PAX', 'year'
        ]
        df_sauv = df_sauv[mycolumns]
        df_sauv["DATE_DEPART"] = pd.to_datetime(df_sauv["DATE_DEPART"],
                                                format='%d/%m/%Y %H:%M')

        df_sauv.reset_index(drop=True, inplace=True)
        df_sauv.dropna(inplace=True)

        # mesure 2
        df_JOUR = pd.pivot_table(
            df_JOUR[(df_JOUR.RESEAU == "CORSE") & (df_JOUR.ARMATEUR == "CL")],
            index=[
                'SAIL_ID', 'NAVIRE', 'MOIS', 'DATE_DEPART', 'PORT_DEPART',
                'PORT_ARRIVEE'
            ],
            aggfunc={'PAX': np.sum})
        df_JOUR.reset_index(inplace=True)
        datetimes = pd.to_datetime(df_JOUR["DATE_DEPART"],
                                   format='%d/%m/%Y %H:%M')
        df_JOUR[['year', 'month',
                 'day']] = datetimes.dt.date.astype(str).str.split('-',
                                                                   expand=True)
        df_JOUR = df_JOUR[
            ((df_JOUR["year"].astype(int) == datetime.now().year) &
             (df_JOUR["month"].astype(int) == datetime.now().month) &
             (df_JOUR["day"].astype(int) > datetime.now().day)) |
            ((df_JOUR["year"].astype(int) == datetime.now().year) &
             (df_JOUR["month"].astype(int) > datetime.now().month)) |
            ((df_JOUR["year"].astype(int) > datetime.now().year))]

        df_JOUR.reset_index(inplace=True, drop=True)
        df_sauv.reset_index(inplace=True, drop=True)
        df_JOUR = df_JOUR.sort_values(by='SAIL_ID')
        mycolumns = [
            'SAIL_ID', 'NAVIRE', 'MOIS', 'DATE_DEPART', 'PORT_DEPART',
            'PORT_ARRIVEE', 'PAX', 'year'
        ]
        df_JOUR = df_JOUR[mycolumns]
        df_JOUR["DATE_DEPART"] = pd.to_datetime(df_JOUR["DATE_DEPART"],
                                                format='%d/%m/%Y %H:%M')
        df_JOUR.dropna(inplace=True)
        df_JOUR.reset_index(inplace=True, drop=True)

        # Mesure final
        df = pd.merge(df_JOUR,
                      df_sauv,
                      on=[
                          'SAIL_ID', 'NAVIRE', 'MOIS', 'PORT_DEPART',
                          'PORT_ARRIVEE', 'year'
                      ])
        df["ECART"] = df["PAX_x"] - df["PAX_y"]
        # df de report
        df_test = pd.DataFrame(df)
        df_test.reset_index(drop=True, inplace=True)
        df_test['SENS'] = [
            "N" if sens == "MRS" else "S" for sens in df_test['PORT_DEPART']
        ]
        df_test = df_test.drop(['DATE_DEPART_y'], axis=1)
        df_test = df_test.sort_values([
            "SENS",
            "MOIS",
            "DATE_DEPART_x",
        ],
                                      ascending=(True, True, True))
        df_test.reset_index(drop=True, inplace=True)
        df_test.columns = [
            'ID', 'NAVIRE', 'MOIS', 'DATE', 'DEPART', 'ARRIVEE', 'VENTEJ',
            'YEAR', 'VENTE', 'ECART', 'SENS'
        ]
        df_test['DATE'] = df_test["DATE"].map(str)
        df_test = df_test[(df_test["ECART"] <= float(ecartInf))]

        # df de mesure
        df = df[(df["ECART"] >= float(ecartSup))
                & (df["ECART"] <= float(ecartInf))]
        df.reset_index(drop=True, inplace=True)
        df['SENS'] = [
            "N" if sens == "MRS" else "S" for sens in df['PORT_DEPART']
        ]
        df = df.drop(['DATE_DEPART_y'], axis=1)
        df = df.sort_values([
            "SENS",
            "MOIS",
            "DATE_DEPART_x",
        ],
                            ascending=(True, True, True))
        df.reset_index(drop=True, inplace=True)
        df.columns = [
            'ID', 'NAVIRE', 'MOIS', 'DATE', 'DEPART', 'ARRIVEE', 'VENTEJ',
            'YEAR', 'VENTE', 'ECART', 'SENS'
        ]
        df['DATE'] = df["DATE"].map(str)
        print(df)
        # Report
        if str(datetime.now().year) in df_test["YEAR"].values:
            df_report = pd.pivot_table(df_test[(df_test.YEAR == str(
                datetime.now().year))],
                                       index=['MOIS'],
                                       aggfunc={'ECART': np.sum})
            df_report.reset_index(inplace=True)
            for i in range(len(df_report)):
                if 1 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 1,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 2 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 2,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 3 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 3,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 4 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 4,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 5 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 5,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 6 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 6,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 7 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 7,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 8 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 8,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 9 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 9,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 10 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 10,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 11 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 11,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 12 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 12,
                        'ECART': 0
                    },
                                                 ignore_index=True)
            df_report = df_report.sort_values(by='MOIS')
            df_report.reset_index(inplace=True, drop=True)

            if datetime.now().month <= 9:
                month = '0' + str(datetime.now().month)
            else:
                month = str(datetime.now().month)
            if datetime.now().day <= 9:
                day = '0' + str(datetime.now().day)
            else:
                day = str(datetime.now().day)
            date = day + '/' + month + '/' + str(datetime.now().year)

            print('------******-------')
            mesurecsc=MesureCorse.objects.filter(Annee_Report=str(datetime.now().year), Date=date)
            df_test_ = pd.DataFrame(list(mesurecsc.values()))
            print(df_test_)
            print(len(df_test_))
            print('------******-------')

            if (len(df_test_) == 0):
                print("Introuvable")
                if ((df_report.ECART[0] != 0) | (df_report.ECART[1] != 0) |
                    (df_report.ECART[2] != 0) | (df_report.ECART[3] != 0) |
                    (df_report.ECART[4] != 0) | (df_report.ECART[5] != 0) |
                    (df_report.ECART[6] != 0) | (df_report.ECART[7] != 0) |
                    (df_report.ECART[8] != 0) | (df_report.ECART[9] != 0) |
                    (df_report.ECART[10] != 0) | (df_report.ECART[11] != 0)):
                    print("rentré")

                    MesureCorse.objects.create(Annee_Report=
                        str(datetime.now().year),
                        Date=date,Annee=str(datetime.now().year),
                        Mois=
                        str(datetime.now().month),
                        Jour=
                        str(datetime.now().day),
                        Jan=
                        str(df_report.ECART[0]),
                        Feb=
                        str(df_report.ECART[1]),
                        Mar=
                        str(df_report.ECART[2]),
                        Apr=
                        str(df_report.ECART[3]),
                        May=
                        str(df_report.ECART[4]),
                        Jun=
                        str(df_report.ECART[5]),
                        Jul=
                        str(df_report.ECART[6]),
                        Aug=
                        str(df_report.ECART[7]),
                        Sep=
                        str(df_report.ECART[8]),
                        Oct=
                        str(df_report.ECART[9]),
                        Nov=
                        str(df_report.ECART[10]),
                        Dec=
                        str(df_report.ECART[11]))
                    
                    print("ajouté")
                else:
                    print("pas ajouté")
            else:
                mesurecsc.update(Annee= str(datetime.now().year),
                            Mois =str(datetime.now().month),
                            Jour= str(datetime.now().day),
                            Jan= str(df_report.ECART[0]),
                            Feb= str(df_report.ECART[1]),
                            Mar= str(df_report.ECART[2]),
                            Apr= str(df_report.ECART[3]),
                            May= str(df_report.ECART[4]),
                            Jun= str(df_report.ECART[5]),
                            Jul= str(df_report.ECART[6]),
                            Aug= str(df_report.ECART[7]),
                            Sep= str(df_report.ECART[8]),
                            Oct= str(df_report.ECART[9]),
                            Nov= str(df_report.ECART[10]),
                            Dec= str(df_report.ECART[11]))
                
                print("trouvable et update")

        if str(datetime.now().year + 1) in df_test["YEAR"].values:
            df_report = pd.pivot_table(
                df_test[(df_test.YEAR == str(datetime.now().year + 1))],
                index=['MOIS'],
                aggfunc={'ECART': np.sum})
            df_report.reset_index(inplace=True)

            for i in range(len(df_report)):
                if 1 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 1,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 2 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 2,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 3 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 3,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 4 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 4,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 5 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 5,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 6 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 6,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 7 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 7,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 8 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 8,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 9 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 9,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 10 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 10,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 11 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 11,
                        'ECART': 0
                    },
                                                 ignore_index=True)
                if 12 not in df_report["MOIS"].values:
                    df_report = df_report.append({
                        "MOIS": 12,
                        'ECART': 0
                    },
                                                 ignore_index=True)
            df_report = df_report.sort_values(by='MOIS')
            df_report.reset_index(inplace=True, drop=True)

            if datetime.now().month <= 9:
                month = '0' + str(datetime.now().month)
            else:
                month = str(datetime.now().month)
            if datetime.now().day <= 9:
                day = '0' + str(datetime.now().day)
            else:
                day = str(datetime.now().day)
            date = day + '/' + month + '/' + str(datetime.now().year)

            print('------******-------')
            mesurecsc=MesureCorse.objects.filter(Annee_Report=str(datetime.now().year+1), Date=date)
            df_test_ = pd.DataFrame(list(mesurecsc.values()))
            print(df_test_)
            print(len(df_test_))
            print('------******-------')

            if (len(df_test_) == 0):
                print("introuvable +")
                if ((df_report.ECART[0] != 0) | (df_report.ECART[1] != 0) |
                    (df_report.ECART[2] != 0) | (df_report.ECART[3] != 0) |
                    (df_report.ECART[4] != 0) | (df_report.ECART[5] != 0) |
                    (df_report.ECART[6] != 0) | (df_report.ECART[7] != 0) |
                    (df_report.ECART[8] != 0) | (df_report.ECART[9] != 0) |
                    (df_report.ECART[10] != 0) | (df_report.ECART[11] != 0)):
                    print("rentré+")
                    
                    MesureCorse.objects.create(Annee_Report=
                        str(datetime.now().year + 1),
                        Date=date,Annee=str(datetime.now().year),
                        Mois=
                        str(datetime.now().month),
                        Jour=
                        str(datetime.now().day),
                        Jan=
                        str(df_report.ECART[0]),
                        Feb=
                        str(df_report.ECART[1]),
                        Mar=
                        str(df_report.ECART[2]),
                        Apr=
                        str(df_report.ECART[3]),
                        May=
                        str(df_report.ECART[4]),
                        Jun=
                        str(df_report.ECART[5]),
                        Jul=
                        str(df_report.ECART[6]),
                        Aug=
                        str(df_report.ECART[7]),
                        Sep=
                        str(df_report.ECART[8]),
                        Oct=
                        str(df_report.ECART[9]),
                        Nov=
                        str(df_report.ECART[10]),
                        Dec=
                        str(df_report.ECART[11]))

                    print("ajouté +")
                else:
                    print("pas ajouté +")
            else:
                mesurecsc.update(Annee= str(datetime.now().year),
                            Mois =str(datetime.now().month),
                            Jour= str(datetime.now().day),
                            Jan= str(df_report.ECART[0]),
                            Feb= str(df_report.ECART[1]),
                            Mar= str(df_report.ECART[2]),
                            Apr= str(df_report.ECART[3]),
                            May= str(df_report.ECART[4]),
                            Jun= str(df_report.ECART[5]),
                            Jul= str(df_report.ECART[6]),
                            Aug= str(df_report.ECART[7]),
                            Sep= str(df_report.ECART[8]),
                            Oct= str(df_report.ECART[9]),
                            Nov= str(df_report.ECART[10]),
                            Dec= str(df_report.ECART[11]))

                print("trouvable et update +")
    total = time.time() - start_time
    print(total)
    print(df.dtypes)
    return HttpResponse(df.to_json(orient='records'))


def ReportCSC(request):
    start_time = time.time()
    if request.method == 'POST':
        annee = request.POST["annee"]
        df = pd.DataFrame(columns=[
            'Annee Report', 'Date', 'Annee', 'Mois', 'Jour', 'Jan', 'Feb',
            'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
            'Dec'
        ])
        mesurecsc=MesureCorse.objects.filter(Annee_Report=annee)
        
        df_test = pd.DataFrame(list(mesurecsc.values()))
        for i in range(len(df_test)):
            df.loc[i] = [
                df_test["Annee_Report"][i], df_test["Date"][i], df_test["Annee"][i],
                df_test["Mois"][i], df_test["Jour"][i], df_test["Jan"][i],
                df_test["Feb"][i], df_test["Mar"][i], df_test["Apr"][i], df_test["May"][i],
                df_test["Jun"][i], df_test["Jul"][i], df_test["Aug"][i], df_test["Sep"][i],
                df_test["Oct"][i], df_test["Nov"][i], df_test["Dec"][i]
            ]

        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
                
            # create a cursor
            cur = conn.cursor()
                
            # execute a statement
            cur.execute('SELECT version()')
            
            # commit the changes
            conn.commit()
            df = df.sort_values(by=['Annee', 'Mois', 'Jour'])
            df.reset_index(inplace=True, drop=True)
            print("#######")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
    total = time.time() - start_time
    print(total)
    return HttpResponse(df.to_json(orient='records'))