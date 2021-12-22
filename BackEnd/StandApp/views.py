import calendar
import numpy as np
from pymongo import MongoClient
import pandas as pd
from pathlib import Path
from django.http import HttpResponse

# REFERENCE DATABASE CONNECTION

client = MongoClient('localhost', 27017)

# Nom de la base = TransportRefDB92
# Nom de la collection = Companies92
db = client['Reporting']
cibleCSC = db['CibleCSC']
budgetCSC = db['BudgetCSC']
cibleALG = db['CibleALG']
budgetALG = db['BudgetALG']
cibleTUN = db['CibleTUN']
budgetTUN = db['BudgetTUN']


def Stat_CSC(data_yesterday, data_today, annee, mois, cible, budget):
    table_reseau_armateur_today = pd.pivot_table(
        data_today[(data_today.RESEAU == "CORSE")
                   & (data_today.ARMATEUR == "CL")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_yesterday = pd.pivot_table(
        data_yesterday[(data_yesterday.RESEAU == "CORSE")
                       & (data_yesterday.ARMATEUR == "CL")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    df = pd.DataFrame()
    df["ANNEE"] = table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"] = table_reseau_armateur_yesterday['MOIS']
    df["CUMUL-18"] = table_reseau_armateur_yesterday['PAX']
    df["CUMUL-19"] = table_reseau_armateur_today['PAX']
    df['Vente journalière'] = table_reseau_armateur_today[
        'PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask = df[df.ANNEE.eq(int(annee) - 1) | df.ANNEE.eq(int(annee))
                 | df.ANNEE.eq(int(annee) + 1)]
    df_mask = df_mask[df_mask.ANNEE.eq(int(annee))]

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
    print("df", df_mask_cumul)
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
    print("df", df_mask_cumul)
    print("mesure", mesure)
    print(len(mesure))
    print(cible)
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
    bud=0
    for i in mesure.index:
        bud+=mesure["BUD"][i]
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
                    "BASSE SAISON 1", BS1["CIBLE"][0] + BS1["CIBLE"][1] + BS1["CIBLE"][2],
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    round((
                        (BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2]) /
                        (mesure["BUD"][i - 2] + mesure["BUD"][i - 1] +
                         mesure["BUD"][i])) * 100)
                ]
            elif len(BS1) == 2:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["CIBLE"][1] + BS1["CIBLE"][2] , BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    round(((BS1["CUMUL"][1] + BS1["CUMUL"][2]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["CIBLE"][1], BS1["VENTE"][1], BS1["CUMUL"][1],
                    BS1["BUDGET"][1]
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
                    "MOYENNE SAISON 1", MS1["CIBLE"][0] + MS1["CIBLE"][1] + MS1["CIBLE"][2],
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    round((
                        (MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2]) /
                        (mesure["BUD"][i - 2] + mesure["BUD"][i - 1] +
                         mesure["BUD"][i])) * 100)
                ]
            elif len(MS1) == 2:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["CIBLE"][1] + MS1["CIBLE"][2], MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    round(((MS1["CUMUL"][1] + MS1["CUMUL"][2]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["CIBLE"][1], MS1["VENTE"][1], MS1["CUMUL"][1],
                    MS1["BUDGET"][1]
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
                    "HAUTE SAISON", HS["CIBLE"][0] + HS["CIBLE"][1], HS["VENTE"][0] + HS["VENTE"][1],
                    HS["CUMUL"][0] + HS["CUMUL"][1],
                    round(((HS["CUMUL"][0] + HS["CUMUL"][1]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["CIBLE"][1], HS["VENTE"][1], HS["CUMUL"][1],
                    HS["BUDGET"][1]
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
                    "MOYENNE SAISON 2", MS2["CIBLE"][0] + MS2["CIBLE"][1], MS2["VENTE"][0] + MS2["VENTE"][1],
                    MS2["CUMUL"][0] + MS2["CUMUL"][1],
                    round(((MS2["CUMUL"][0] + MS2["CUMUL"][1]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["CIBLE"][1], MS2["VENTE"][1], MS2["CUMUL"][1],
                    MS2["BUDGET"][1]
                ]
        #  2 BS
        if mesure["CORSE"][i] == "Nov":
            BS2.loc[0] = [
                "Novembre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
            if mesure["CORSE"][i+1] != "Dec":
                if len(BS2) == 1:
                    BS2.loc[1] = [
                    "BASSE SAISON 2", BS2["CIBLE"][0], BS2["VENTE"][0], BS2["CUMUL"][0],BS2["BUDGET"][0]
                ]
        if mesure["CORSE"][i] == "Dec":
            BS2.loc[1] = [
                "Décembre", mesure["CIBLE"][i], mesure["VENTE"][i],
                mesure["CUMUL"][i], mesure["BUDGET"][i]
            ]
            if len(BS2) == 2:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["CIBLE"][0] + BS2["CIBLE"][1], BS2["VENTE"][0] + BS2["VENTE"][1],
                    BS2["CUMUL"][0] + BS2["CUMUL"][1],
                    round(((BS2["CUMUL"][0] + BS2["CUMUL"][1]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["CIBLE"][1], BS2["VENTE"][1], BS2["CUMUL"][1],
                    BS2["BUDGET"][1]
                ]
    print("BS1", len(BS1))
    print("BS2", len(BS2))
    print("HS", len(HS))
    print("MS1", len(MS1))
    print("MS2", len(MS2))
    if len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([BS1, MS1, HS, MS2, BS2])
    elif len(MS1) != 0 and len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS1, HS, MS2, BS2])
    elif len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([HS, MS2, BS2])
    elif len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS2, BS2])
    elif len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) != 0 and len(BS2) == 0:
        reporting = pd.concat([BS1, MS1, HS, MS2])
    elif len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) == 0 and len(BS2) == 0:
        reporting = pd.concat([BS1, MS1, HS])
    elif len(BS1) != 0 and len(MS1) != 0 and len(HS) == 0 and len(
            MS2) == 0 and len(BS2) == 0:
        reporting = pd.concat([BS1, MS1])
    elif len(BS1) != 0 and len(MS1) == 0 and len(HS) == 0 and len(
            MS2) == 0 and len(BS2) == 0:
        reporting = BS1
    else:
        reporting = BS2
    print("reporting", reporting)
    reporting.reset_index(inplace=True)
    if len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting=reporting.append({'CORSE':'TOUTES SAISONS '+annee, 'CIBLE':BS1["CIBLE"][len(BS1)-1]+BS2["CIBLE"][len(BS2)-1]+HS["CIBLE"][len(HS)-1]+MS1["CIBLE"][len(MS1)-1]+MS2["CIBLE"][len(MS2)-1], 'VENTE':BS1["VENTE"][len(BS1)-1]+BS2["VENTE"][len(BS2)-1]+HS["VENTE"][len(HS)-1]+MS1["VENTE"][len(MS1)-1]+MS2["VENTE"][len(MS2)-1], "CUMUL":BS1["CUMUL"][len(BS1)-1]+BS2["CUMUL"][len(BS2)-1]+HS["CUMUL"][len(HS)-1]+MS1["CUMUL"][len(MS1)-1]+MS2["CUMUL"][len(MS2)-1], "BUDGET":round(((BS1["CUMUL"][len(BS1)-1]+BS2["CUMUL"][len(BS2)-1]+HS["CUMUL"][len(HS)-1]+MS1["CUMUL"][len(MS1)-1]+MS2["CUMUL"][len(MS2)-1])/(bud))*100)} , ignore_index=True)
    elif len(MS1) != 0 and len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting=reporting.append({'CORSE':'TOUTES SAISONS '+annee, 'CIBLE':BS2["CIBLE"][len(BS2)-1]+HS["CIBLE"][len(HS)-1]+MS1["CIBLE"][len(MS1)-1]+MS2["CIBLE"][len(MS2)-1], 'VENTE':BS2["VENTE"][len(BS2)-1]+HS["VENTE"][len(HS)-1]+MS1["VENTE"][len(MS1)-1]+MS2["VENTE"][len(MS2)-1], "CUMUL":BS2["CUMUL"][len(BS2)-1]+HS["CUMUL"][len(HS)-1]+MS1["CUMUL"][len(MS1)-1]+MS2["CUMUL"][len(MS2)-1], "BUDGET":round(((BS2["CUMUL"][len(BS2)-1]+HS["CUMUL"][len(HS)-1]+MS1["CUMUL"][len(MS1)-1]+MS2["CUMUL"][len(MS2)-1])/(bud))*100)} , ignore_index=True)
    elif len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting=reporting.append({'CORSE':'TOUTES SAISONS '+annee, 'CIBLE':BS2["CIBLE"][len(BS2)-1]+HS["CIBLE"][len(HS)-1]+MS2["CIBLE"][len(MS2)-1], 'VENTE':BS2["VENTE"][len(BS2)-1]+HS["VENTE"][len(HS)-1]+MS2["VENTE"][len(MS2)-1], "CUMUL":BS2["CUMUL"][len(BS2)-1]+HS["CUMUL"][len(HS)-1]+MS2["CUMUL"][len(MS2)-1], "BUDGET":round(((BS2["CUMUL"][len(BS2)-1]+HS["CUMUL"][len(HS)-1]+MS2["CUMUL"][len(MS2)-1])/(bud))*100)} , ignore_index=True)
    elif len(MS2) != 0 and len(BS2) != 0:
        reporting=reporting.append({'CORSE':'TOUTES SAISONS '+annee, 'CIBLE':BS2["CIBLE"][len(BS2)-1]+MS2["CIBLE"][len(MS2)-1], 'VENTE':BS2["VENTE"][len(BS2)-1]+MS2["VENTE"][len(MS2)-1], "CUMUL":BS2["CUMUL"][len(BS2)-1]+MS2["CUMUL"][len(MS2)-1], "BUDGET":round(((BS2["CUMUL"][len(BS2)-1]+MS2["CUMUL"][len(MS2)-1])/(bud))*100)} , ignore_index=True)
    elif len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(MS2) != 0 and len(BS2) == 0:
        reporting=reporting.append({'CORSE':'TOUTES SAISONS '+annee, 'CIBLE':BS1["CIBLE"][len(BS1)-1]+HS["CIBLE"][len(HS)-1]+MS1["CIBLE"][len(MS1)-1]+MS2["CIBLE"][len(MS2)-1], 'VENTE':BS1["VENTE"][len(BS1)-1]+HS["VENTE"][len(HS)-1]+MS1["VENTE"][len(MS1)-1]+MS2["VENTE"][len(MS2)-1], "CUMUL":BS1["CUMUL"][len(BS1)-1]+HS["CUMUL"][len(HS)-1]+MS1["CUMUL"][len(MS1)-1]+MS2["CUMUL"][len(MS2)-1], "BUDGET":round(((BS1["CUMUL"][len(BS1)-1]+HS["CUMUL"][len(HS)-1]+MS1["CUMUL"][len(MS1)-1]+MS2["CUMUL"][len(MS2)-1])/(bud))*100)} , ignore_index=True)
    elif len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(MS2) == 0 and len(BS2) == 0:
        reporting=reporting.append({'CORSE':'TOUTES SAISONS '+annee, 'CIBLE':BS1["CIBLE"][len(BS1)-1]+HS["CIBLE"][len(HS)-1]+MS1["CIBLE"][len(MS1)-1], 'VENTE':BS1["VENTE"][len(BS1)-1]+HS["VENTE"][len(HS)-1]+MS1["VENTE"][len(MS1)-1], "CUMUL":BS1["CUMUL"][len(BS1)-1]+HS["CUMUL"][len(HS)-1]+MS1["CUMUL"][len(MS1)-1], "BUDGET":round(((BS1["CUMUL"][len(BS1)-1]+HS["CUMUL"][len(HS)-1]+MS1["CUMUL"][len(MS1)-1])/(bud))*100)} , ignore_index=True)
    elif len(BS1) != 0 and len(MS1) != 0 and len(HS) == 0 and len(MS2) == 0 and len(BS2) == 0:
        reporting=reporting.append({'CORSE':'TOUTES SAISONS '+annee, 'CIBLE':BS1["CIBLE"][len(BS1)-1]+MS1["CIBLE"][len(MS1)-1], 'VENTE':BS1["VENTE"][len(BS1)-1]+MS1["VENTE"][len(MS1)-1], "CUMUL":BS1["CUMUL"][len(BS1)-1]+MS1["CUMUL"][len(MS1)-1], "BUDGET":round(((BS1["CUMUL"][len(BS1)-1]+MS1["CUMUL"][len(MS1)-1])/(bud))*100)} , ignore_index=True)
    elif len(BS1) != 0 and len(MS1) == 0 and len(HS) == 0 and len(MS2) == 0 and len(BS2) == 0:
        reporting=reporting.append({'CORSE':'TOUTES SAISONS '+annee, 'CIBLE':BS1["CIBLE"][len(BS1)-1], 'VENTE':BS1["VENTE"][len(BS1)-1], "CUMUL":BS1["CUMUL"][len(BS1)-1], "BUDGET":round(((BS1["CUMUL"][len(BS1)-1])/(bud))*100)} , ignore_index=True)
    else:
        reporting=reporting.append({'CORSE':'TOUTES SAISONS '+annee, 'CIBLE':BS2["CIBLE"][len(BS2)-1], 'VENTE':BS2["VENTE"][len(BS2)-1], "CUMUL":BS2["CUMUL"][len(BS2)-1], "BUDGET":round(((BS2["CUMUL"][len(BS2)-1])/(bud))*100)} , ignore_index=True)

    del reporting['index']

    for i in range(len(reporting)):
        reporting["BUDGET"][i] = str(reporting["BUDGET"][i]) + ' %'

    return reporting


def Stat_CSC_plus(data_yesterday, data_today, annee, mois):
    table_reseau_armateur_today = pd.pivot_table(
        data_today[(data_today.RESEAU == "CORSE")
                   & (data_today.ARMATEUR == "CL")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_yesterday = pd.pivot_table(
        data_yesterday[(data_yesterday.RESEAU == "CORSE")
                       & (data_yesterday.ARMATEUR == "CL")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    df = pd.DataFrame()
    df["ANNEE"] = table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"] = table_reseau_armateur_yesterday['MOIS']
    df["CUMUL-18"] = table_reseau_armateur_yesterday['PAX']
    df["CUMUL-19"] = table_reseau_armateur_today['PAX']
    df['Vente journalière'] = table_reseau_armateur_today[
        'PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask = df[df.ANNEE.eq(int(annee) - 1) | df.ANNEE.eq(int(annee))
                 | df.ANNEE.eq(int(annee) - 1)]
    df_mask = df_mask[df_mask.ANNEE.eq(int(annee))]
    print(df_mask)
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
    mesure = pd.DataFrame()
    mesure["CORSE"] = df_mask_cumul['MOIS'].apply(
        lambda x: calendar.month_abbr[int(x)])
    mesure["VENTE"] = df_mask_cumul['Vente journalière']
    mesure["CUMUL"] = df_mask_cumul['CUMUL-19']

    BS1 = pd.DataFrame(
        columns=['CORSE', 'CIBLE/JR', 'VENTE', "CUMUL", "BUDGET"])
    MS1 = pd.DataFrame(
        columns=['CORSE', 'CIBLE/JR', 'VENTE', "CUMUL", "BUDGET"])
    HS = pd.DataFrame(
        columns=['CORSE', 'CIBLE/JR', 'VENTE', "CUMUL", "BUDGET"])
    MS2 = pd.DataFrame(
        columns=['CORSE', 'CIBLE/JR', 'VENTE', "CUMUL", "BUDGET"])
    BS2 = pd.DataFrame(
        columns=['CORSE', 'CIBLE/JR', 'VENTE', "CUMUL", "BUDGET"])
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
        #  HS
        if mesure["CORSE"][i] == "Jul":
            HS.loc[0] = [
                "Juillet", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        if mesure["CORSE"][i] == "Aug":
            HS.loc[1] = [
                "Août", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        #  2 MS
        if mesure["CORSE"][i] == "Sep":
            MS2.loc[0] = [
                "Septembre", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
            ]
        if mesure["CORSE"][i] == "Oct":
            MS2.loc[1] = [
                "Octobre", "", mesure["VENTE"][i], mesure["CUMUL"][i], ""
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

        if len(BS1) == 3:
            BS1.loc[3] = [
                "BASSE SAISON 1", "",
                BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2], ""
            ]
        elif len(BS1) == 2:
            BS1.loc[2] = [
                "BASSE SAISON 1", "", BS1["VENTE"][1] + BS1["VENTE"][0],
                BS1["CUMUL"][1] + BS1["CUMUL"][0], ""
            ]
        elif len(BS1) == 1:
            BS1.loc[1] = [
                "BASSE SAISON 1", "", BS1["VENTE"][0], BS1["CUMUL"][0],
                BS1["BUDGET"][0]
            ]

        if len(MS1) == 3:
            MS1.loc[3] = [
                "MOYENNE SAISON 1", "",
                MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2], ""
            ]
        elif len(MS1) == 2:
            MS1.loc[2] = [
                "MOYENNE SAISON 1", "", MS1["VENTE"][1] + MS1["VENTE"][0],
                MS1["CUMUL"][1] + MS1["CUMUL"][0], ""
            ]
        elif len(MS1) == 1:
            MS1.loc[1] = [
                "MOYENNE SAISON 1", "", MS1["VENTE"][0], MS1["CUMUL"][0],
                MS1["BUDGET"][0]
            ]

        if len(HS) == 2:
            HS.loc[2] = [
                "HAUTE SAISON", "", HS["VENTE"][0] + HS["VENTE"][1],
                HS["CUMUL"][0] + HS["CUMUL"][1], ""
            ]
        elif len(HS) == 1:
            HS.loc[1] = [
                "HAUTE SAISON", "", HS["VENTE"][0], HS["CUMUL"][0],
                HS["BUDGET"][0]
            ]

        if len(MS2) == 2:
            MS2.loc[2] = [
                "MOYENNE SAISON 2", "", MS2["VENTE"][0] + MS2["VENTE"][1],
                MS2["CUMUL"][0] + MS2["CUMUL"][1], ""
            ]
        elif len(MS2) == 1:
            MS2.loc[1] = [
                "MOYENNE SAISON 2", "", MS2["VENTE"][0], MS2["CUMUL"][0],
                MS2["BUDGET"][0]
            ]

        if len(BS2) == 2:
            BS2.loc[2] = [
                "BASSE SAISON 2", "", BS2["VENTE"][0] + BS2["VENTE"][1],
                BS2["CUMUL"][0] + BS2["CUMUL"][1], ""
            ]
        elif len(BS2) == 1:
            BS2.loc[1] = [
                "BASSE SAISON 2", "", BS2["VENTE"][0], BS2["CUMUL"][0],
                BS2["BUDGET"][0]
            ]

    if len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([BS1, MS1, HS, MS2, BS2])
    elif len(MS1) != 0 and len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS1, HS, MS2, BS2])
    elif len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([HS, MS2, BS2])
    elif len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS2, BS2])
    elif len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) != 0 and len(BS2) == 0:
        reporting = pd.concat([BS1, MS1, HS, MS2])
    elif len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) == 0 and len(BS2) == 0:
        reporting = pd.concat([BS1, MS1, HS])
    elif len(BS1) != 0 and len(MS1) != 0 and len(HS) == 0 and len(
            MS2) == 0 and len(BS2) == 0:
        reporting = pd.concat([BS1, MS1])
    elif len(BS1) != 0 and len(MS1) == 0 and len(HS) == 0 and len(
            MS2) == 0 and len(BS2) == 0:
        reporting = BS1
    else:
        reporting = BS2

    reporting.reset_index(inplace=True)
    del reporting['index']

    return reporting


def Stat_ALG(data_yesterday, data_today, annee, mois):
    table_reseau_armateur_today = pd.pivot_table(
        data_today[(data_today.RESEAU == "ALGERIE")
                   & (data_today.ARMATEUR == "CL")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_yesterday = pd.pivot_table(
        data_yesterday[(data_yesterday.RESEAU == "ALGERIE")
                       & (data_yesterday.ARMATEUR == "CL")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    df = pd.DataFrame()
    df["ANNEE"] = table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"] = table_reseau_armateur_yesterday['MOIS']
    df["CUMUL"] = table_reseau_armateur_today['PAX']
    df['VENTE'] = table_reseau_armateur_today[
        'PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask = df[df.ANNEE.eq(int(annee) - 1) | df.ANNEE.eq(int(annee))
                 | df.ANNEE.eq(int(annee) + 1)]
    df_mask_2020 = pd.DataFrame()
    df_mask_2020 = df_mask[df_mask.ANNEE.eq(int(annee) - 1)]
    df_mask_2021 = pd.DataFrame()
    df_mask_2021 = df_mask[df_mask.ANNEE.eq(int(annee))]

    if len(mois) == 1:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])]
    if len(mois) == 2:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])]
    if len(mois) == 3:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])]
    if len(mois) == 4:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])]
    if len(mois) == 5:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])]
    if len(mois) == 6:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])]
    if len(mois) == 7:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])]
    if len(mois) == 8:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])]
    if len(mois) == 9:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])]
    if len(mois) == 10:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])]
    if len(mois) == 11:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])
                                          | df_mask_2020.MOIS.eq(mois[10])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])
                                          | df_mask_2021.MOIS.eq(mois[10])]
    if len(mois) == 12:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])
                                          | df_mask_2020.MOIS.eq(mois[10])
                                          | df_mask_2020.MOIS.eq(mois[11])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])
                                          | df_mask_2021.MOIS.eq(mois[10])
                                          | df_mask_2021.MOIS.eq(mois[11])]

    del df_mask_cumul_2020["ANNEE"]
    df_mask_cumul_2020.columns = ['MOIS', 'CUMULYES', 'VENTEYES']
    df_mask_cumul_2020.reset_index(drop=True, inplace=True)

    del df_mask_cumul_2021["ANNEE"]
    df_mask_cumul_2021.columns = ['MOIS', 'CUMUL', 'VENTE']
    df_mask_cumul_2021.reset_index(drop=True, inplace=True)

    mesure = pd.DataFrame()

    mesure["ALGERIE"] = df_mask_cumul_2020['MOIS'].apply(
        lambda x: calendar.month_abbr[x])
    mesure["VENTEYES"] = df_mask_cumul_2020['VENTEYES'].apply(lambda x: x)
    mesure["VENTE"] = df_mask_cumul_2021['VENTE'].apply(lambda x: x)
    mesure["CUMULYES"] = df_mask_cumul_2020['CUMULYES'].apply(lambda x: x)
    mesure["CUMUL"] = df_mask_cumul_2021['CUMUL'].apply(lambda x: x)
    mesure["ECART"] = (
        (df_mask_cumul_2021['CUMUL'] - df_mask_cumul_2020['CUMULYES']) /
        df_mask_cumul_2020['CUMULYES']).apply(lambda x: int(x * 100))

    mesure = mesure.reset_index(drop=True)

    BS1 = pd.DataFrame(
        columns=['ALGERIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    MS1 = pd.DataFrame(
        columns=['ALGERIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    HS = pd.DataFrame(
        columns=['ALGERIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    MS2 = pd.DataFrame(
        columns=['ALGERIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    BS2 = pd.DataFrame(
        columns=['ALGERIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    for i in mesure.index:
        #  1 BS
        if mesure["ALGERIE"][i] == "Jan":
            BS1.loc[0] = [
                "Janvier", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ALGERIE"][i] == "Feb":
            BS1.loc[1] = [
                "Février", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ALGERIE"][i] == "Mar":
            BS1.loc[2] = [
                "Mars", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(BS1) == 3:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][0] + BS1["VENTEYES"][1] +
                    BS1["VENTEYES"][2],
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMULYES"][0] + BS1["CUMULYES"][1] +
                    BS1["CUMULYES"][2],
                    BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    (BS1["ECART"][0] + BS1["ECART"][1] + BS1["ECART"][2])
                ]
            elif len(BS1) == 2:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][1] + BS1["VENTEYES"][2],
                    BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMULYES"][1] + BS1["CUMULYES"][2],
                    BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    (BS1["ECART"][1] + BS1["ECART"][2])
                ]
            else:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][1], BS1["VENTE"][1],
                    BS1["CUMUL"][1], BS1["ECART"][1]
                ]
        #  1 MS
        if mesure["ALGERIE"][i] == "Apr":
            MS1.loc[0] = [
                "Avril", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ALGERIE"][i] == "May":
            MS1.loc[1] = [
                "Mai", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ALGERIE"][i] == "Jun":
            MS1.loc[2] = [
                "juin", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(MS1) == 3:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTEYES"][0] +
                    MS1["VENTEYES"][1] + MS1["VENTEYES"][2],
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMULYES"][0] + MS1["CUMULYES"][1] +
                    MS1["CUMULYES"][2],
                    MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    (MS1["ECART"][0] + MS1["ECART"][1] + MS1["ECART"][2])
                ]
            elif len(MS1) == 2:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1",
                    MS1["VENTEYES"][1] + MS1["VENTEYES"][2],
                    MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMULYES"][1] + MS1["CUMULYES"][2],
                    MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    (MS1["ECART"][1] + MS1["ECART"][2])
                ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTEYES"][1], MS1["VENTE"][1],
                    MS1["CUMULYES"][1], MS1["CUMUL"][1], MS1["ECART"][1]
                ]
        #  HS
        if mesure["ALGERIE"][i] == "Jul":
            HS.loc[0] = [
                "Juillet", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ALGERIE"][i] == "Aug":
            HS.loc[1] = [
                "Août", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(HS) == 2:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["VENTEYES"][0] + HS["VENTEYES"][1],
                    HS["VENTE"][0] + HS["VENTE"][1],
                    HS["CUMULYES"][0] + HS["CUMULYES"][1],
                    HS["CUMUL"][0] + HS["CUMUL"][1],
                    (HS["ECART"][0] + HS["ECART"][1])
                ]
            else:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["VENTEYES"][1], HS["VENTE"][1],
                    HS["CUMUL"][1], HS["ECART"][1]
                ]
        #  2 MS
        if mesure["ALGERIE"][i] == "Sep":
            MS2.loc[0] = [
                "Septembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ALGERIE"][i] == "Oct":
            MS2.loc[1] = [
                "Octobre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(MS2) == 2:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2",
                    MS2["VENTEYES"][0] + MS2["VENTEYES"][1],
                    MS2["VENTE"][0] + MS2["VENTE"][1],
                    MS2["CUMULYES"][0] + MS2["CUMULYES"][1],
                    MS2["CUMUL"][0] + MS2["CUMUL"][1],
                    (MS2["ECART"][0] + MS2["ECART"][1])
                ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["VENTEYES"][1], MS2["VENTE"][1],
                    MS2["CUMULYES"][1], MS2["CUMUL"][1], MS2["ECART"][1]
                ]
        #  2 BS
        if mesure["ALGERIE"][i] == "Nov":
            BS2.loc[0] = [
                "Novembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ALGERIE"][i] == "Dec":
            BS2.loc[1] = [
                "Décembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(BS2) == 2:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTEYES"][1] + BS2["VENTEYES"][0],
                    BS2["VENTE"][0] + BS2["VENTE"][1],
                    BS2["CUMULYES"][0] + BS2["CUMULYES"][1],
                    BS2["CUMUL"][0] + BS2["CUMUL"][1],
                    int((((BS2["CUMUL"][0] + BS2["CUMUL"][1]) -
                          (BS2["CUMULYES"][0] + BS2["CUMULYES"][1])) /
                         (BS2["CUMULYES"][0] + BS2["CUMULYES"][1])) * 100)
                ]
            else:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTEYES"][1], BS2["VENTE"][1],
                    BS2["CUMULYES"][1], BS2["CUMUL"][1], BS2["ECART"][1]
                ]

    if len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([BS1, MS1, HS, MS2, BS2])
    elif len(MS1) != 0 and len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS1, HS, MS2, BS2])
    elif len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([HS, MS2, BS2])
    elif len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS2, BS2])
    else:
        reporting = BS2

    reporting = reporting.reset_index(drop=True)
    for i in range(len(reporting)):
        reporting["ECART"][i] = str(reporting["ECART"][i]) + ' %'

    return reporting


