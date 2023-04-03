import calendar
from colorsys import hsv_to_rgb
import numpy as np
import pandas as pd
from pathlib import Path
from django.http import HttpResponse

import psycopg2
from StandApp.models import ReportingCorse
from config import config

""" Connect to the PostgreSQL database server """
conn = None
cur = None
try:
    # read connection parameters
    params = config()

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)

    # create a cursor
    cur = conn.cursor()

    # execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)

except (Exception, psycopg2.DatabaseError) as error:
    print(error)


def Stat_CSC(data_yesterday, data_today, annee, mois, cible, budget):
    table_reseau_armateur_today = pd.pivot_table(
        data_today[(data_today.RESEAU == "CORSE")
                   & (data_today.ARMATEUR == "CL") &
                   (data_today.COM == "COURANT") &
                   (data_today.ANNEE.eq(int(annee)))],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_today[
        "ID"] = table_reseau_armateur_today.ANNEE + table_reseau_armateur_today.MOIS
    table_reseau_armateur_today.reset_index(inplace=True)
    print(table_reseau_armateur_today)

    table_reseau_armateur_yesterday = pd.pivot_table(
        data_yesterday[(data_yesterday.RESEAU == "CORSE")
                       & (data_yesterday.ARMATEUR == "CL") &
                       (data_yesterday.COM == "COURANT") &
                       (data_yesterday.ANNEE.eq(int(annee)))],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    table_reseau_armateur_yesterday[
        "ID"] = table_reseau_armateur_yesterday.ANNEE + table_reseau_armateur_yesterday.MOIS
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    print(table_reseau_armateur_yesterday)

    for i in range(len(table_reseau_armateur_today)):
        if table_reseau_armateur_today["ID"][
                i] not in table_reseau_armateur_yesterday["ID"].values:
            table_reseau_armateur_yesterday = table_reseau_armateur_yesterday.append(
                {
                    "ID": table_reseau_armateur_today["ID"][i],
                    'ANNEE': table_reseau_armateur_today['ANNEE'][i],
                    'MOIS': table_reseau_armateur_today['MOIS'][i],
                    'PAX': 0,
                },
                ignore_index=True)
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    print(table_reseau_armateur_yesterday)
    df = pd.DataFrame()
    df["ANNEE"] = table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"] = table_reseau_armateur_yesterday['MOIS']
    df["CUMUL-18"] = table_reseau_armateur_yesterday['PAX']
    df["CUMUL-19"] = table_reseau_armateur_today['PAX']
    df['Vente journalière'] = table_reseau_armateur_today[
        'PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask = df[df.ANNEE.eq(int(annee))]
    df_mask = df_mask[df_mask.ANNEE.eq(int(annee))]
    print("tes test tyest")
    print("df", df)
    if 1 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 1,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 2 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 2,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 3 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 3,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 4 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 4,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 5 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 5,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 6 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 6,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 7 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 7,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 8 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 8,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 9 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 9,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 10 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 10,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 11 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 11,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 12 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 12,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    df_mask = df_mask.sort_values(by=['MOIS'])
    df_mask = df_mask.reset_index(drop=True)

    if len(mois) == 1:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])]
    if len(mois) == 2:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])]
    if len(mois) == 3:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])]
    if len(mois) == 4:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])]
    if len(mois) == 5:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])]
    if len(mois) == 6:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])]
    if len(mois) == 7:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])]
    if len(mois) == 8:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])]
    if len(mois) == 9:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])]
    if len(mois) == 10:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])
                                | df_mask.MOIS.eq(mois[9])]
    if len(mois) == 11:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])
                                | df_mask.MOIS.eq(mois[9])
                                | df_mask.MOIS.eq(mois[10])]
    if len(mois) == 12:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])
                                | df_mask.MOIS.eq(mois[9])
                                | df_mask.MOIS.eq(mois[10])
                                | df_mask.MOIS.eq(mois[11])]
    if len(df_mask_cumul) == 0:
        return pd.DataFrame()
    '''
    print("////////////////")
    cumul_j_1=df_mask["CUMUL-19"].sum()
    basseS1=df_mask.loc[(df_mask["MOIS"]==1) | (df_mask["MOIS"]==2) | (df_mask["MOIS"]==3)]
    bs11=basseS1["CUMUL-19"].sum()
    print(bs11)
    moyS1=df_mask.loc[(df_mask["MOIS"]==4) | (df_mask["MOIS"]==5) | (df_mask["MOIS"]==6)]
    ms11=moyS1["CUMUL-19"].sum()
    print(ms11)
    hauteS=df_mask.loc[(df_mask["MOIS"]==7) | (df_mask["MOIS"]==8)]
    hs1=hauteS["CUMUL-19"].sum()
    print(hs1)
    moyS2=df_mask.loc[(df_mask["MOIS"]==9) | (df_mask["MOIS"]==10)]
    ms22=moyS2["CUMUL-19"].sum()
    print(ms22)
    basseS2=df_mask.loc[(df_mask["MOIS"]==11) | (df_mask["MOIS"]==12)]
    bs22=basseS2["CUMUL-19"].sum()
    print(bs22)
    print(cumul_j_1)'''
    print("-------------------------")
    if len(df_mask_cumul) == 0:
        return pd.DataFrame()
    print("-------------------------")
    if len(df_mask_cumul) == 1:
        df_mask_cumul['BUDGET'] = budget[0]
    if len(df_mask_cumul) == 2:
        df_mask_cumul['BUDGET'] = [budget[0], budget[1]]
    if len(df_mask_cumul) == 3:
        df_mask_cumul['BUDGET'] = [budget[0], budget[1], budget[2]]
    if len(df_mask_cumul) == 4:
        df_mask_cumul['BUDGET'] = [budget[0], budget[1], budget[2], budget[3]]
    if len(df_mask_cumul) == 5:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4]
        ]
    if len(df_mask_cumul) == 6:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5]
        ]
    if len(df_mask_cumul) == 7:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6]
        ]
    if len(df_mask_cumul) == 8:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7]
        ]
    if len(df_mask_cumul) == 9:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7], budget[8]
        ]
    if len(df_mask_cumul) == 10:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7], budget[8], budget[9]
        ]
    if len(df_mask_cumul) == 11:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7], budget[8], budget[9], budget[10]
        ]
    if len(df_mask_cumul) == 12:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7], budget[8], budget[9], budget[10], budget[11]
        ]
    mesure = pd.DataFrame()
    mesure["CORSE"] = df_mask_cumul['MOIS'].apply(
        lambda x: calendar.month_abbr[int(x)])
    print(mesure)
    '''print("df", df_mask_cumul)
    print("mesure", mesure)
    print(len(mesure))
    print(cible)'''
    if len(mesure) == 1:
        mesure['CIBLE'] = cible[0]
    if len(mesure) == 2:
        mesure['CIBLE'] = [cible[0], cible[1]]
    if len(mesure) == 3:
        mesure['CIBLE'] = [cible[0], cible[1], cible[2]]
    if len(mesure) == 4:
        mesure['CIBLE'] = [cible[0], cible[1], cible[2], cible[3]]
    if len(mesure) == 5:
        mesure['CIBLE'] = [cible[0], cible[1], cible[2], cible[3], cible[4]]
    if len(mesure) == 6:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5]
        ]
    if len(mesure) == 7:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6]
        ]
    if len(mesure) == 8:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7]
        ]
    if len(mesure) == 9:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7], cible[8]
        ]
    if len(mesure) == 10:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7], cible[8], cible[9]
        ]
    if len(mesure) == 11:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7], cible[8], cible[9], cible[10]
        ]
    if len(mesure) == 12:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7], cible[8], cible[9], cible[10], cible[11]
        ]
    mesure["VENTE"] = df_mask_cumul['Vente journalière']
    mesure["CUMUL"] = df_mask_cumul['CUMUL-19']
    mesure["BUD"] = df_mask_cumul['BUDGET']
    mesure["BUDGET"] = round(
        (df_mask_cumul['CUMUL-19'] / df_mask_cumul['BUDGET']) * 100)
    BS1 = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    MS1 = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    HS = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    MS2 = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    BS2 = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    print("-------------------------------")
    print(mesure)
    mesure = mesure.fillna(0)
    bud = 0
    for i in mesure.index:
        bud += mesure["BUD"][i]
    print(bud)
    for i in mesure.index:
        #  1 BS
        if mesure["CORSE"][i] == "Jan":
            BS1.loc[0] = [
                "Janvier", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
        if mesure["CORSE"][i] == "Feb":
            BS1.loc[1] = [
                "Février", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
        if mesure["CORSE"][i] == "Mar":
            BS1.loc[2] = [
                "Mars", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
            if len(BS1) == 3:
                BS1.loc[3] = [
                    "BASSE SAISON 1",
                    BS1["CIBLE"][0] + BS1["CIBLE"][1] + BS1["CIBLE"][2],
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    round((
                        (BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2]) /
                        (mesure["BUD"][i - 2] + mesure["BUD"][i - 1] +
                         mesure["BUD"][i])) * 100)
                ]
            elif len(BS1) == 2:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["CIBLE"][1] + BS1["CIBLE"][2],
                    BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    round(((BS1["CUMUL"][1] + BS1["CUMUL"][2]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["CIBLE"][2], BS1["VENTE"][2],
                    BS1["CUMUL"][2], BS1["BUDGET"][2]
                ]
        #  1 MS
        if mesure["CORSE"][i] == "Apr":
            MS1.loc[0] = [
                "Avril", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
        if mesure["CORSE"][i] == "May":
            MS1.loc[1] = [
                "Mai", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
        if mesure["CORSE"][i] == "Jun":
            MS1.loc[2] = [
                "juin", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
            if len(MS1) == 3:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1",
                    MS1["CIBLE"][0] + MS1["CIBLE"][1] + MS1["CIBLE"][2],
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    round((
                        (MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2]) /
                        (mesure["BUD"][i - 2] + mesure["BUD"][i - 1] +
                         mesure["BUD"][i])) * 100)
                ]
            elif len(MS1) == 2:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["CIBLE"][1] + MS1["CIBLE"][2],
                    MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    round(((MS1["CUMUL"][1] + MS1["CUMUL"][2]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["CIBLE"][2], MS1["VENTE"][2],
                    MS1["CUMUL"][2], MS1["BUDGET"][2]
                ]
        #  HS
        if mesure["CORSE"][i] == "Jul":
            HS.loc[0] = [
                "Juillet", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
        if mesure["CORSE"][i] == "Aug":
            HS.loc[1] = [
                "Août", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
            if len(HS) == 2:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["CIBLE"][0] + HS["CIBLE"][1],
                    HS["VENTE"][0] + HS["VENTE"][1],
                    HS["CUMUL"][0] + HS["CUMUL"][1],
                    round(((HS["CUMUL"][0] + HS["CUMUL"][1]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["CIBLE"][1], HS["VENTE"][1],
                    HS["CUMUL"][1], HS["BUDGET"][1]
                ]
        #  2 MS
        if mesure["CORSE"][i] == "Sep":
            MS2.loc[0] = [
                "Septembre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
        if mesure["CORSE"][i] == "Oct":
            MS2.loc[1] = [
                "Octobre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
            if len(MS2) == 2:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["CIBLE"][0] + MS2["CIBLE"][1],
                    MS2["VENTE"][0] + MS2["VENTE"][1],
                    MS2["CUMUL"][0] + MS2["CUMUL"][1],
                    round(((MS2["CUMUL"][0] + MS2["CUMUL"][1]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["CIBLE"][1], MS2["VENTE"][1],
                    MS2["CUMUL"][1], MS2["BUDGET"][1]
                ]
        #  2 BS
        if mesure["CORSE"][i] == "Nov":
            BS2.loc[0] = [
                "Novembre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
        if mesure["CORSE"][i] == "Dec":
            BS2.loc[1] = [
                "Décembre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
            if len(BS2) == 2:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["CIBLE"][0] + BS2["CIBLE"][1],
                    BS2["VENTE"][0] + BS2["VENTE"][1],
                    BS2["CUMUL"][0] + BS2["CUMUL"][1],
                    round(((BS2["CUMUL"][0] + BS2["CUMUL"][1]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["CIBLE"][1], BS2["VENTE"][1],
                    BS2["CUMUL"][1], BS2["BUDGET"][1]
                ]
    '''print("BS1", len(BS1))
    print("BS2", len(BS2))
    print("HS", len(HS))
    print("MS1", len(MS1))
    print("MS2", len(MS2))'''
    MS1.reset_index(inplace=True)
    MS2.reset_index(inplace=True)
    HS.reset_index(inplace=True)
    BS1.reset_index(inplace=True)
    BS2.reset_index(inplace=True)
    if len(BS1)==0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = BS2
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS2, BS2])
                    else:
                        reporting = MS2
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([HS, MS2, BS2])
                    else:
                        reporting = pd.concat([HS, MS2])
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1,BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1, MS2, BS2])
                    else:
                        reporting = pd.concat([MS1,MS2])
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1,HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1,HS, MS2, BS2])
                    else:
                        reporting = pd.concat([MS1,HS, MS2])
    elif len(BS1)!=0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,MS2])
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,HS, MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,HS, MS2])
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1,BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1, MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,MS1,MS2])
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1,HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1,HS, MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,MS1,HS, MS2])
    print("reporting", reporting)
    reporting.reset_index(inplace=True)
    if len(BS1)==0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] +
                MS1["VENTE"][len(MS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1]+
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                       reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
    elif len(BS1)!=0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] +
                MS1["VENTE"][len(MS1) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1]+
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                       reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
    del reporting['index']

    for i in range(len(reporting) - 1):
        reporting["BUDGET"][i] = str(reporting["BUDGET"][i]) + '%'

    return reporting


def Stat_CSC_Objectif(data_yesterday, data_today, annee, mois, cible, budget,
                      objectif):
    table_reseau_armateur_today = pd.pivot_table(
        data_today[(data_today.RESEAU == "CORSE")
                   & (data_today.ARMATEUR == "CL") &
                   (data_today.COM == "COURANT") &
                   (data_today.ANNEE.eq(int(annee)))],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_today[
        "ID"] = table_reseau_armateur_today.ANNEE + table_reseau_armateur_today.MOIS
    table_reseau_armateur_today.reset_index(inplace=True)
    print(table_reseau_armateur_today)
    table_reseau_armateur_yesterday = pd.pivot_table(
        data_yesterday[(data_yesterday.RESEAU == "CORSE")
                       & (data_yesterday.ARMATEUR == "CL") &
                       (data_yesterday.COM == "COURANT") &
                       (data_yesterday.ANNEE.eq(int(annee)))],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    table_reseau_armateur_yesterday[
        "ID"] = table_reseau_armateur_yesterday.ANNEE + table_reseau_armateur_yesterday.MOIS
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    print(table_reseau_armateur_yesterday)

    for i in range(len(table_reseau_armateur_today)):
        if table_reseau_armateur_today["ID"][
                i] not in table_reseau_armateur_yesterday["ID"].values:
            table_reseau_armateur_yesterday = table_reseau_armateur_yesterday.append(
                {
                    "ID": table_reseau_armateur_today["ID"][i],
                    'ANNEE': table_reseau_armateur_today['ANNEE'][i],
                    'MOIS': table_reseau_armateur_today['MOIS'][i],
                    'PAX': 0,
                },
                ignore_index=True)
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    print(table_reseau_armateur_yesterday)
    df = pd.DataFrame()
    df["ANNEE"] = table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"] = table_reseau_armateur_yesterday['MOIS']
    df["CUMUL-18"] = table_reseau_armateur_yesterday['PAX']
    df["CUMUL-19"] = table_reseau_armateur_today['PAX']
    df['Vente journalière'] = table_reseau_armateur_today[
        'PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask = df[df.ANNEE.eq(int(annee))]
    df_mask = df_mask[df_mask.ANNEE.eq(int(annee))]
    if 1 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 1,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 2 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 2,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 3 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 3,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 4 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 4,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 5 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 5,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 6 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 6,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 7 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 7,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 8 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 8,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 9 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 9,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 10 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 10,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 11 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 11,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 12 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 12,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    df_mask = df_mask.sort_values(by=['MOIS'])
    df_mask = df_mask.reset_index(drop=True)
    if len(mois) == 1:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])]
    if len(mois) == 2:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])]
    if len(mois) == 3:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])]
    if len(mois) == 4:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])]
    if len(mois) == 5:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])]
    if len(mois) == 6:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])]
    if len(mois) == 7:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])]
    if len(mois) == 8:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])]
    if len(mois) == 9:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])]
    if len(mois) == 10:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])
                                | df_mask.MOIS.eq(mois[9])]
    if len(mois) == 11:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])
                                | df_mask.MOIS.eq(mois[9])
                                | df_mask.MOIS.eq(mois[10])]
    if len(mois) == 12:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])
                                | df_mask.MOIS.eq(mois[9])
                                | df_mask.MOIS.eq(mois[10])
                                | df_mask.MOIS.eq(mois[11])]
    print("////////////////")
    '''
    cumul_j_1=df_mask["CUMUL-19"].sum()
    basseS1=df_mask.loc[(df_mask["MOIS"]==1) | (df_mask["MOIS"]==2) | (df_mask["MOIS"]==3)]
    bs11=basseS1["CUMUL-19"].sum()
    print(bs11)
    moyS1=df_mask.loc[(df_mask["MOIS"]==4) | (df_mask["MOIS"]==5) | (df_mask["MOIS"]==6)]
    ms11=moyS1["CUMUL-19"].sum()
    print(ms11)
    hauteS=df_mask.loc[(df_mask["MOIS"]==7) | (df_mask["MOIS"]==8)]
    hs1=hauteS["CUMUL-19"].sum()
    print(hs1)
    moyS2=df_mask.loc[(df_mask["MOIS"]==9) | (df_mask["MOIS"]==10)]
    ms22=moyS2["CUMUL-19"].sum()
    print(ms22)
    basseS2=df_mask.loc[(df_mask["MOIS"]==11) | (df_mask["MOIS"]==12)]
    bs22=basseS2["CUMUL-19"].sum()
    print(bs22)
    print(cumul_j_1)
    '''
    if len(df_mask_cumul) == 0:
        return pd.DataFrame()
        print("-------------------------")
    if len(df_mask_cumul) == 1:
        df_mask_cumul['BUDGET'] = budget[0]
        df_mask_cumul['OBJECTIF'] = objectif[0]
    if len(df_mask_cumul) == 2:
        df_mask_cumul['BUDGET'] = [budget[0], budget[1]]
        df_mask_cumul['OBJECTIF'] = [objectif[0], objectif[1]]
    if len(df_mask_cumul) == 3:
        df_mask_cumul['BUDGET'] = [budget[0], budget[1], budget[2]]
        df_mask_cumul['OBJECTIF'] = [objectif[0], objectif[1], objectif[2]]
    if len(df_mask_cumul) == 4:
        df_mask_cumul['BUDGET'] = [budget[0], budget[1], budget[2], budget[3]]
        df_mask_cumul['OBJECTIF'] = [
            objectif[0], objectif[1], objectif[2], objectif[3]
        ]
    if len(df_mask_cumul) == 5:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4]
        ]
        df_mask_cumul['OBJECTIF'] = [
            objectif[0], objectif[1], objectif[2], objectif[3], objectif[4]
        ]
    if len(df_mask_cumul) == 6:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5]
        ]
        df_mask_cumul['OBJECTIF'] = [
            objectif[0], objectif[1], objectif[2], objectif[3], objectif[4],
            objectif[5]
        ]
    if len(df_mask_cumul) == 7:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6]
        ]
        df_mask_cumul['OBJECTIF'] = [
            objectif[0], objectif[1], objectif[2], objectif[3], objectif[4],
            objectif[5], objectif[6]
        ]
    if len(df_mask_cumul) == 8:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7]
        ]
        df_mask_cumul['OBJECTIF'] = [
            objectif[0], objectif[1], objectif[2], objectif[3], objectif[4],
            objectif[5], objectif[6], objectif[7]
        ]
    if len(df_mask_cumul) == 9:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7], budget[8]
        ]
        df_mask_cumul['OBJECTIF'] = [
            objectif[0], objectif[1], objectif[2], objectif[3], objectif[4],
            objectif[5], objectif[6], objectif[7], objectif[8]
        ]
    if len(df_mask_cumul) == 10:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7], budget[8], budget[9]
        ]
        df_mask_cumul['OBJECTIF'] = [
            objectif[0], objectif[1], objectif[2], objectif[3], objectif[4],
            objectif[5], objectif[6], objectif[7], objectif[8], objectif[9]
        ]
    if len(df_mask_cumul) == 11:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7], budget[8], budget[9], budget[10]
        ]
        df_mask_cumul['OBJECTIF'] = [
            objectif[0], objectif[1], objectif[2], objectif[3], objectif[4],
            objectif[5], objectif[6], objectif[7], objectif[8], objectif[9],
            objectif[10]
        ]
    if len(df_mask_cumul) == 12:
        df_mask_cumul['BUDGET'] = [
            budget[0], budget[1], budget[2], budget[3], budget[4], budget[5],
            budget[6], budget[7], budget[8], budget[9], budget[10], budget[11]
        ]
        df_mask_cumul['OBJECTIF'] = [
            objectif[0], objectif[1], objectif[2], objectif[3], objectif[4],
            objectif[5], objectif[6], objectif[7], objectif[8], objectif[9],
            objectif[10], objectif[11]
        ]
    mesure = pd.DataFrame()
    mesure["CORSE"] = df_mask_cumul['MOIS'].apply(
        lambda x: calendar.month_abbr[int(x)])
    '''print("df", df_mask_cumul)
    print("mesure", mesure)
    print(len(mesure))
    print(cible)'''
    if len(mesure) == 1:
        mesure['CIBLE'] = cible[0]
    if len(mesure) == 2:
        mesure['CIBLE'] = [cible[0], cible[1]]
    if len(mesure) == 3:
        mesure['CIBLE'] = [cible[0], cible[1], cible[2]]
    if len(mesure) == 4:
        mesure['CIBLE'] = [cible[0], cible[1], cible[2], cible[3]]
    if len(mesure) == 5:
        mesure['CIBLE'] = [cible[0], cible[1], cible[2], cible[3], cible[4]]
    if len(mesure) == 6:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5]
        ]
    if len(mesure) == 7:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6]
        ]
    if len(mesure) == 8:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7]
        ]
    if len(mesure) == 9:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7], cible[8]
        ]
    if len(mesure) == 10:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7], cible[8], cible[9]
        ]
    if len(mesure) == 11:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7], cible[8], cible[9], cible[10]
        ]
    if len(mesure) == 12:
        mesure['CIBLE'] = [
            cible[0], cible[1], cible[2], cible[3], cible[4], cible[5],
            cible[6], cible[7], cible[8], cible[9], cible[10], cible[11]
        ]
    mesure["VENTE"] = df_mask_cumul['Vente journalière']
    mesure["CUMUL"] = df_mask_cumul['CUMUL-19']
    mesure["BUD"] = df_mask_cumul['BUDGET']
    mesure["BUDGET"] = round(
        (df_mask_cumul['CUMUL-19'] / df_mask_cumul['BUDGET']) * 100)
    mesure["OBJECTIF"] = df_mask_cumul['OBJECTIF']
    print("- - - - - - - - - - -", mesure)
    BS1 = pd.DataFrame(
        columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET", "OBJECTIF"])
    MS1 = pd.DataFrame(
        columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET", "OBJECTIF"])
    HS = pd.DataFrame(
        columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET", "OBJECTIF"])
    MS2 = pd.DataFrame(
        columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET", "OBJECTIF"])
    BS2 = pd.DataFrame(
        columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET", "OBJECTIF"])
    print("-------------------------------")
    print(mesure)
    mesure = mesure.fillna(0)
    bud = 0
    for i in mesure.index:
        bud += mesure["BUD"][i]
    print(bud)
    mesure.reset_index(drop=True)
    for i in mesure.index:
        #  1 BS
        if mesure["CORSE"][i] == "Jan":
            BS1.loc[0] = [
                "Janvier", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
        if mesure["CORSE"][i] == "Feb":
            BS1.loc[1] = [
                "Février", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
        if mesure["CORSE"][i] == "Mar":
            BS1.loc[2] = [
                "Mars", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
            if len(BS1) == 3:
                BS1.loc[3] = [
                    "BASSE SAISON 1",
                    BS1["CIBLE"][0] + BS1["CIBLE"][1] + BS1["CIBLE"][2],
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    round((
                        (BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2]) /
                        (mesure["BUD"][i - 2] + mesure["BUD"][i - 1] +
                         mesure["BUD"][i])) * 100),
                    round((BS1["OBJECTIF"][0] + BS1["OBJECTIF"][1] +
                           BS1["OBJECTIF"][2]) / 3)
                ]
            elif len(BS1) == 2:
                if (mesure["BUD"][i - 1] == 0 & mesure["BUD"][i] == 0) | (
                        BS1["OBJECTIF"][1] == 0 & BS1["OBJECTIF"][2] == 0):
                    BS1.loc[3] = [
                        "BASSE SAISON 1", BS1["CIBLE"][1] + BS1["CIBLE"][2],
                        BS1["VENTE"][1] + BS1["VENTE"][2],
                        BS1["CUMUL"][1] + BS1["CUMUL"][2],
                        round(
                            ((BS1["CUMUL"][1] + BS1["CUMUL"][2]) /
                             (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100),
                        round((BS1["OBJECTIF"][1] + BS1["OBJECTIF"][2]) / 2)
                    ]
                else:
                    BS1.loc[3] = [
                        "BASSE SAISON 1", BS1["CIBLE"][1] + BS1["CIBLE"][2],
                        BS1["VENTE"][1] + BS1["VENTE"][2],
                        BS1["CUMUL"][1] + BS1["CUMUL"][2],
                        round(
                            ((BS1["CUMUL"][1] + BS1["CUMUL"][2]) /
                             (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100),
                        round((BS1["OBJECTIF"][1] + BS1["OBJECTIF"][2]) / 2)
                    ]
            else:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["CIBLE"][2], BS1["VENTE"][2],
                    BS1["CUMUL"][2], BS1["BUDGET"][2], BS1["OBJECTIF"][2]
                ]
        #  1 MS
        if mesure["CORSE"][i] == "Apr":
            MS1.loc[0] = [
                "Avril", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
        if mesure["CORSE"][i] == "May":
            MS1.loc[1] = [
                "Mai", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
        if mesure["CORSE"][i] == "Jun":
            MS1.loc[2] = [
                "juin", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
            if len(MS1) == 3:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1",
                    MS1["CIBLE"][0] + MS1["CIBLE"][1] + MS1["CIBLE"][2],
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    round((
                        (MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2]) /
                        (mesure["BUD"][i - 2] + mesure["BUD"][i - 1] +
                         mesure["BUD"][i])) * 100),
                    round((MS1["OBJECTIF"][0] + MS1["OBJECTIF"][1] +
                           MS1["OBJECTIF"][2]) / 3)
                ]
            elif len(MS1) == 2:
                if (mesure["BUD"][i - 1] == 0 & mesure["BUD"][i] == 0) | (
                        MS1["OBJECTIF"][1] == 0 & MS1["OBJECTIF"][2] == 0):
                    MS1.loc[3] = [
                        "MOYENNE SAISON 1", MS1["CIBLE"][1] + MS1["CIBLE"][2],
                        MS1["VENTE"][1] + MS1["VENTE"][2],
                        MS1["CUMUL"][1] + MS1["CUMUL"][2], 0, 0
                    ]
                else:
                    MS1.loc[3] = [
                        "MOYENNE SAISON 1", MS1["CIBLE"][1] + MS1["CIBLE"][2],
                        MS1["VENTE"][1] + MS1["VENTE"][2],
                        MS1["CUMUL"][1] + MS1["CUMUL"][2],
                        round(
                            ((MS1["CUMUL"][1] + MS1["CUMUL"][2]) /
                             (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100),
                        round((MS1["OBJECTIF"][1] + MS1["OBJECTIF"][2]) / 2)
                    ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["CIBLE"][2], MS1["VENTE"][2],
                    MS1["CUMUL"][1] + MS1["CUMUL"][2], MS1["BUDGET"][2],
                    MS1["OBJECTIF"][2]
                ]
        #  HS
        if mesure["CORSE"][i] == "Jul":
            HS.loc[0] = [
                "Juillet", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
        if mesure["CORSE"][i] == "Aug":
            HS.loc[1] = [
                "Août", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
            if len(HS) == 2:
                if (mesure["BUD"][i - 1] == 0 & mesure["BUD"][i] ==
                        0) | (HS["OBJECTIF"][0] == 0 & HS["OBJECTIF"][1] == 0):
                    HS.loc[2] = [
                        "HAUTE SAISON", HS["CIBLE"][0] + HS["CIBLE"][1],
                        HS["VENTE"][0] + HS["VENTE"][1],
                        HS["CUMUL"][0] + HS["CUMUL"][1], 0, 0
                    ]
                else:
                    HS.loc[2] = [
                        "HAUTE SAISON", HS["CIBLE"][0] + HS["CIBLE"][1],
                        HS["VENTE"][0] + HS["VENTE"][1],
                        HS["CUMUL"][0] + HS["CUMUL"][1],
                        round(
                            ((HS["CUMUL"][0] + HS["CUMUL"][1]) /
                             (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100),
                        round((HS["OBJECTIF"][0] + HS["OBJECTIF"][1]) / 2)
                    ]
            else:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["CIBLE"][1], HS["VENTE"][1],
                    HS["CUMUL"][1], HS["BUDGET"][1], HS["OBJECTIF"][1]
                ]
        #  2 MS
        if mesure["CORSE"][i] == "Sep":
            MS2.loc[0] = [
                "Septembre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
        if mesure["CORSE"][i] == "Oct":
            MS2.loc[1] = [
                "Octobre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
            if len(MS2) == 2:
                if (mesure["BUD"][i - 1] == 0 & mesure["BUD"][i] == 0) | (
                        MS2["OBJECTIF"][0] == 0 & MS2["OBJECTIF"][1] == 0):
                    MS2.loc[2] = [
                        "MOYENNE SAISON 2", MS2["CIBLE"][0] + MS2["CIBLE"][1],
                        MS2["VENTE"][0] + MS2["VENTE"][1],
                        MS2["CUMUL"][0] + MS2["CUMUL"][1], 0, 0
                    ]
                else:
                    MS2.loc[2] = [
                        "MOYENNE SAISON 2", MS2["CIBLE"][0] + MS2["CIBLE"][1],
                        MS2["VENTE"][0] + MS2["VENTE"][1],
                        MS2["CUMUL"][0] + MS2["CUMUL"][1],
                        round(
                            ((MS2["CUMUL"][0] + MS2["CUMUL"][1]) /
                             (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100),
                        round((MS2["OBJECTIF"][0] + MS2["OBJECTIF"][1]) / 2)
                    ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["CIBLE"][1], MS2["VENTE"][1],
                    MS2["CUMUL"][1], MS2["BUDGET"][1], MS2["OBJECTIF"][1]
                ]
        #  2 BS
        if mesure["CORSE"][i] == "Nov":
            BS2.loc[0] = [
                "Novembre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
            '''
            if mesure["CORSE"][i + 1] != "Dec":
                if len(BS2) == 1:
                    BS2.loc[1] = [
                        "BASSE SAISON 2", BS2["CIBLE"][0], BS2["VENTE"][0],
                        BS2["CUMUL"][0], BS2["BUDGET"][0], BS2["OBJECTIF"][0]
                    ]'''
        if mesure["CORSE"][i] == "Dec":
            BS2.loc[1] = [
                "Décembre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i], mesure["OBJECTIF"][i]
            ]
            if len(BS2) == 2:
                if (mesure["BUD"][i - 1] == 0 & mesure["BUD"][i] == 0) | (
                        BS2["OBJECTIF"][0] == 0 & BS2["OBJECTIF"][1] == 0):
                    BS2.loc[2] = [
                        "BASSE SAISON 2", BS2["CIBLE"][0] + BS2["CIBLE"][1],
                        BS2["VENTE"][0] + BS2["VENTE"][1],
                        BS2["CUMUL"][0] + BS2["CUMUL"][1], 0, 0
                    ]
                else:
                    BS2.loc[2] = [
                        "BASSE SAISON 2", BS2["CIBLE"][0] + BS2["CIBLE"][1],
                        BS2["VENTE"][0] + BS2["VENTE"][1],
                        BS2["CUMUL"][0] + BS2["CUMUL"][1],
                        round(
                            ((BS2["CUMUL"][0] + BS2["CUMUL"][1]) /
                             (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100),
                        round((BS2["OBJECTIF"][0] + BS2["OBJECTIF"][1]) / 2)
                    ]
            else:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["CIBLE"][1], BS2["VENTE"][1],
                    BS2["CUMUL"][1], BS2["BUDGET"][1], BS2["OBJECTIF"][1]
                ]

    MS1.reset_index(inplace=True)
    MS2.reset_index(inplace=True)
    HS.reset_index(inplace=True)
    BS1.reset_index(inplace=True)
    BS2.reset_index(inplace=True)
    if len(BS1)==0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = BS2
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS2, BS2])
                    else:
                        reporting = MS2
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([HS, MS2, BS2])
                    else:
                        reporting = pd.concat([HS, MS2])
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1,BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1, MS2, BS2])
                    else:
                        reporting = pd.concat([MS1,MS2])
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1,HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1,HS, MS2, BS2])
                    else:
                        reporting = pd.concat([MS1,HS, MS2])
    elif len(BS1)!=0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,MS2])
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,HS, MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,HS, MS2])
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1,BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1, MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,MS1,MS2])
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1,HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1,HS, MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,MS1,HS, MS2])
    print("reporting", reporting)
    reporting.reset_index(inplace=True)
    
    if len(BS1)==0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] +
                MS1["VENTE"][len(MS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1]+
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                       reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
    elif len(BS1)!=0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] +
                MS1["VENTE"][len(MS1) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1]+
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                       reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)

    del reporting['index']
    
    for i in range(len(reporting) - 1):
        reporting["BUDGET"][i] = str(reporting["BUDGET"][i]) + '%'
        reporting["OBJECTIF"][i] = str(reporting["OBJECTIF"][i]) + '%'

    return reporting


def Stat_CSC_plus(data_yesterday, data_today, annee, mois):
    table_reseau_armateur_today = pd.pivot_table(
        data_today[(data_today.RESEAU == "CORSE")
                   & (data_today.ARMATEUR == "CL") &
                   (data_today.COM == "COURANT") &
                   (data_today.ANNEE.eq(int(annee)))],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_today[
        "ID"] = table_reseau_armateur_today.ANNEE + table_reseau_armateur_today.MOIS
    table_reseau_armateur_today.reset_index(inplace=True)
    print(table_reseau_armateur_today)
    table_reseau_armateur_yesterday = pd.pivot_table(
        data_yesterday[(data_yesterday.RESEAU == "CORSE")
                       & (data_yesterday.ARMATEUR == "CL") &
                       (data_yesterday.COM == "COURANT") &
                       (data_yesterday.ANNEE.eq(int(annee)))],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    table_reseau_armateur_yesterday[
        "ID"] = table_reseau_armateur_yesterday.ANNEE + table_reseau_armateur_yesterday.MOIS
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    print(table_reseau_armateur_yesterday)

    for i in range(len(table_reseau_armateur_today)):
        if table_reseau_armateur_today["ID"][
                i] not in table_reseau_armateur_yesterday["ID"].values:
            table_reseau_armateur_yesterday = table_reseau_armateur_yesterday.append(
                {
                    "ID": table_reseau_armateur_today["ID"][i],
                    'ANNEE': table_reseau_armateur_today['ANNEE'][i],
                    'MOIS': table_reseau_armateur_today['MOIS'][i],
                    'PAX': 0,
                },
                ignore_index=True)
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    print(table_reseau_armateur_yesterday)
    df = pd.DataFrame()
    df["ANNEE"] = table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"] = table_reseau_armateur_yesterday['MOIS']
    df["CUMUL-18"] = table_reseau_armateur_yesterday['PAX']
    df["CUMUL-19"] = table_reseau_armateur_today['PAX']
    df['Vente journalière'] = table_reseau_armateur_today[
        'PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask = df[df.ANNEE.eq(int(annee))]
    df_mask = df_mask[df_mask.ANNEE.eq(int(annee))]
    if 1 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 1,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 2 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 2,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 3 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 3,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 4 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 4,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 5 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 5,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 6 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 6,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 7 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 7,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 8 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 8,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 9 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 9,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 10 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 10,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 11 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 11,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    if 12 not in df_mask.MOIS.values:
        df_mask = df_mask.append(
            {
                'ANNEE': int(annee),
                'MOIS': 12,
                'CUMUL N-1': 0,
                'CUMUL': 0,
                'VENTE': 0
            },
            ignore_index=True)
    df_mask = df_mask.sort_values(by=['MOIS'])
    df_mask = df_mask.reset_index(drop=True)
    if len(mois) == 1:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])]
    if len(mois) == 2:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])]
    if len(mois) == 3:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])]
    if len(mois) == 4:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])]
    if len(mois) == 5:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])]
    if len(mois) == 6:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])]
    if len(mois) == 7:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])]
    if len(mois) == 8:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])]
    if len(mois) == 9:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])]
    if len(mois) == 10:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])
                                | df_mask.MOIS.eq(mois[9])]
    if len(mois) == 11:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])
                                | df_mask.MOIS.eq(mois[9])
                                | df_mask.MOIS.eq(mois[10])]
    if len(mois) == 12:
        df_mask_cumul = df_mask[df_mask.MOIS.eq(mois[0])
                                | df_mask.MOIS.eq(mois[1])
                                | df_mask.MOIS.eq(mois[2])
                                | df_mask.MOIS.eq(mois[3])
                                | df_mask.MOIS.eq(mois[4])
                                | df_mask.MOIS.eq(mois[5])
                                | df_mask.MOIS.eq(mois[6])
                                | df_mask.MOIS.eq(mois[7])
                                | df_mask.MOIS.eq(mois[8])
                                | df_mask.MOIS.eq(mois[9])
                                | df_mask.MOIS.eq(mois[10])
                                | df_mask.MOIS.eq(mois[11])]
    print("////////////////")
    if len(df_mask_cumul) == 0:
        print("-------------------------")
        return pd.DataFrame()
    mesure = pd.DataFrame()
    mesure["CORSE"] = df_mask_cumul['MOIS'].apply(
        lambda x: calendar.month_abbr[int(x)])
    mesure["VENTE"] = df_mask_cumul['Vente journalière']
    mesure["CUMUL"] = df_mask_cumul['CUMUL-19']
    print("- - - - - -", mesure)
    BS1 = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    MS1 = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    HS = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    MS2 = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    BS2 = pd.DataFrame(columns=['CORSE', 'CIBLE', 'VENTE', "CUMUL", "BUDGET"])
    mesure = mesure.fillna(0)
    mesure.reset_index(drop=True)
    for i in mesure.index:
        #  1 BS
        if mesure["CORSE"][i] == "Jan":
            BS1.loc[0] = [
                "Janvier", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        if mesure["CORSE"][i] == "Feb":
            BS1.loc[1] = [
                "Février", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        if mesure["CORSE"][i] == "Mar":
            BS1.loc[2] = [
                "Mars", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
            if len(BS1) == 3:
                BS1.loc[3] = [
                    "BASSE SAISON 1", "",
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2], bs11,
                    ""
                ]
            elif len(BS1) == 2:
                BS1.loc[3] = [
                    "BASSE SAISON 1", "", BS1["VENTE"][1] + BS1["VENTE"][2],
                    bs11, ""
                ]
            else:
                BS1.loc[3] = ["BASSE SAISON 1", "", BS1["VENTE"][2], bs11, ""]
        #  1 MS
        if mesure["CORSE"][i] == "Apr":
            MS1.loc[0] = [
                "Avril", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        if mesure["CORSE"][i] == "May":
            MS1.loc[1] = [
                "Mai", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        if mesure["CORSE"][i] == "Jun":
            MS1.loc[2] = [
                "juin", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
            if len(MS1) == 3:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", "",
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2], ms11,
                    ""
                ]
            elif len(MS1) == 2:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", "", MS1["VENTE"][1] + MS1["VENTE"][2],
                    ms11, ""
                ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", "", MS1["VENTE"][2], ms11, ""
                ]
        #  HS
        if mesure["CORSE"][i] == "Jul":
            HS.loc[0] = [
                "Juillet", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        if mesure["CORSE"][i] == "Aug":
            HS.loc[1] = [
                "Août", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
            if len(HS) == 2:
                HS.loc[2] = [
                    "HAUTE SAISON", "", HS["VENTE"][0] + HS["VENTE"][1], hs1,
                    ""
                ]
            else:
                HS.loc[2] = ["HAUTE SAISON", "", HS["VENTE"][1], hs1, ""]
        #  2 MS
        if mesure["CORSE"][i] == "Sep":
            MS2.loc[0] = [
                "Septembre", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        if mesure["CORSE"][i] == "Oct":
            MS2.loc[1] = [
                "Octobre", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
            if len(MS2) == 2:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", "", MS2["VENTE"][0] + MS2["VENTE"][1],
                    ms22, ""
                ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", "", MS2["VENTE"][1], ms22, ""
                ]
        #  2 BS
        if mesure["CORSE"][i] == "Nov":
            BS2.loc[0] = [
                "Novembre", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        if mesure["CORSE"][i] == "Dec":
            BS2.loc[1] = [
                "Décembre", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
            if len(BS2) == 2:
                BS2.loc[2] = [
                    "BASSE SAISON 2", "", BS2["VENTE"][0] + BS2["VENTE"][1],
                    bs22, ""
                ]
            else:
                BS2.loc[2] = ["BASSE SAISON 2", "", BS2["VENTE"][1], bs22, ""]

    MS1.reset_index(inplace=True)
    MS2.reset_index(inplace=True)
    HS.reset_index(inplace=True)
    BS1.reset_index(inplace=True)
    BS2.reset_index(inplace=True)

    if len(BS1)==0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = BS2
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS2, BS2])
                    else:
                        reporting = MS2
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([HS, MS2, BS2])
                    else:
                        reporting = pd.concat([HS, MS2])
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1,BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1, MS2, BS2])
                    else:
                        reporting = pd.concat([MS1,MS2])
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1,HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([MS1,HS, MS2, BS2])
                    else:
                        reporting = pd.concat([MS1,HS, MS2])
    elif len(BS1)!=0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,MS2])
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,HS, MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,HS, MS2])
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1,BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1, MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,MS1,MS2])
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1,HS, BS2])
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = pd.concat([BS1,MS1,HS, MS2, BS2])
                    else:
                        reporting = pd.concat([BS1,MS1,HS, MS2])

    print("reporting", reporting)
    reporting.reset_index(inplace=True)
    if len(BS1)==0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] +
                MS1["VENTE"][len(MS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1]+
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                       reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
    elif len(BS1)!=0:
       if(len(MS1))==0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
       if(len(MS1))!=0:
            if(len(HS))==0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] +
                MS1["VENTE"][len(MS1) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1]+
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1]+
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1]+
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                       reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
            elif(len(HS))!=0:
                if(len(MS2))==0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                elif(len(MS2))!=0:
                    if(len(BS2))!=0:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                BS2["CIBLE"][len(BS2) - 1] + HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                BS2["VENTE"][len(BS2) - 1] + HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                BS2["CUMUL"][len(BS2) - 1] + HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
                    else:
                        reporting = reporting.append(
            {
                'CORSE':
                'TOUTES SAISONS ' + annee,
                'CIBLE':
                HS["CIBLE"][len(HS) - 1] +
                MS1["CIBLE"][len(MS1) - 1] + MS2["CIBLE"][len(MS2) - 1]+BS1["CIBLE"][len(BS1) - 1],
                'VENTE':
                HS["VENTE"][len(HS) - 1] +
                MS1["VENTE"][len(MS1) - 1] + MS2["VENTE"][len(MS2) - 1]+BS1["VENTE"][len(BS1) - 1],
                "CUMUL":
                HS["CUMUL"][len(HS) - 1] +
                MS1["CUMUL"][len(MS1) - 1] + MS2["CUMUL"][len(MS2) - 1]+BS1["CUMUL"][len(BS1) - 1],
                "BUDGET":
                "",
                "OBJECTIF":
                ""
            },
            ignore_index=True)
    del reporting['index']

    return reporting


