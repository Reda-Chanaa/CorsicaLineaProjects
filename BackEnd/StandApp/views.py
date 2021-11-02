import calendar
import numpy as np
import pandas as pd
from pathlib import Path
from django.http import HttpResponse


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

    df_mask_cumul['BUDGET'] = budget
    mesure = pd.DataFrame()
    mesure["CORSE"] = df_mask_cumul['MOIS'].apply(
        lambda x: calendar.month_abbr[int(x)])
    mesure["CIBLE"] = cible
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
                    "BASSE SAISON 1", "",
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    round((
                        (BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2]) /
                        (mesure["BUD"][i - 2] + mesure["BUD"][i - 1] +
                         mesure["BUD"][i])) * 100)
                ]
            elif len(BS1) == 2:
                BS1.loc[3] = [
                    "BASSE SAISON 1", "", BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMUL"][1] + BS1["CUMUL"][2],
                    round(((BS1["CUMUL"][1] + BS1["CUMUL"][2]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                BS1.loc[3] = [
                    "BASSE SAISON 1", "", BS1["VENTE"][1], BS1["CUMUL"][1],
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
                    "MOYENNE SAISON 1", "",
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    round((
                        (MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2]) /
                        (mesure["BUD"][i - 2] + mesure["BUD"][i - 1] +
                         mesure["BUD"][i])) * 100)
                ]
            elif len(MS1) == 2:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", "", MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMUL"][1] + MS1["CUMUL"][2],
                    round(((MS1["CUMUL"][1] + MS1["CUMUL"][2]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", "", MS1["VENTE"][1], MS1["CUMUL"][1],
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
                    "HAUTE SAISON 2", "", HS["VENTE"][0] + HS["VENTE"][1],
                    HS["CUMUL"][0] + HS["CUMUL"][1],
                    round(((HS["CUMUL"][0] + HS["CUMUL"][1]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                HS.loc[2] = [
                    "HAUTE SAISON 2", "", HS["VENTE"][1], HS["CUMUL"][1],
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
                    "MOYENNE SAISON 2", "", MS2["VENTE"][0] + MS2["VENTE"][1],
                    MS2["CUMUL"][0] + MS2["CUMUL"][1],
                    round(((MS2["CUMUL"][0] + MS2["CUMUL"][1]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", "", MS2["VENTE"][1], MS2["CUMUL"][1],
                    MS2["BUDGET"][1]
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
                    "BASSE SAISON 2", "", BS2["VENTE"][0] + BS2["VENTE"][1],
                    BS2["CUMUL"][0] + BS2["CUMUL"][1],
                    round(((BS2["CUMUL"][0] + BS2["CUMUL"][1]) /
                           (mesure["BUD"][i - 1] + mesure["BUD"][i])) * 100)
                ]
            else:
                BS2.loc[2] = [
                    "BASSE SAISON 2", "", BS2["VENTE"][1], BS2["CUMUL"][1],
                    BS2["BUDGET"][1]
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

    reporting.reset_index(inplace=True)
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

    BS1 = pd.DataFrame(columns=['CORSE', 'VENTE', "CUMUL"])
    MS1 = pd.DataFrame(columns=['CORSE', 'VENTE', "CUMUL"])
    HS = pd.DataFrame(columns=['CORSE', 'VENTE', "CUMUL"])
    MS2 = pd.DataFrame(columns=['CORSE', 'VENTE', "CUMUL"])
    BS2 = pd.DataFrame(columns=['CORSE', 'VENTE', "CUMUL"])
    for i in mesure.index:
        #  1 BS
        if mesure["CORSE"][i] == "Jan":
            BS1.loc[0] = ["Janvier", mesure["VENTE"][i], mesure["CUMUL"][i]]
        if mesure["CORSE"][i] == "Feb":
            BS1.loc[1] = ["Février", mesure["VENTE"][i], mesure["CUMUL"][i]]
        if mesure["CORSE"][i] == "Mar":
            BS1.loc[2] = ["Mars", mesure["VENTE"][i], mesure["CUMUL"][i]]
            if len(BS1) == 3:
                BS1.loc[3] = [
                    "BASSE SAISON 1",
                    BS1["VENTE"][0] + BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMUL"][0] + BS1["CUMUL"][1] + BS1["CUMUL"][2]
                ]
            elif len(BS1) == 2:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTE"][1] + BS1["VENTE"][2],
                    BS1["CUMUL"][1] + BS1["CUMUL"][2]
                ]
            else:
                BS1.loc[3] = [
                    "BASSE SAISON 1", BS1["VENTE"][1], BS1["CUMUL"][1]
                ]
        #  1 MS
        if mesure["CORSE"][i] == "Apr":
            MS1.loc[0] = ["Avril", mesure["VENTE"][i], mesure["CUMUL"][i]]
        if mesure["CORSE"][i] == "May":
            MS1.loc[1] = ["Mai", mesure["VENTE"][i], mesure["CUMUL"][i]]
        if mesure["CORSE"][i] == "Jun":
            MS1.loc[2] = ["juin", mesure["VENTE"][i], mesure["CUMUL"][i]]
            if len(MS1) == 3:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1",
                    MS1["VENTE"][0] + MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMUL"][0] + MS1["CUMUL"][1] + MS1["CUMUL"][2]
                ]
            elif len(MS1) == 2:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTE"][1] + MS1["VENTE"][2],
                    MS1["CUMUL"][1] + MS1["CUMUL"][2]
                ]
            else:
                MS1.loc[3] = [
                    "MOYENNE SAISON 1", MS1["VENTE"][1], MS1["CUMUL"][1]
                ]
        #  HS
        if mesure["CORSE"][i] == "Jul":
            HS.loc[0] = ["Juillet", mesure["VENTE"][i], mesure["CUMUL"][i]]
        if mesure["CORSE"][i] == "Aug":
            HS.loc[1] = ["Août", mesure["VENTE"][i], mesure["CUMUL"][i]]
            if len(HS) == 2:
                HS.loc[2] = [
                    "HAUTE SAISON 2", HS["VENTE"][0] + HS["VENTE"][1],
                    HS["CUMUL"][0] + HS["CUMUL"][1]
                ]
            else:
                HS.loc[2] = ["HAUTE SAISON 2", HS["VENTE"][1], HS["CUMUL"][1]]
        #  2 MS
        if mesure["CORSE"][i] == "Sep":
            MS2.loc[0] = ["Septembre", mesure["VENTE"][i], mesure["CUMUL"][i]]
        if mesure["CORSE"][i] == "Oct":
            MS2.loc[1] = ["Octobre", mesure["VENTE"][i], mesure["CUMUL"][i]]
            if len(MS2) == 2:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["VENTE"][0] + MS2["VENTE"][1],
                    MS2["CUMUL"][0] + MS2["CUMUL"][1]
                ]
            else:
                MS2.loc[2] = [
                    "MOYENNE SAISON 2", MS2["VENTE"][1], MS2["CUMUL"][1]
                ]
        #  2 BS
        if mesure["CORSE"][i] == "Nov":
            BS2.loc[0] = ["Novembre", mesure["VENTE"][i], mesure["CUMUL"][i]]
        if mesure["CORSE"][i] == "Dec":
            BS2.loc[1] = ["Décembre", mesure["VENTE"][i], mesure["CUMUL"][i]]
            if len(BS2) == 2:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTE"][0] + BS2["VENTE"][1],
                    BS2["CUMUL"][0] + BS2["CUMUL"][1]
                ]
            else:
                BS2.loc[2] = [
                    "BASSE SAISON 2", BS2["VENTE"][1], BS2["CUMUL"][1]
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

    reporting.reset_index(inplace=True)
    del reporting['index']

    return reporting


# Files stats with Django


def StatFile(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee = request.POST["annee"]
        print(annee)
        mois = request.POST["mois"]
        print(mois)
        cible = request.POST["cible"]
        print(cible)
        budget = request.POST["budget"]
        print(budget)
        df1 = pd.read_csv(File1, sep=';', index_col=False)
        print(df1)
        df2 = pd.read_csv(File2, sep=';', index_col=False)
        print(df2)
        MOIS = mois.split(",")
        MOIS = list(map(int, MOIS))
        CIBLE = cible.split(",")
        CIBLE = list(map(int, CIBLE))
        BUDGET = budget.split(",")
        BUDGET = list(map(int, BUDGET))
        # Stats
        data = Stat_CSC(df1, df2, annee, MOIS, CIBLE, BUDGET)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))


def StatFilePlus(request):
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
        data = Stat_CSC_plus(df1, df2, annee, MOIS)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))