def Stat_ITA(data_yesterday, data_today, annee, mois):
    table_reseau_armateur_today = pd.pivot_table(
        data_today[(data_today.RESEAU == "ITALIE")
                   & (data_today.ARMATEUR == "CTN")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_yesterday = pd.pivot_table(
        data_yesterday[(data_yesterday.RESEAU == "ITALIE")
                       & (data_yesterday.ARMATEUR == "CTN")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    df = pd.DataFrame()
    df["ANNEE"] = table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"] = table_reseau_armateur_yesterday['MOIS']
    df["CUMUL"] = table_reseau_armateur_today['PAX']
    df['VENTE'] = table_reseau_armateur_today[
        'PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask = df[df.ANNEE.eq(int(annee) - 1) | df.ANNEE.eq(int(annee))
                 | df.ANNEE.eq(int(annee) + 1)]
    df_mask_2020 = pd.DataFrame()
    df_mask_2020 = df_mask[df_mask.ANNEE.eq(int(annee) - 1)]
    df_mask_2021 = pd.DataFrame()
    df_mask_2021 = df_mask[df_mask.ANNEE.eq(int(annee))]

    if len(mois) == 1:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])]
    if len(mois) == 2:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])]
    if len(mois) == 3:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])]
    if len(mois) == 4:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])]
    if len(mois) == 5:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])]
    if len(mois) == 6:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])]
    if len(mois) == 7:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])]
    if len(mois) == 8:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])]
    if len(mois) == 9:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])]
    if len(mois) == 10:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])]
    if len(mois) == 11:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])
                                          | df_mask_2020.MOIS.eq(mois[10])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])
                                          | df_mask_2021.MOIS.eq(mois[10])]
    if len(mois) == 12:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])
                                          | df_mask_2020.MOIS.eq(mois[10])
                                          | df_mask_2020.MOIS.eq(mois[11])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])
                                          | df_mask_2021.MOIS.eq(mois[10])
                                          | df_mask_2021.MOIS.eq(mois[11])]

    del df_mask_cumul_2020["ANNEE"]
    df_mask_cumul_2020.columns = ['MOIS', 'CUMULYES', 'VENTEYES']
    df_mask_cumul_2020.reset_index(drop=True, inplace=True)

    del df_mask_cumul_2021["ANNEE"]
    df_mask_cumul_2021.columns = ['MOIS', 'CUMUL', 'VENTE']
    df_mask_cumul_2021.reset_index(drop=True, inplace=True)

    mesure = pd.DataFrame()

    mesure["ITALIE"] = df_mask_cumul_2020['MOIS'].apply(
        lambda x: calendar.month_abbr[x])
    mesure["VENTEYES"] = df_mask_cumul_2020['VENTEYES'].apply(lambda x: x)
    mesure["VENTE"] = df_mask_cumul_2021['VENTE'].apply(lambda x: x)
    mesure["CUMULYES"] = df_mask_cumul_2020['CUMULYES'].apply(lambda x: x)
    mesure["CUMUL"] = df_mask_cumul_2021['CUMUL'].apply(lambda x: x)
    mesure["ECART"] = (
        (df_mask_cumul_2021['CUMUL'] - df_mask_cumul_2020['CUMULYES']) /
        df_mask_cumul_2020['CUMULYES']).apply(lambda x: int(x * 100))

    mesure = mesure.reset_index(drop=True)

    BS1 = pd.DataFrame(
        columns=['ITALIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    MS1 = pd.DataFrame(
        columns=['ITALIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    HS = pd.DataFrame(
        columns=['ITALIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    MS2 = pd.DataFrame(
        columns=['ITALIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    BS2 = pd.DataFrame(
        columns=['ITALIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    for i in mesure.index:
        #  1 BS
        if mesure["ITALIE"][i] == "Jan":
            BS1.loc[0] = [
                "Janvier", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ITALIE"][i] == "Feb":
            BS1.loc[1] = [
                "Février", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ITALIE"][i] == "Mar":
            BS1.loc[2] = [
                "Mars", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(BS1) == 3:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][0] + BS1["VENTEYES"][1] +
                    BS1["VENTEYES"][2],
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMULYES"][0] + BS1["CUMULYES"][1] +
                    BS1["CUMULYES"][2],
                    BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    (BS1["ECART"][0] + BS1["ECART"][1] + BS1["ECART"][2])
                ]
            elif len(BS1) == 2:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][1] + BS1["VENTEYES"][2],
                    BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMULYES"][1] + BS1["CUMULYES"][2],
                    BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    (BS1["ECART"][1] + BS1["ECART"][2])
                ]
            else:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][1], BS1["VENTE"][1],
                    BS1["CUMUL"][1], BS1["ECART"][1]
                ]
        #  1 MS
        if mesure["ITALIE"][i] == "Apr":
            MS1.loc[0] = [
                "Avril", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ITALIE"][i] == "May":
            MS1.loc[1] = [
                "Mai", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ITALIE"][i] == "Jun":
            MS1.loc[2] = [
                "juin", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(MS1) == 3:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTEYES"][0] +
                    MS1["VENTEYES"][1] + MS1["VENTEYES"][2],
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMULYES"][0] + MS1["CUMULYES"][1] +
                    MS1["CUMULYES"][2],
                    MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    (MS1["ECART"][0] + MS1["ECART"][1] + MS1["ECART"][2])
                ]
            elif len(MS1) == 2:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1",
                    MS1["VENTEYES"][1] + MS1["VENTEYES"][2],
                    MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMULYES"][1] + MS1["CUMULYES"][2],
                    MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    (MS1["ECART"][1] + MS1["ECART"][2])
                ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTEYES"][1], MS1["VENTE"][1],
                    MS1["CUMULYES"][1], MS1["CUMUL"][1], MS1["ECART"][1]
                ]
        #  HS
        if mesure["ITALIE"][i] == "Jul":
            HS.loc[0] = [
                "Juillet", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ITALIE"][i] == "Aug":
            HS.loc[1] = [
                "Août", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(HS) == 2:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["VENTEYES"][0] + HS["VENTEYES"][1],
                    HS["VENTE"][0] + HS["VENTE"][1],
                    HS["CUMULYES"][0] + HS["CUMULYES"][1],
                    HS["CUMUL"][0] + HS["CUMUL"][1],
                    (HS["ECART"][0] + HS["ECART"][1])
                ]
            else:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["VENTEYES"][1], HS["VENTE"][1],
                    HS["CUMUL"][1], HS["ECART"][1]
                ]
        #  2 MS
        if mesure["ITALIE"][i] == "Sep":
            MS2.loc[0] = [
                "Septembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ITALIE"][i] == "Oct":
            MS2.loc[1] = [
                "Octobre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(MS2) == 2:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2",
                    MS2["VENTEYES"][0] + MS2["VENTEYES"][1],
                    MS2["VENTE"][0] + MS2["VENTE"][1],
                    MS2["CUMULYES"][0] + MS2["CUMULYES"][1],
                    MS2["CUMUL"][0] + MS2["CUMUL"][1],
                    (MS2["ECART"][0] + MS2["ECART"][1])
                ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["VENTEYES"][1], MS2["VENTE"][1],
                    MS2["CUMULYES"][1], MS2["CUMUL"][1], MS2["ECART"][1]
                ]
        #  2 BS
        if mesure["ITALIE"][i] == "Nov":
            BS2.loc[0] = [
                "Novembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["ITALIE"][i] == "Dec":
            BS2.loc[1] = [
                "Décembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(BS2) == 2:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTEYES"][1] + BS2["VENTEYES"][0],
                    BS2["VENTE"][0] + BS2["VENTE"][1],
                    BS2["CUMULYES"][0] + BS2["CUMULYES"][1],
                    BS2["CUMUL"][0] + BS2["CUMUL"][1],
                    int((((BS2["CUMUL"][0] + BS2["CUMUL"][1]) -
                          (BS2["CUMULYES"][0] + BS2["CUMULYES"][1])) /
                         (BS2["CUMULYES"][0] + BS2["CUMULYES"][1])) * 100)
                ]
            else:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTEYES"][1], BS2["VENTE"][1],
                    BS2["CUMULYES"][1], BS2["CUMUL"][1], BS2["ECART"][1]
                ]

    if len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([BS1, MS1, HS, MS2, BS2])
    elif len(MS1) != 0 and len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS1, HS, MS2, BS2])
    elif len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([HS, MS2, BS2])
    elif len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS2, BS2])
    else:
        reporting = BS2

    reporting = reporting.reset_index(drop=True)

    for i in range(len(reporting)):
        reporting["ECART"][i] = str(reporting["ECART"][i]) + ' %'

    return reporting


