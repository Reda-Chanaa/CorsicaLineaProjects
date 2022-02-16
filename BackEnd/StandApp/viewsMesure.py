from optparse import Values
import time
from django.http import HttpResponse
import pandas as pd
import numpy as np
from datetime import date
from pymongo import MongoClient
from datetime import datetime

from django.http import HttpResponse

# REFERENCE DATABASE CONNECTION

client = MongoClient('localhost', 27017)

# Nom de la base = Reporting

db = client['Mesure']
mesure = db['MesureCSC']


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
            
            if datetime.now().month<=9:
                date=str(datetime.now().day)+'/0'+ str(datetime.now().month) +'/'+str(datetime.now().year)
            else:
                date=str(datetime.now().day)+'/'+ str(datetime.now().month) +'/'+str(datetime.now().year)
            
            z = mesure.count_documents({
                'Annee Report': str(datetime.now().year),
                'Date': date
            })

            if (z == 0):
                mesure.insert_one({
                    "Annee Report": str(datetime.now().year),
                    "Date": date,
                    "Annee": str(datetime.now().year),
                    "Mois": str(datetime.now().month),
                    "Jour": str(datetime.now().day),
                    'Jan': str(df_report.ECART[0]),
                    'Feb': str(df_report.ECART[1]),
                    'Mar': str(df_report.ECART[2]),
                    'Apr': str(df_report.ECART[3]),
                    'May': str(df_report.ECART[4]),
                    'Jun': str(df_report.ECART[5]),
                    'Jul': str(df_report.ECART[6]),
                    'Aug': str(df_report.ECART[7]),
                    'Sep': str(df_report.ECART[8]),
                    'Oct': str(df_report.ECART[9]),
                    'Nov': str(df_report.ECART[10]),
                    'Dec': str(df_report.ECART[11])
                }),
        print(df_test)
        if str(datetime.now().year+1) in df_test["YEAR"].values:
            df_report = pd.pivot_table(df_test[(df_test.YEAR == str(
                datetime.now().year+1))],
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
            
            if datetime.now().month<=9:
                date=str(datetime.now().day)+'/0'+ str(datetime.now().month) +'/'+str(datetime.now().year)
            else:
                date=str(datetime.now().day)+'/'+ str(datetime.now().month) +'/'+str(datetime.now().year)
            
            z = mesure.count_documents({
                'Annee Report': str(datetime.now().year+1),
                'Date': date
            })

            if (z == 0):
                mesure.insert_one({
                    "Annee Report": str(datetime.now().year+1),
                    "Date": date,
                    "Annee": str(datetime.now().year),
                    "Mois": str(datetime.now().month),
                    "Jour": str(datetime.now().day),
                    'Jan': str(df_report.ECART[0]),
                    'Feb': str(df_report.ECART[1]),
                    'Mar': str(df_report.ECART[2]),
                    'Apr': str(df_report.ECART[3]),
                    'May': str(df_report.ECART[4]),
                    'Jun': str(df_report.ECART[5]),
                    'Jul': str(df_report.ECART[6]),
                    'Aug': str(df_report.ECART[7]),
                    'Sep': str(df_report.ECART[8]),
                    'Oct': str(df_report.ECART[9]),
                    'Nov': str(df_report.ECART[10]),
                    'Dec': str(df_report.ECART[11])
                }),
    total = time.time() - start_time
    print(total)
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
        data = mesure.find({'Annee Report': str(annee)})
        nbr = mesure.count_documents({'Annee Report': str(annee)})
        for i in range(nbr):
            df.loc[i] = [
                data[i]["Annee Report"], data[i]["Date"], data[i]["Annee"],
                data[i]["Mois"], data[i]["Jour"], data[i]["Jan"],
                data[i]["Feb"], data[i]["Mar"], data[i]["Apr"], data[i]["May"],
                data[i]["Jun"], data[i]["Jul"], data[i]["Aug"], data[i]["Sep"],
                data[i]["Oct"], data[i]["Nov"], data[i]["Dec"]
            ]
        df = df.sort_values(by=['Annee','Mois','Jour'])
        df.reset_index(inplace=True,drop=True)
        print(df)
    total = time.time() - start_time
    print(total)
    return HttpResponse(df.to_json(orient='records'))