# Files stats with Django


def StatCSCInfo(request):
    if request.method == 'POST':
        annee = request.POST["annee"]

        data = pd.DataFrame(columns=['Mois', 'Cible', 'Budget', 'Objectif'])
        mesurecsc = ReportingCorse.objects.filter(Annee=annee)
        df_test_ = pd.DataFrame(list(mesurecsc.values()))

        if len(df_test_) != 0:
            for i in range(len(df_test_)):
                data.loc[i] = df_test_["Mois"][i], df_test_["Cible"][
                    i], df_test_["Budget"][i], df_test_["Objectif"][i]

        print(data)
    return HttpResponse(data.to_json(orient='records'))


def StatCSCObj(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee = request.POST["annee"]
        mois = request.POST["mois"]
        cible = request.POST["cible"]
        budget = request.POST["budget"]
        objectif = request.POST["objectif"]
        df1 = pd.read_csv(File1, sep=';', index_col=False)
        df2 = pd.read_csv(File2, sep=';', index_col=False)
        MOIS = mois.split(",")
        MOIS = list(map(int, MOIS))
        CIBLE = cible.split(",")
        CIBLE = list(map(int, CIBLE))
        BUDGET = budget.split(",")
        BUDGET = list(map(int, BUDGET))
        OBJECTIF = objectif.split(",")
        OBJECTIF = list(map(int, OBJECTIF))
        # Stats
        data = Stat_CSC_Objectif(df1, df2, annee, MOIS, CIBLE, BUDGET,
                                 OBJECTIF)
        print('data : ', data)

        for i in range(len(MOIS)):
            mesurecsc = ReportingCorse.objects.filter(Annee=annee,
                                                      Mois=MOIS[i])
            df_test_ = pd.DataFrame(list(mesurecsc.values()))

            if (len(df_test_) == 0):
                ReportingCorse.objects.create(Annee=annee,
                                              Mois=MOIS[i],
                                              Cible=CIBLE[i],
                                              Budget=BUDGET[i],
                                              Objectif=OBJECTIF[i])
            if (len(df_test_) != 0):
                mesurecsc.update(Cible=CIBLE[i],
                                 Budget=BUDGET[i],
                                 Objectif=OBJECTIF[i])

    return HttpResponse(data.to_json(orient='records'))


def StatCSC(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee = request.POST["annee"]
        mois = request.POST["mois"]
        cible = request.POST["cible"]
        budget = request.POST["budget"]
        df1 = pd.read_csv(File1, sep=';', index_col=False)
        df2 = pd.read_csv(File2, sep=';', index_col=False)
        MOIS = mois.split(",")
        MOIS = list(map(int, MOIS))
        CIBLE = cible.split(",")
        CIBLE = list(map(int, CIBLE))
        BUDGET = budget.split(",")
        BUDGET = list(map(int, BUDGET))
        # Stats
        data = Stat_CSC(df1, df2, annee, MOIS, CIBLE, BUDGET)
        print('data : ', data)

        for i in range(len(MOIS)):
            mesurecsc = ReportingCorse.objects.filter(Annee=annee,
                                                      Mois=MOIS[i])
            df_test_ = pd.DataFrame(list(mesurecsc.values()))

            if (len(df_test_) == 0):
                ReportingCorse.objects.create(Annee=annee,
                                              Mois=MOIS[i],
                                              Cible=CIBLE[i],
                                              Budget=BUDGET[i])
            if (len(df_test_) != 0):
                mesurecsc.update(Cible=CIBLE[i], Budget=BUDGET[i])

    return HttpResponse(data.to_json(orient='records'))


def StatCSCPLUS(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee = request.POST["annee"]
        mois = request.POST["mois"]
        df1 = pd.read_csv(File1, sep=';', index_col=False)
        df2 = pd.read_csv(File2, sep=';', index_col=False)
        MOIS = mois.split(",")
        MOIS = list(map(int, MOIS))
        # Stats
        data = Stat_CSC_plus(df1, df2, annee, MOIS)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))