def Stat_TUN_CL(data_yesterday, data_today, annee, mois):
    table_reseau_armateur_today = pd.pivot_table(
        data_today[(data_today.RESEAU == "TUNISIE")
                   & (data_today.ARMATEUR == "CL")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_yesterday = pd.pivot_table(
        data_yesterday[(data_yesterday.RESEAU == "TUNISIE")
                       & (data_yesterday.ARMATEUR == "CL")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    df = pd.DataFrame()
    df["ANNEE"] = table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"] = table_reseau_armateur_yesterday['MOIS']
    df["CUMUL"] = table_reseau_armateur_today['PAX']
    df['VENTE'] = table_reseau_armateur_today[
        'PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask = df[df.ANNEE.eq(int(annee) - 1) | df.ANNEE.eq(int(annee))
                 | df.ANNEE.eq(int(annee) + 1)]
    df_mask_2020 = pd.DataFrame()
    df_mask_2020 = df_mask[df_mask.ANNEE.eq(int(annee) - 1)]
    df_mask_2021 = pd.DataFrame()
    df_mask_2021 = df_mask[df_mask.ANNEE.eq(int(annee))]

    if len(mois) == 1:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])]
    if len(mois) == 2:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])]
    if len(mois) == 3:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])]
    if len(mois) == 4:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])]
    if len(mois) == 5:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])]
    if len(mois) == 6:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])]
    if len(mois) == 7:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])]
    if len(mois) == 8:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])]
    if len(mois) == 9:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])]
    if len(mois) == 10:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])]
    if len(mois) == 11:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])
                                          | df_mask_2020.MOIS.eq(mois[10])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])
                                          | df_mask_2021.MOIS.eq(mois[10])]
    if len(mois) == 12:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])
                                          | df_mask_2020.MOIS.eq(mois[10])
                                          | df_mask_2020.MOIS.eq(mois[11])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])
                                          | df_mask_2021.MOIS.eq(mois[10])
                                          | df_mask_2021.MOIS.eq(mois[11])]

    del df_mask_cumul_2020["ANNEE"]
    df_mask_cumul_2020.columns = ['MOIS', 'CUMULYES', 'VENTEYES']
    df_mask_cumul_2020.reset_index(drop=True, inplace=True)

    del df_mask_cumul_2021["ANNEE"]
    df_mask_cumul_2021.columns = ['MOIS', 'CUMUL', 'VENTE']
    df_mask_cumul_2021.reset_index(drop=True, inplace=True)

    mesure = pd.DataFrame()

    mesure["TUNISIE"] = df_mask_cumul_2020['MOIS'].apply(
        lambda x: calendar.month_abbr[x])
    mesure["VENTEYES"] = df_mask_cumul_2020['VENTEYES'].apply(lambda x: x)
    mesure["VENTE"] = df_mask_cumul_2021['VENTE'].apply(lambda x: x)
    mesure["CUMULYES"] = df_mask_cumul_2020['CUMULYES'].apply(lambda x: x)
    mesure["CUMUL"] = df_mask_cumul_2021['CUMUL'].apply(lambda x: x)
    mesure["ECART"] = (
        (df_mask_cumul_2021['CUMUL'] - df_mask_cumul_2020['CUMULYES']) /
        df_mask_cumul_2020['CUMULYES']).apply(lambda x: x * 100)

    mesure = mesure.reset_index(drop=True)

    BS1 = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    MS1 = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    HS = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    MS2 = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    BS2 = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    for i in mesure.index:
        #  1 BS
        if mesure["TUNISIE"][i] == "Jan":
            BS1.loc[0] = [
                "Janvier", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Feb":
            BS1.loc[1] = [
                "Février", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Mar":
            BS1.loc[2] = [
                "Mars", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(BS1) == 3:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][0] + BS1["VENTEYES"][1] +
                    BS1["VENTEYES"][2],
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMULYES"][0] + BS1["CUMULYES"][1] +
                    BS1["CUMULYES"][2],
                    BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    (BS1["ECART"][0] + BS1["ECART"][1] + BS1["ECART"][2])
                ]
            elif len(BS1) == 2:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][1] + BS1["VENTEYES"][2],
                    BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMULYES"][1] + BS1["CUMULYES"][2],
                    BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    (BS1["ECART"][1] + BS1["ECART"][2])
                ]
            else:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][1], BS1["VENTE"][1],
                    BS1["CUMUL"][1], BS1["ECART"][1]
                ]
        #  1 MS
        if mesure["TUNISIE"][i] == "Apr":
            MS1.loc[0] = [
                "Avril", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "May":
            MS1.loc[1] = [
                "Mai", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Jun":
            MS1.loc[2] = [
                "juin", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(MS1) == 3:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTEYES"][0] +
                    MS1["VENTEYES"][1] + MS1["VENTEYES"][2],
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMULYES"][0] + MS1["CUMULYES"][1] +
                    MS1["CUMULYES"][2],
                    MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    (MS1["ECART"][0] + MS1["ECART"][1] + MS1["ECART"][2])
                ]
            elif len(MS1) == 2:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1",
                    MS1["VENTEYES"][1] + MS1["VENTEYES"][2],
                    MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMULYES"][1] + MS1["CUMULYES"][2],
                    MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    (MS1["ECART"][1] + MS1["ECART"][2])
                ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTEYES"][1], MS1["VENTE"][1],
                    MS1["CUMULYES"][1], MS1["CUMUL"][1], MS1["ECART"][1]
                ]
        #  HS
        if mesure["TUNISIE"][i] == "Jul":
            HS.loc[0] = [
                "Juillet", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Aug":
            HS.loc[1] = [
                "Août", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(HS) == 2:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["VENTEYES"][0] + HS["VENTEYES"][1],
                    HS["VENTE"][0] + HS["VENTE"][1],
                    HS["CUMULYES"][0] + HS["CUMULYES"][1],
                    HS["CUMUL"][0] + HS["CUMUL"][1],
                    (HS["ECART"][0] + HS["ECART"][1])
                ]
            else:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["VENTEYES"][1], HS["VENTE"][1],
                    HS["CUMUL"][1], HS["ECART"][1]
                ]
        #  2 MS
        if mesure["TUNISIE"][i] == "Sep":
            MS2.loc[0] = [
                "Septembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Oct":
            MS2.loc[1] = [
                "Octobre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(MS2) == 2:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2",
                    MS2["VENTEYES"][0] + MS2["VENTEYES"][1],
                    MS2["VENTE"][0] + MS2["VENTE"][1],
                    MS2["CUMULYES"][0] + MS2["CUMULYES"][1],
                    MS2["CUMUL"][0] + MS2["CUMUL"][1],
                    (MS2["ECART"][0] + MS2["ECART"][1])
                ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["VENTEYES"][1], MS2["VENTE"][1],
                    MS2["CUMULYES"][1], MS2["CUMUL"][1], MS2["ECART"][1]
                ]
        #  2 BS
        if mesure["TUNISIE"][i] == "Nov":
            BS2.loc[0] = [
                "Novembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Dec":
            BS2.loc[1] = [
                "Décembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(BS2) == 2:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTEYES"][1] + BS2["VENTEYES"][0],
                    BS2["VENTE"][0] + BS2["VENTE"][1],
                    BS2["CUMULYES"][0] + BS2["CUMULYES"][1],
                    BS2["CUMUL"][0] + BS2["CUMUL"][1],
                    (((BS2["CUMUL"][0] + BS2["CUMUL"][1]) -
                      (BS2["CUMULYES"][0] + BS2["CUMULYES"][1])) /
                     (BS2["CUMULYES"][0] + BS2["CUMULYES"][1])) * 100
                ]
            else:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTEYES"][1], BS2["VENTE"][1],
                    BS2["CUMULYES"][1], BS2["CUMUL"][1], BS2["ECART"][1]
                ]

    if len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([BS1, MS1, HS, MS2, BS2])
    elif len(MS1) != 0 and len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS1, HS, MS2, BS2])
    elif len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([HS, MS2, BS2])
    elif len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS2, BS2])
    else:
        reporting = BS2

    reporting = reporting.reset_index(drop=True)

    for i in range(len(reporting)):
        reporting["ECART"][i] = str(reporting["ECART"][i]) + ' %'

    return reporting


def Stat_TUN_CTN(data_yesterday, data_today, annee, mois):
    table_reseau_armateur_today = pd.pivot_table(
        data_today[(data_today.RESEAU == "TUNISIE")
                   & (data_today.ARMATEUR == "CTN")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_yesterday = pd.pivot_table(
        data_yesterday[(data_yesterday.RESEAU == "TUNISIE")
                       & (data_yesterday.ARMATEUR == "CTN")],
        index=['ANNEE', 'MOIS'],
        aggfunc={'PAX': np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    df = pd.DataFrame()
    df["ANNEE"] = table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"] = table_reseau_armateur_yesterday['MOIS']
    df["CUMUL"] = table_reseau_armateur_today['PAX']
    df['VENTE'] = table_reseau_armateur_today[
        'PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask = df[df.ANNEE.eq(int(annee) - 1) | df.ANNEE.eq(int(annee))
                 | df.ANNEE.eq(int(annee) + 1)]
    df_mask_2020 = pd.DataFrame()
    df_mask_2020 = df_mask[df_mask.ANNEE.eq(int(annee) - 1)]
    df_mask_2021 = pd.DataFrame()
    df_mask_2021 = df_mask[df_mask.ANNEE.eq(int(annee))]

    if len(mois) == 1:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])]
    if len(mois) == 2:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])]
    if len(mois) == 3:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])]
    if len(mois) == 4:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])]
    if len(mois) == 5:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])]
    if len(mois) == 6:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])]
    if len(mois) == 7:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])]
    if len(mois) == 8:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])]
    if len(mois) == 9:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])]
    if len(mois) == 10:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])]
    if len(mois) == 11:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])
                                          | df_mask_2020.MOIS.eq(mois[10])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])
                                          | df_mask_2021.MOIS.eq(mois[10])]
    if len(mois) == 12:
        df_mask_cumul_2020 = df_mask_2020[df_mask_2020.MOIS.eq(mois[0])
                                          | df_mask_2020.MOIS.eq(mois[1])
                                          | df_mask_2020.MOIS.eq(mois[2])
                                          | df_mask_2020.MOIS.eq(mois[3])
                                          | df_mask_2020.MOIS.eq(mois[4])
                                          | df_mask_2020.MOIS.eq(mois[5])
                                          | df_mask_2020.MOIS.eq(mois[6])
                                          | df_mask_2020.MOIS.eq(mois[7])
                                          | df_mask_2020.MOIS.eq(mois[8])
                                          | df_mask_2020.MOIS.eq(mois[9])
                                          | df_mask_2020.MOIS.eq(mois[10])
                                          | df_mask_2020.MOIS.eq(mois[11])]
        df_mask_cumul_2021 = df_mask_2021[df_mask_2021.MOIS.eq(mois[0])
                                          | df_mask_2021.MOIS.eq(mois[1])
                                          | df_mask_2021.MOIS.eq(mois[2])
                                          | df_mask_2021.MOIS.eq(mois[3])
                                          | df_mask_2021.MOIS.eq(mois[4])
                                          | df_mask_2021.MOIS.eq(mois[5])
                                          | df_mask_2021.MOIS.eq(mois[6])
                                          | df_mask_2021.MOIS.eq(mois[7])
                                          | df_mask_2021.MOIS.eq(mois[8])
                                          | df_mask_2021.MOIS.eq(mois[9])
                                          | df_mask_2021.MOIS.eq(mois[10])
                                          | df_mask_2021.MOIS.eq(mois[11])]

    del df_mask_cumul_2020["ANNEE"]
    df_mask_cumul_2020.columns = ['MOIS', 'CUMULYES', 'VENTEYES']
    df_mask_cumul_2020.reset_index(drop=True, inplace=True)

    del df_mask_cumul_2021["ANNEE"]
    df_mask_cumul_2021.columns = ['MOIS', 'CUMUL', 'VENTE']
    df_mask_cumul_2021.reset_index(drop=True, inplace=True)

    mesure = pd.DataFrame()

    mesure["TUNISIE"] = df_mask_cumul_2020['MOIS'].apply(
        lambda x: calendar.month_abbr[x])
    mesure["VENTEYES"] = df_mask_cumul_2020['VENTEYES'].apply(lambda x: x)
    mesure["VENTE"] = df_mask_cumul_2021['VENTE'].apply(lambda x: x)
    mesure["CUMULYES"] = df_mask_cumul_2020['CUMULYES'].apply(lambda x: x)
    mesure["CUMUL"] = df_mask_cumul_2021['CUMUL'].apply(lambda x: x)
    mesure["ECART"] = (
        (df_mask_cumul_2021['CUMUL'] - df_mask_cumul_2020['CUMULYES']) /
        df_mask_cumul_2020['CUMULYES']).apply(lambda x: int(x * 100))

    mesure = mesure.reset_index(drop=True)

    BS1 = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    MS1 = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    HS = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    MS2 = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    BS2 = pd.DataFrame(
        columns=['TUNISIE', 'VENTEYES', 'VENTE', "CUMULYES", "CUMUL", "ECART"])
    for i in mesure.index:
        #  1 BS
        if mesure["TUNISIE"][i] == "Jan":
            BS1.loc[0] = [
                "Janvier", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Feb":
            BS1.loc[1] = [
                "Février", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Mar":
            BS1.loc[2] = [
                "Mars", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(BS1) == 3:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][0] + BS1["VENTEYES"][1] +
                    BS1["VENTEYES"][2],
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMULYES"][0] + BS1["CUMULYES"][1] +
                    BS1["CUMULYES"][2],
                    BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    (BS1["ECART"][0] + BS1["ECART"][1] + BS1["ECART"][2])
                ]
            elif len(BS1) == 2:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][1] + BS1["VENTEYES"][2],
                    BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMULYES"][1] + BS1["CUMULYES"][2],
                    BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    (BS1["ECART"][1] + BS1["ECART"][2])
                ]
            else:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTEYES"][1], BS1["VENTE"][1],
                    BS1["CUMUL"][1], BS1["ECART"][1]
                ]
        #  1 MS
        if mesure["TUNISIE"][i] == "Apr":
            MS1.loc[0] = [
                "Avril", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "May":
            MS1.loc[1] = [
                "Mai", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Jun":
            MS1.loc[2] = [
                "juin", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(MS1) == 3:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTEYES"][0] +
                    MS1["VENTEYES"][1] + MS1["VENTEYES"][2],
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMULYES"][0] + MS1["CUMULYES"][1] +
                    MS1["CUMULYES"][2],
                    MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    (MS1["ECART"][0] + MS1["ECART"][1] + MS1["ECART"][2])
                ]
            elif len(MS1) == 2:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1",
                    MS1["VENTEYES"][1] + MS1["VENTEYES"][2],
                    MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMULYES"][1] + MS1["CUMULYES"][2],
                    MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    (MS1["ECART"][1] + MS1["ECART"][2])
                ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTEYES"][1], MS1["VENTE"][1],
                    MS1["CUMULYES"][1], MS1["CUMUL"][1], MS1["ECART"][1]
                ]
        #  HS
        if mesure["TUNISIE"][i] == "Jul":
            HS.loc[0] = [
                "Juillet", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Aug":
            HS.loc[1] = [
                "Août", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(HS) == 2:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["VENTEYES"][0] + HS["VENTEYES"][1],
                    HS["VENTE"][0] + HS["VENTE"][1],
                    HS["CUMULYES"][0] + HS["CUMULYES"][1],
                    HS["CUMUL"][0] + HS["CUMUL"][1],
                    (HS["ECART"][0] + HS["ECART"][1])
                ]
            else:
                HS.loc[2] = [
                    "HAUTE SAISON", HS["VENTEYES"][1], HS["VENTE"][1],
                    HS["CUMUL"][1], HS["ECART"][1]
                ]
        #  2 MS
        if mesure["TUNISIE"][i] == "Sep":
            MS2.loc[0] = [
                "Septembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Oct":
            MS2.loc[1] = [
                "Octobre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(MS2) == 2:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2",
                    MS2["VENTEYES"][0] + MS2["VENTEYES"][1],
                    MS2["VENTE"][0] + MS2["VENTE"][1],
                    MS2["CUMULYES"][0] + MS2["CUMULYES"][1],
                    MS2["CUMUL"][0] + MS2["CUMUL"][1],
                    (MS2["ECART"][0] + MS2["ECART"][1])
                ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["VENTEYES"][1], MS2["VENTE"][1],
                    MS2["CUMULYES"][1], MS2["CUMUL"][1], MS2["ECART"][1]
                ]
        #  2 BS
        if mesure["TUNISIE"][i] == "Nov":
            BS2.loc[0] = [
                "Novembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
        if mesure["TUNISIE"][i] == "Dec":
            BS2.loc[1] = [
                "Décembre", mesure["VENTEYES"][i], mesure["VENTE"][i],
                mesure["CUMULYES"][i], mesure["CUMUL"][i], mesure["ECART"][i]
            ]
            if len(BS2) == 2:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTEYES"][1] + BS2["VENTEYES"][0],
                    BS2["VENTE"][0] + BS2["VENTE"][1],
                    BS2["CUMULYES"][0] + BS2["CUMULYES"][1],
                    BS2["CUMUL"][0] + BS2["CUMUL"][1],
                    int((((BS2["CUMUL"][0] + BS2["CUMUL"][1]) -
                          (BS2["CUMULYES"][0] + BS2["CUMULYES"][1])) /
                         (BS2["CUMULYES"][0] + BS2["CUMULYES"][1])) * 100)
                ]
            else:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTEYES"][1], BS2["VENTE"][1],
                    BS2["CUMULYES"][1], BS2["CUMUL"][1], BS2["ECART"][1]
                ]

    if len(BS1) != 0 and len(MS1) != 0 and len(HS) != 0 and len(
            MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([BS1, MS1, HS, MS2, BS2])
    elif len(MS1) != 0 and len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS1, HS, MS2, BS2])
    elif len(HS) != 0 and len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([HS, MS2, BS2])
    elif len(MS2) != 0 and len(BS2) != 0:
        reporting = pd.concat([MS2, BS2])
    else:
        reporting = BS2

    reporting = reporting.reset_index(drop=True)

    for i in range(len(reporting)):
        reporting["ECART"][i] = str(reporting["ECART"][i]) + ' %'

    return reporting


# Files stats with Django

def StatCSCInfo(request):
    if request.method == 'POST':
        annee = request.POST["annee"]
        z=cibleCSC.find({'Annee': annee})
        data = pd.DataFrame(columns=['Mois', 'Cible', 'Budget'])
        if cibleCSC.count_documents({'Annee': annee})!=0:
            for i in range(cibleCSC.count_documents({'Annee': annee})):
                data.loc[i]=z[i]["Mois"],z[i]["Cible"],z[i]["Budget"]
        print(data)
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
            z=cibleCSC.count_documents({'Annee': annee, "Mois":MOIS[i]})
            if (z == 0):
                cibleCSC.insert_one({
                "id": i,
                "Annee": annee,
                "Mois": MOIS[i],
                "Cible": CIBLE[i],
                "Budget": BUDGET[i]
            })
            else:
                cibleCSC.update_one({'Annee': annee, "Mois":MOIS[i]},{'$set': {'Cible': CIBLE[i],"Budget": BUDGET[i]}}, upsert=False)

    return HttpResponse(data.to_json(orient='records'))


def StatCSCPLUS(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee = request.POST["annee"]
        print(annee)
        mois = request.POST["mois"]
        print(mois)
        df1 = pd.read_csv(File1, sep=';', index_col=False)
        df2 = pd.read_csv(File2, sep=';', index_col=False)
        MOIS = mois.split(",")
        MOIS = list(map(int, MOIS))
        # Stats
        data = Stat_CSC_plus(df1, df2, annee, MOIS)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))


def StatALG(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee = request.POST["annee"]
        print(annee)
        mois = request.POST["mois"]
        print(mois)
        df1 = pd.read_csv(File1, sep=';', index_col=False)
        print(df1)
        df2 = pd.read_csv(File2, sep=';', index_col=False)
        print(df2)
        MOIS = mois.split(",")
        MOIS = list(map(int, MOIS))
        # Stats
        data = Stat_ALG(df1, df2, annee, MOIS)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))


def StatITA(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee = request.POST["annee"]
        print(annee)
        mois = request.POST["mois"]
        print(mois)
        df1 = pd.read_csv(File1, sep=';', index_col=False)
        print(df1)
        df2 = pd.read_csv(File2, sep=';', index_col=False)
        print(df2)
        MOIS = mois.split(",")
        MOIS = list(map(int, MOIS))
        # Stats
        data = Stat_ITA(df1, df2, annee, MOIS)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))


def StatTUNCL(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee = request.POST["annee"]
        print(annee)
        mois = request.POST["mois"]
        print(mois)
        df1 = pd.read_csv(File1, sep=';', index_col=False)
        print(df1)
        df2 = pd.read_csv(File2, sep=';', index_col=False)
        print(df2)
        MOIS = mois.split(",")
        MOIS = list(map(int, MOIS))
        # Stats
        data = Stat_TUN_CL(df1, df2, annee, MOIS)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))


def StatTUNCTN(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee = request.POST["annee"]
        print(annee)
        mois = request.POST["mois"]
        print(mois)
        df1 = pd.read_csv(File1, sep=';', index_col=False)
        print(df1)
        df2 = pd.read_csv(File2, sep=';', index_col=False)
        print(df2)
        MOIS = mois.split(",")
        MOIS = list(map(int, MOIS))
        # Stats
        data = Stat_TUN_CTN(df1, df2, annee, MOIS)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))
