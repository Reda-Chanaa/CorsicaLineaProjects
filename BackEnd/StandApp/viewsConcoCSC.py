from re import I
import time
from django.http import HttpResponse
from datetime import datetime
from datetime import timedelta, date
import pandas as pd
import numpy as np
import datetime
from jours_feries_france import JoursFeries
from vacances_scolaires_france import SchoolHolidayDates

def conco(df1,df_new, annee1, annee2):
    
    fusion1=df1.merge(df_new, how='left', on=['ARM','DEP','ARR','DAY',"MOIS"])
    fusion1=fusion1.dropna(subset=['JOUR_y'])
    fusion1['ARM_y']=fusion1['ARM']
    fusion1['DEP_y']=fusion1['DEP']
    fusion1['MOIS_y']=fusion1['MOIS']
    fusion1['ARR_y']=fusion1['ARR']
    fusion1['DAY_y']=fusion1['DAY']
    fusion1 = fusion1.rename(columns={'DAY':'DAY_x','MOIS': 'MOIS_x','ARM':'ARM_x','DEP':'DEP_x','ARR': 'ARR_x'})
    fusion1.reset_index(inplace=True,drop=True)
    indexNames = fusion1[ ((fusion1['DAY_x'] != 1) | (fusion1['MOIS_x'] != 1)) & ((fusion1['DAY_x'] != 14) | (fusion1['MOIS_x'] != 7)) & ((fusion1['DAY_x'] != 15) | (fusion1['MOIS_x'] != 8)) & ( (fusion1['DAY_x'] != 8) | (fusion1['MOIS_x'] != 5)) & ( (fusion1['DAY_x'] != 1) | (fusion1['MOIS_x'] != 5))& ((fusion1['DAY_x'] != 25) | (fusion1['MOIS_x'] != 12)) & ( (fusion1['DAY_x'] != 11) | (fusion1['MOIS_x'] != 11)) & ( (fusion1['DAY_x'] != 1) | (fusion1['MOIS_x'] != 11)) ].index
    fusion1.drop(indexNames , inplace=True)
    fusion1.reset_index(inplace=True,drop=True)
    
    fusion3=df1.merge(df_new, how='left', on=['ARM','JOUR','DEP','ARR'])
    fusion3=fusion3.dropna(subset=['NAV REF'])
    fusion3['ARM_y']=fusion3['ARM']
    fusion3['DEP_y']=fusion3['DEP']
    fusion3['ARR_y']=fusion3['ARR']
    fusion3['JOUR_y']=fusion3['JOUR']
    fusion3 = fusion3.rename(columns={'JOUR':'JOUR_x','ARM':'ARM_x','DEP':'DEP_x','ARR': 'ARR_x'})
    df4=fusion3.loc[(fusion3['MOIS_x'] == fusion3['MOIS_y']) | (fusion3['MOIS_x'] == fusion3['MOIS_y']+1) | (fusion3['MOIS_y'] == fusion3['MOIS_x']+1)]
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(fusion1['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    indexNames = df4[df4['ID REF'].isin(fusion1['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    pentecote=df4.copy(deep=True)
    pentecoteDatex=JoursFeries.lundi_pentecote(int(annee2))
    pentecoteDatey=JoursFeries.lundi_pentecote(int(annee1))

    indexNames = pentecote[ (((pentecote['DAY_x'] != pentecoteDatex.day-3) | (pentecote['MOIS_x'] != pentecoteDatex.month)) | ((pentecote['DAY_y'] != pentecoteDatey.day-3) | (pentecote['MOIS_y'] != pentecoteDatey.month))) 
    & (((pentecote['DAY_x'] != pentecoteDatex.day-2) | (pentecote['MOIS_x'] != pentecoteDatex.month)) | ((pentecote['DAY_y'] != pentecoteDatey.day-2) | (pentecote['MOIS_y'] != pentecoteDatey.month)))
    & (((pentecote['DAY_x'] != pentecoteDatex.day-1) | (pentecote['MOIS_x'] != pentecoteDatex.month)) | ((pentecote['DAY_y'] != pentecoteDatey.day-1) | (pentecote['MOIS_y'] != pentecoteDatey.month))) 
    & (((pentecote['DAY_x'] != pentecoteDatex.day) | (pentecote['MOIS_x'] != pentecoteDatex.month)) | ((pentecote['DAY_y'] != pentecoteDatey.day) | (pentecote['MOIS_y'] != pentecoteDatey.month))) ].index
    pentecote.drop(indexNames , inplace=True)
    pentecote.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(pentecote['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    indexNames = df4[df4['ID REF'].isin(pentecote['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    paques=df4.copy(deep=True)

    paquesx=JoursFeries.lundi_paques(int(annee2))
    paquesy=JoursFeries.lundi_paques(int(annee1))

    indexNames = paques[ (((paques['DAY_x'] != paquesx.day-3) | (paques['MOIS_x'] != paquesx.month)) | ((paques['DAY_y'] != paquesy.day-3) | (paques['MOIS_y'] != paquesy.month))) 
    & (((paques['DAY_x'] != paquesx.day-2) | (paques['MOIS_x'] != paquesx.month)) | ((paques['DAY_y'] != paquesy.day-2) | (paques['MOIS_y'] != paquesy.month)))
    & (((paques['DAY_x'] != paquesx.day-1) | (paques['MOIS_x'] != paquesx.month)) | ((paques['DAY_y'] != paquesy.day-1) | (paques['MOIS_y'] != paquesy.month))) 
    & (((paques['DAY_x'] != paquesx.day) | (paques['MOIS_x'] != paquesx.month)) | ((paques['DAY_y'] != paquesy.day) | (paques['MOIS_y'] != paquesy.month))) ].index
    paques.drop(indexNames , inplace=True)
    paques.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(paques['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    indexNames = df4[df4['ID REF'].isin(paques['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    ascension=df4.copy(deep=True)

    ascensionx=JoursFeries.ascension(int(annee2))
    ascensiony=JoursFeries.ascension(int(annee1))

    indexNames = ascension[ (((ascension['DAY_x'] != ascensionx.day-1) | (ascension['MOIS_x'] != ascensionx.month)) | ((ascension['DAY_y'] != ascensiony.day-1) | (ascension['MOIS_y'] != ascensiony.month))) 
    & (((ascension['DAY_x'] != ascensionx.day) | (ascension['MOIS_x'] != ascensionx.month)) | ((ascension['DAY_y'] != ascensiony.day) | (ascension['MOIS_y'] != ascensiony.month)))
    & (((ascension['DAY_x'] != ascensionx.day+1) | (ascension['MOIS_x'] != ascensionx.month)) | ((ascension['DAY_y'] != ascensiony.day+1) | (ascension['MOIS_y'] != ascensiony.month))) 
    & (((ascension['DAY_x'] != ascensionx.day+2) | (ascension['MOIS_x'] != ascensionx.month)) | ((ascension['DAY_y'] != ascensiony.day+2) | (ascension['MOIS_y'] != ascensiony.month)))
    & (((ascension['DAY_x'] != ascensionx.day+3) | (ascension['MOIS_x'] != ascensionx.month)) | ((ascension['DAY_y'] != ascensiony.day+3) | (ascension['MOIS_y'] != ascensiony.month))) ].index
    ascension.drop(indexNames , inplace=True)
    ascension.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(ascension['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    indexNames = df4[df4['ID REF'].isin(ascension['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    ete=df4.copy(deep=True)
    print('------------------- été')

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee1), 'A')
    elsA = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances d'Ã©tÃ©"):
            elsA=elsA.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee1), 'B')
    elsB = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances d'Ã©tÃ©"):
            elsB=elsB.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee1), 'C')
    elsC = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances d'Ã©tÃ©"):
            elsC=elsC.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee2), 'A')
    els_A = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances d'Ã©tÃ©"):
            els_A=els_A.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee2), 'B')
    els_B = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances d'Ã©tÃ©"):
            els_B=els_B.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee2), 'C')
    els_C = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances d'Ã©tÃ©"):
            els_C=els_C.append({'date': test[0]}, ignore_index=True)

    start_date_2021 = date(els_A['date'][0].year, els_A['date'][0].month, els_A['date'][0].day)
    end_date_2021 = date(els_A['date'][len(els_A)-1].year, els_A['date'][len(els_A)-1].month, els_A['date'][len(els_A)-1].day)
    start_date_2022 = date(elsA['date'][0].year, elsA['date'][0].month, elsA['date'][0].day-1)
    end_date_2022 = date(elsA['date'][len(elsA)-1].year, elsA['date'][len(elsA)-1].month, elsA['date'][len(elsA)-1].day)

    start_date_B_2021 = date(els_B['date'][0].year, els_B['date'][0].month, els_B['date'][0].day)
    end_date_B_2021 = date(els_B['date'][len(els_B)-1].year, els_B['date'][len(els_B)-1].month, els_B['date'][len(els_B)-1].day)
    start_date_B_2022 = date(elsB['date'][0].year, elsB['date'][0].month, elsB['date'][0].day-1)
    end_date_B_2022 = date(elsB['date'][len(elsB)-1].year, elsB['date'][len(elsB)-1].month, elsB['date'][len(elsB)-1].day)

    start_date_C_2021=date(els_C['date'][0].year, els_C['date'][0].month, els_C['date'][0].day)
    end_date_C_2021 = date(els_C['date'][len(els_C)-1].year, els_C['date'][len(els_C)-1].month, els_C['date'][len(els_C)-1].day)
    start_date_C_2022 = date(elsC['date'][0].year, elsC['date'][0].month, elsC['date'][0].day-1)
    end_date_C_2022 = date(elsC['date'][len(elsC)-1].year, elsC['date'][len(elsC)-1].month, elsC['date'][len(elsC)-1].day)

    '''
    eteA=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'A',"Vacances d'été")
    #print(eteA)
    eteB=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'B',"Vacances d'été")
    #print(eteB)
    eteC=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'C',"Vacances d'été")
    #print(eteC)

    ete_A=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'A',"Vacances d'été")
    #print(ete_A)
    ete_B=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'B',"Vacances d'été")
    #print(ete_B)
    ete_C=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'C',"Vacances d'été")
    #print(ete_C)

    elsA = list(eteA.items())
    elsB = list(eteB.items())
    elsC = list(eteC.items())

    els_A = list(ete_A.items())
    els_B = list(ete_B.items())
    els_C = list(ete_C.items())

   
    
    start_date_2021 = date(2021, 7, 8)
    end_date_2021 = date(2021, 9, 1)
    start_date_2022 = date(2022, 7, 7)
    end_date_2022 = date(2022, 8, 31)
    '''
    
    if (int ((end_date_2021 - start_date_2021).days)) > (int ((end_date_2022 - start_date_2022).days)):
        print("yes")
    elif (int ((end_date_2021 - start_date_2021).days)) < (int ((end_date_2022 - start_date_2022).days)):
        print("no")
    else:
        vac_ete=pd.DataFrame()
        for n in range(int ((end_date_2021 - start_date_2021).days)):
            ete=df4.copy(deep=True)
            if n==0:
                indexNames=ete[(((ete['DAY_x'] != start_date_2021.day) | (ete['MOIS_x'] != start_date_2021.month)) | ((ete['DAY_y'] != start_date_2022.day) | (ete['MOIS_y'] != start_date_2022.month)))].index
                ete.drop(indexNames , inplace=True)
                ete.reset_index(inplace=True,drop=True)
                frames = [ete,vac_ete]
                vac_ete = pd.concat(frames)
                vac_ete.reset_index(inplace=True,drop=True) 
            else:
                indexNames=ete[(((ete['DAY_x'] != (start_date_2021 + timedelta(n)).day) | (ete['MOIS_x'] != (start_date_2021 + timedelta(n)).month)) | ((ete['DAY_y'] != (start_date_2022 + timedelta(n)).day) | (ete['MOIS_y'] != (start_date_2022 + timedelta(n)).month)))].index
                ete.drop(indexNames , inplace=True)
                ete.reset_index(inplace=True,drop=True)
                frames = [ete,vac_ete]
                vac_ete = pd.concat(frames)
                vac_ete.reset_index(inplace=True,drop=True)

    shipswitch=vac_ete.copy(deep=True)
    indexNames=shipswitch[(((shipswitch['NAV'] == "NEPI") & (shipswitch['JOUR_x'] == "dimanche") & (shipswitch['NAV REF'] == 'NEPI'))) | (((shipswitch['NAV'] == "NOLI") & (shipswitch['JOUR_x'] == "dimanche") & (shipswitch['NAV REF'] == 'ORBA')))].index

    shipswitch.drop(indexNames , inplace=True)
    shipswitch.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(shipswitch['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    indexNames = df4[df4['ID REF'].isin(shipswitch['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    print('------------------- printemps')
    printempsA=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'A',"Vacances de printemps")
    printempsB=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'B',"Vacances de printemps")
    printempsC=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'C',"Vacances de printemps")

    printemps_A=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'A',"Vacances de printemps")
    printemps_B=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'B',"Vacances de printemps")
    printemps_C=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'C',"Vacances de printemps")
    
    elsA = list(printempsA.items())
    elsB = list(printempsB.items())
    elsC = list(printempsC.items())

    els_A = list(printemps_A.items())
    els_B = list(printemps_B.items())
    els_C = list(printemps_C.items())

    start_date_A_2021 = date(els_A[0][0].year, els_A[0][0].month, els_A[0][0].day-1)
    end_date_A_2021 = date(els_A[-1][0].year, els_A[-1][0].month, els_A[-1][0].day)
    start_date_A_2022 = date(elsA[0][0].year, elsA[0][0].month, elsA[0][0].day-1)
    end_date_A_2022 = date(elsA[-1][0].year, elsA[-1][0].month, elsA[-1][0].day)

    start_date_B_2021 = date(els_B[0][0].year, els_B[0][0].month, els_B[0][0].day-1)
    end_date_B_2021 = date(els_B[-1][0].year, els_B[-1][0].month, els_B[-1][0].day)
    start_date_B_2022 = date(elsB[0][0].year, elsB[0][0].month, elsB[0][0].day-1)
    end_date_B_2022 = date(elsB[-1][0].year, elsB[-1][0].month, elsB[-1][0].day)

    start_date_C_2021=date(els_C[0][0].year, els_C[0][0].month, els_C[0][0].day-1)
    end_date_C_2021 = date(els_C[-1][0].year, els_C[-1][0].month, els_C[-1][0].day)
    start_date_C_2022 = date(elsC[0][0].year, elsC[0][0].month, elsC[0][0].day-1)
    end_date_C_2022 = date(elsC[-1][0].year, elsC[-1][0].month, elsC[-1][0].day)

    if (int ((end_date_B_2021 - start_date_B_2021).days)) > (int ((end_date_B_2022 - start_date_B_2022).days)):
        print("bigger")
    elif (int ((end_date_B_2021 - start_date_B_2021).days)) < (int ((end_date_B_2022 - start_date_B_2022).days)):
        print("smaller")
    else:
        vac_printemps_B=pd.DataFrame()
        for n in range(int((end_date_B_2021 - start_date_B_2021).days)):
            printempsB=df4.copy(deep=True)
            if n==0:
                indexNames=printempsB[(((printempsB['DAY_x'] != start_date_B_2021.day) | (printempsB['MOIS_x'] != start_date_B_2021.month)) | ((printempsB['DAY_y'] != start_date_B_2022.day) | (printempsB['MOIS_y'] != start_date_B_2022.month)))].index
                printempsB.drop(indexNames , inplace=True)
                printempsB.reset_index(inplace=True,drop=True)
                frames = [printempsB,vac_printemps_B]
                vac_printemps_B = pd.concat(frames)
                vac_printemps_B.reset_index(inplace=True,drop=True) 
            else:
                indexNames=printempsB[(((printempsB['DAY_x'] != (start_date_B_2021 + timedelta(n)).day) | (printempsB['MOIS_x'] != (start_date_B_2021 + timedelta(n)).month)) | ((printempsB['DAY_y'] != (start_date_B_2022 + timedelta(n)).day) | (printempsB['MOIS_y'] != (start_date_B_2022 + timedelta(n)).month)))].index
                printempsB.drop(indexNames , inplace=True)
                printempsB.reset_index(inplace=True,drop=True)
                frames = [printempsB,vac_printemps_B]
                vac_printemps_B = pd.concat(frames)
                vac_printemps_B.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_printemps_B['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_printemps_B['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    
    if (int ((end_date_C_2021 - start_date_C_2021).days)) > (int ((end_date_C_2022 - start_date_C_2022).days)):
        print("bigger")
    elif (int ((end_date_C_2021 - start_date_C_2021).days)) < (int ((end_date_C_2022 - start_date_C_2022).days)):
        print("smaller")
    else:
        vac_printemps_C=pd.DataFrame()
    for n in range(int((end_date_C_2021 - start_date_C_2021).days)):
        printempsC=df4.copy(deep=True)
        if n==0:
            indexNames=printempsC[(((printempsC['DAY_x'] != start_date_C_2021.day) | (printempsC['MOIS_x'] != start_date_C_2021.month)) | ((printempsC['DAY_y'] != start_date_C_2022.day) | (printempsC['MOIS_y'] != start_date_C_2022.month)))].index
            printempsC.drop(indexNames , inplace=True)
            printempsC.reset_index(inplace=True,drop=True)
            frames = [printempsC,vac_printemps_C]
            vac_printemps_C = pd.concat(frames)
            vac_printemps_C.reset_index(inplace=True,drop=True) 
        else:
            indexNames=printempsC[(((printempsC['DAY_x'] != (start_date_C_2021 + timedelta(n)).day) | (printempsC['MOIS_x'] != (start_date_C_2021 + timedelta(n)).month)) | ((printempsC['DAY_y'] != (start_date_C_2022 + timedelta(n)).day) | (printempsC['MOIS_y'] != (start_date_C_2022 + timedelta(n)).month)))].index
            printempsC.drop(indexNames , inplace=True)
            printempsC.reset_index(inplace=True,drop=True)
            frames = [printempsC,vac_printemps_C]
            vac_printemps_C = pd.concat(frames)
            vac_printemps_C.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_printemps_C['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_printemps_C['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    if (int ((end_date_A_2021 - start_date_A_2021).days)) > (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("bigger")
    elif (int ((end_date_A_2021 - start_date_A_2021).days)) < (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("smaller")
    else:
        vac_printemps_A=pd.DataFrame()
        for n in range(int((end_date_A_2021 - start_date_A_2021).days)):
            printempsA=df4.copy(deep=True)
            if n==0:
                indexNames=printempsA[(((printempsA['DAY_x'] != start_date_A_2021.day) | (printempsA['MOIS_x'] != start_date_A_2021.month)) | ((printempsA['DAY_y'] != start_date_A_2022.day) | (printempsA['MOIS_y'] != start_date_A_2022.month)))].index
                printempsA.drop(indexNames , inplace=True)
                printempsA.reset_index(inplace=True,drop=True)
                frames = [printempsA,vac_printemps_A]
                vac_printemps_A = pd.concat(frames)
                vac_printemps_A.reset_index(inplace=True,drop=True) 
            else:
                indexNames=printempsA[(((printempsA['DAY_x'] != (start_date_A_2021 + timedelta(n)).day) | (printempsA['MOIS_x'] != (start_date_A_2021 + timedelta(n)).month)) | ((printempsA['DAY_y'] != (start_date_A_2022 + timedelta(n)).day) | (printempsA['MOIS_y'] != (start_date_A_2022 + timedelta(n)).month)))].index
                printempsA.drop(indexNames , inplace=True)
                printempsA.reset_index(inplace=True,drop=True)
                frames = [printempsA,vac_printemps_A]
                vac_printemps_A = pd.concat(frames)
                vac_printemps_A.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_printemps_A['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_printemps_A['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    print('------------------- hiver')
    hiverA=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'A',"Vacances d'hiver")
    hiverB=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'B',"Vacances d'hiver")
    hiverC=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'C',"Vacances d'hiver")

    hiver_A=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'A',"Vacances d'hiver")
    hiver_B=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'B',"Vacances d'hiver")
    hiver_C=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'C',"Vacances d'hiver")
    
    elsA = list(hiverA.items())
    elsB = list(hiverB.items())
    elsC = list(hiverC.items())

    els_A = list(hiver_A.items())
    els_B = list(hiver_B.items())
    els_C = list(hiver_C.items())

    start_date_A_2021 = date(els_A[0][0].year, els_A[0][0].month, els_A[0][0].day-1)
    end_date_A_2021 = date(els_A[-1][0].year, els_A[-1][0].month, els_A[-1][0].day)
    start_date_A_2022 = date(elsA[0][0].year, elsA[0][0].month, elsA[0][0].day-1)
    end_date_A_2022 = date(elsA[-1][0].year, elsA[-1][0].month, elsA[-1][0].day)

    start_date_B_2021 = date(els_B[0][0].year, els_B[0][0].month, els_B[0][0].day-1)
    end_date_B_2021 = date(els_B[-1][0].year, els_B[-1][0].month, els_B[-1][0].day)
    start_date_B_2022 = date(elsB[0][0].year, elsB[0][0].month, elsB[0][0].day-1)
    end_date_B_2022 = date(elsB[-1][0].year, elsB[-1][0].month, elsB[-1][0].day)

    start_date_C_2021=date(els_C[0][0].year, els_C[0][0].month, els_C[0][0].day-1)
    end_date_C_2021 = date(els_C[-1][0].year, els_C[-1][0].month, els_C[-1][0].day)
    start_date_C_2022 = date(elsC[0][0].year, elsC[0][0].month, elsC[0][0].day-1)
    end_date_C_2022 = date(elsC[-1][0].year, elsC[-1][0].month, elsC[-1][0].day)

    # zone c
    if (int ((end_date_C_2021 - start_date_C_2021).days)) > (int ((end_date_C_2022 - start_date_C_2022).days)):
        print("bigger")
    elif (int ((end_date_C_2021 - start_date_C_2021).days)) < (int ((end_date_C_2022 - start_date_C_2022).days)):
        print("smaller")
    else:
        vac_hiver_C=pd.DataFrame()
        for n in range(int((end_date_C_2021 - start_date_C_2021).days)):
            hiverC=df4.copy(deep=True)
            if n==0:
                indexNames=hiverC[(((hiverC['DAY_x'] != start_date_C_2021.day) | (hiverC['MOIS_x'] != start_date_C_2021.month)) | ((hiverC['DAY_y'] != start_date_C_2022.day) | (hiverC['MOIS_y'] != start_date_C_2022.month)))].index
                hiverC.drop(indexNames , inplace=True)
                hiverC.reset_index(inplace=True,drop=True)
                frames = [hiverC,vac_hiver_C]
                vac_hiver_C = pd.concat(frames)
                vac_hiver_C.reset_index(inplace=True,drop=True) 
            else:
                indexNames=hiverC[(((hiverC['DAY_x'] != (start_date_C_2021 + timedelta(n)).day) | (hiverC['MOIS_x'] != (start_date_C_2021 + timedelta(n)).month)) | ((hiverC['DAY_y'] != (start_date_C_2022 + timedelta(n)).day) | (hiverC['MOIS_y'] != (start_date_C_2022 + timedelta(n)).month)))].index
                hiverC.drop(indexNames , inplace=True)
                hiverC.reset_index(inplace=True,drop=True)
                frames = [hiverC,vac_hiver_C]
                vac_hiver_C = pd.concat(frames)
                vac_hiver_C.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_hiver_C['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_hiver_C['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    # zone B
    if (int ((end_date_B_2021 - start_date_B_2021).days)) > (int ((end_date_B_2022 - start_date_B_2022).days)):
        print("bigger")
    elif (int ((end_date_B_2021 - start_date_B_2021).days)) < (int ((end_date_B_2022 - start_date_B_2022).days)):
        print("smaller")
    else:
        vac_hiver_B=pd.DataFrame()
        for n in range(int((end_date_B_2021 - start_date_B_2021).days)):
            hiverB=df4.copy(deep=True)
            if n==0:
                indexNames=hiverB[(((hiverB['DAY_x'] != start_date_B_2021.day) | (hiverB['MOIS_x'] != start_date_B_2021.month)) | ((hiverB['DAY_y'] != start_date_B_2022.day) | (hiverB['MOIS_y'] != start_date_B_2022.month)))].index
                hiverB.drop(indexNames , inplace=True)
                hiverB.reset_index(inplace=True,drop=True)
                frames = [hiverB,vac_hiver_B]
                vac_hiver_B = pd.concat(frames)
                vac_hiver_B.reset_index(inplace=True,drop=True) 
            else:
                indexNames=hiverB[(((hiverB['DAY_x'] != (start_date_B_2021 + timedelta(n)).day) | (hiverB['MOIS_x'] != (start_date_B_2021 + timedelta(n)).month)) | ((hiverB['DAY_y'] != (start_date_B_2022 + timedelta(n)).day) | (hiverB['MOIS_y'] != (start_date_B_2022 + timedelta(n)).month)))].index
                hiverB.drop(indexNames , inplace=True)
                hiverB.reset_index(inplace=True,drop=True)
                frames = [hiverB,vac_hiver_B]
                vac_hiver_B = pd.concat(frames)
                vac_hiver_B.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_hiver_B['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_hiver_B['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    # zone A

    if (int ((end_date_A_2021 - start_date_A_2021).days)) > (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("bigger")
    elif (int ((end_date_A_2021 - start_date_A_2021).days)) < (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("smaller")
    else:
        vac_hiver_A=pd.DataFrame()
        for n in range(int((end_date_A_2021 - start_date_A_2021).days)):
            hiverA=df4.copy(deep=True)
            if n==0:
                indexNames=hiverA[(((hiverA['DAY_x'] != start_date_A_2021.day) | (hiverA['MOIS_x'] != start_date_A_2021.month)) | ((hiverA['DAY_y'] != start_date_A_2022.day) | (hiverA['MOIS_y'] != start_date_A_2022.month)))].index
                hiverA.drop(indexNames , inplace=True)
                hiverA.reset_index(inplace=True,drop=True)
                frames = [hiverA,vac_hiver_A]
                vac_hiver_A = pd.concat(frames)
                vac_hiver_A.reset_index(inplace=True,drop=True) 
            else:
                indexNames=hiverA[(((hiverA['DAY_x'] != (start_date_A_2021 + timedelta(n)).day) | (hiverA['MOIS_x'] != (start_date_A_2021 + timedelta(n)).month)) | ((hiverA['DAY_y'] != (start_date_A_2022 + timedelta(n)).day) | (hiverA['MOIS_y'] != (start_date_A_2022 + timedelta(n)).month)))].index
                hiverA.drop(indexNames , inplace=True)
                hiverA.reset_index(inplace=True,drop=True)
                frames = [hiverA,vac_hiver_A]
                vac_hiver_A = pd.concat(frames)
                vac_hiver_A.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_hiver_A['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_hiver_A['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    print('------------------- octobre')
    tousaintA=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'A','Vacances de la Toussaint')
    tousaintB=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'B','Vacances de la Toussaint')
    tousaintC=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee1),'C','Vacances de la Toussaint')

    tousaint_A=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'A','Vacances de la Toussaint')
    tousaint_B=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'B','Vacances de la Toussaint')
    tousaint_C=SchoolHolidayDates().holidays_for_year_zone_and_name(int(annee2),'C','Vacances de la Toussaint')
    
    elsA = list(tousaintA.items())
    elsB = list(tousaintB.items())
    elsC = list(tousaintC.items())

    els_A = list(tousaint_A.items())
    els_B = list(tousaint_B.items())
    els_C = list(tousaint_C.items())

    # Octobre
    start_date_A_2021 = date(els_A[0][0].year, els_A[0][0].month, els_A[0][0].day-1)
    end_date_A_2021 = date(els_A[-1][0].year, els_A[-1][0].month, els_A[-1][0].day)
    start_date_A_2022 = date(elsA[0][0].year, elsA[0][0].month, elsA[0][0].day-1)
    end_date_A_2022 = date(elsA[-1][0].year, elsA[-1][0].month, elsA[-1][0].day)

    start_date_B_2021 = date(els_B[0][0].year, els_B[0][0].month, els_B[0][0].day-1)
    end_date_B_2021 = date(els_B[-1][0].year, els_B[-1][0].month, els_B[-1][0].day)
    start_date_B_2022 = date(elsB[0][0].year, elsB[0][0].month, elsB[0][0].day-1)
    end_date_B_2022 = date(elsB[-1][0].year, elsB[-1][0].month, elsB[-1][0].day)

    start_date_C_2021=date(els_C[0][0].year, els_C[0][0].month, els_C[0][0].day-1)
    end_date_C_2021 = date(els_C[-1][0].year, els_C[-1][0].month, els_C[-1][0].day)
    start_date_C_2022 = date(elsC[0][0].year, elsC[0][0].month, elsC[0][0].day-1)
    end_date_C_2022 = date(elsC[-1][0].year, elsC[-1][0].month, elsC[-1][0].day)


    # zone c
    if (int ((end_date_C_2021 - start_date_C_2021).days)) > (int ((end_date_C_2022 - start_date_C_2022).days)):
        print("bigger")
    elif (int ((end_date_C_2021 - start_date_C_2021).days)) < (int ((end_date_C_2022 - start_date_C_2022).days)):
        print("smaller")
    else:
        vac_oct_C=pd.DataFrame()
        for n in range(int((end_date_C_2021 - start_date_C_2021).days)):
            octC=df4.copy(deep=True)
            if n==0:
                indexNames=octC[(((octC['DAY_x'] != start_date_C_2021.day) | (octC['MOIS_x'] != start_date_C_2021.month)) | ((octC['DAY_y'] != start_date_C_2022.day) | (octC['MOIS_y'] != start_date_C_2022.month)))].index
                octC.drop(indexNames , inplace=True)
                octC.reset_index(inplace=True,drop=True)
                frames = [octC,vac_oct_C]
                vac_oct_C = pd.concat(frames)
                vac_oct_C.reset_index(inplace=True,drop=True) 
            else:
                indexNames=octC[(((octC['DAY_x'] != (start_date_C_2021 + timedelta(n)).day) | (octC['MOIS_x'] != (start_date_C_2021 + timedelta(n)).month)) | ((octC['DAY_y'] != (start_date_C_2022 + timedelta(n)).day) | (octC['MOIS_y'] != (start_date_C_2022 + timedelta(n)).month)))].index
                octC.drop(indexNames , inplace=True)
                octC.reset_index(inplace=True,drop=True)
                frames = [octC,vac_oct_C]
                vac_oct_C = pd.concat(frames)
                vac_oct_C.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_oct_C['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_oct_C['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    # zone B
    if (int ((end_date_B_2021 - start_date_B_2021).days)) > (int ((end_date_B_2022 - start_date_B_2022).days)):
        print("bigger")
    elif (int ((end_date_B_2021 - start_date_B_2021).days)) < (int ((end_date_B_2022 - start_date_B_2022).days)):
        print("smaller")
    else:
        vac_oct_B=pd.DataFrame()
        for n in range(int((end_date_B_2021 - start_date_B_2021).days)):
            octB=df4.copy(deep=True)
            if n==0:
                indexNames=octB[(((octB['DAY_x'] != start_date_B_2021.day) | (octB['MOIS_x'] != start_date_B_2021.month)) | ((octB['DAY_y'] != start_date_B_2022.day) | (octB['MOIS_y'] != start_date_B_2022.month)))].index
                octB.drop(indexNames , inplace=True)
                octB.reset_index(inplace=True,drop=True)
                frames = [octB,vac_oct_B]
                vac_oct_B = pd.concat(frames)
                vac_oct_B.reset_index(inplace=True,drop=True) 
            else:
                indexNames=octB[(((octB['DAY_x'] != (start_date_B_2021 + timedelta(n)).day) | (octB['MOIS_x'] != (start_date_B_2021 + timedelta(n)).month)) | ((octB['DAY_y'] != (start_date_B_2022 + timedelta(n)).day) | (octB['MOIS_y'] != (start_date_B_2022 + timedelta(n)).month)))].index
                octB.drop(indexNames , inplace=True)
                octB.reset_index(inplace=True,drop=True)
                frames = [octB,vac_oct_B]
                vac_oct_B = pd.concat(frames)
                vac_oct_B.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_oct_B['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_oct_B['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    # zone A

    if (int ((end_date_A_2021 - start_date_A_2021).days)) > (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("bigger")
    elif (int ((end_date_A_2021 - start_date_A_2021).days)) < (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("smaller")
    else:
        vac_oct_A=pd.DataFrame()
        for n in range(int((end_date_A_2021 - start_date_A_2021).days)):
            octA=df4.copy(deep=True)
            if n==0:
                indexNames=octA[(((octA['DAY_x'] != start_date_A_2021.day) | (octA['MOIS_x'] != start_date_A_2021.month)) | ((octA['DAY_y'] != start_date_A_2022.day) | (octA['MOIS_y'] != start_date_A_2022.month)))].index
                octA.drop(indexNames , inplace=True)
                octA.reset_index(inplace=True,drop=True)
                frames = [octA,vac_oct_A]
                vac_oct_A = pd.concat(frames)
                vac_oct_A.reset_index(inplace=True,drop=True) 
            else:
                indexNames=octA[(((octA['DAY_x'] != (start_date_A_2021 + timedelta(n)).day) | (octA['MOIS_x'] != (start_date_A_2021 + timedelta(n)).month)) | ((octA['DAY_y'] != (start_date_A_2022 + timedelta(n)).day) | (octA['MOIS_y'] != (start_date_A_2022 + timedelta(n)).month)))].index
                octA.drop(indexNames , inplace=True)
                octA.reset_index(inplace=True,drop=True)
                frames = [octA,vac_oct_A]
                vac_oct_A = pd.concat(frames)
                vac_oct_A.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_oct_A['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_oct_A['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    print('------------------- Noël')

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee1), 'A')
    elsA = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==12):
                elsA=elsA.append({'date': test[0]}, ignore_index=True)
    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee1)+1, 'A')
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==1):
                elsA=elsA.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee1), 'B')
    elsB = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==12):
                elsB=elsB.append({'date': test[0]}, ignore_index=True)
    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee1)+1, 'B')
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==1):
                elsB=elsB.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee1), 'C')
    elsC = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==12):
                elsC=elsC.append({'date': test[0]}, ignore_index=True)
    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee1)+1, 'C')
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==1):
                elsC=elsC.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee2), 'A')
    els_A = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==12):
                els_A=els_A.append({'date': test[0]}, ignore_index=True)
    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee2)+1, 'A')
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==1):
                els_A=els_A.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee2), 'B')
    els_B = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==12):
                els_B=els_B.append({'date': test[0]}, ignore_index=True)
    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee2)+1, 'B')
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==1):
                els_B=els_B.append({'date': test[0]}, ignore_index=True)

    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee2), 'C')
    els_C = pd.DataFrame(columns=['date'])
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==12):
                els_C=els_C.append({'date': test[0]}, ignore_index=True)
    items=SchoolHolidayDates().holidays_for_year_and_zone(int(annee2)+1, 'C')
    for key, value in items.items():
        test=list(value.values())
        if(test[4]=="Vacances de NoÃ«l"):
            if(test[0].month==1):
                els_C=els_C.append({'date': test[0]}, ignore_index=True)

    print(els_A['date'])
    print(elsA['date'])
    start_date_A_2021 = date(els_A['date'][0].year, els_A['date'][0].month, els_A['date'][0].day-2)
    end_date_A_2021 = date(els_A['date'][len(els_A)-1].year, els_A['date'][len(els_A)-1].month, els_A['date'][len(els_A)-1].day)
    start_date_A_2022 = date(elsA['date'][0].year, elsA['date'][0].month, elsA['date'][0].day-1)
    end_date_A_2022 = date(elsA['date'][len(elsA)-1].year, elsA['date'][len(elsA)-1].month, elsA['date'][len(elsA)-1].day)

    start_date_B_2021 = date(els_B['date'][0].year, els_B['date'][0].month, els_B['date'][0].day-2)
    end_date_B_2021 = date(els_B['date'][len(els_B)-1].year, els_B['date'][len(els_B)-1].month, els_B['date'][len(els_B)-1].day)
    start_date_B_2022 = date(elsB['date'][0].year, elsB['date'][0].month, elsB['date'][0].day-1)
    end_date_B_2022 = date(elsB['date'][len(elsB)-1].year, elsB['date'][len(elsB)-1].month, elsB['date'][len(elsB)-1].day)

    start_date_C_2021=date(els_C['date'][0].year, els_C['date'][0].month, els_C['date'][0].day-2)
    end_date_C_2021 = date(els_C['date'][len(els_C)-1].year, els_C['date'][len(els_C)-1].month, els_C['date'][len(els_C)-1].day)
    start_date_C_2022 = date(elsC['date'][0].year, elsC['date'][0].month, elsC['date'][0].day-1)
    end_date_C_2022 = date(elsC['date'][len(elsC)-1].year, elsC['date'][len(elsC)-1].month, elsC['date'][len(elsC)-1].day)

    '''
    
    
    # Decembre

    
    start_date_A_2021 = date(2021, 12, 17)
    end_date_A_2021 = date(2022, 1, 2)
    start_date_A_2022 = date(2022, 12, 16)
    end_date_A_2022 = date(2023, 1, 1)

    start_date_B_2021 = date(2021, 12, 17)
    end_date_B_2021 = date(2022, 1, 2)
    start_date_B_2022 = date(2022, 12, 16)
    end_date_B_2022 = date(2023, 1, 1)

    start_date_C_2021 = date(2021, 12, 17)
    end_date_C_2021 = date(2022, 1, 2)
    start_date_C_2022 = date(2022, 12, 16)
    end_date_C_2022 = date(2023, 1, 1)'''

    # zone c
    if (int ((end_date_C_2021 - start_date_C_2021).days)) > (int ((end_date_C_2022 - start_date_C_2022).days)):
        print("bigger")
    elif (int ((end_date_C_2021 - start_date_C_2021).days)) < (int ((end_date_C_2022 - start_date_C_2022).days)):
        print("smaller")
    else:
        vac_dec_C=pd.DataFrame()
        for n in range(int((end_date_C_2021 - start_date_C_2021).days)):
            decC=df4.copy(deep=True)
            if n==0:
                indexNames=decC[(((decC['DAY_x'] != start_date_C_2021.day) | (decC['MOIS_x'] != start_date_C_2021.month)) | ((decC['DAY_y'] != start_date_C_2022.day) | (decC['MOIS_y'] != start_date_C_2022.month)))].index
                decC.drop(indexNames , inplace=True)
                decC.reset_index(inplace=True,drop=True)
                frames = [decC,vac_dec_C]
                vac_dec_C = pd.concat(frames)
                vac_dec_C.reset_index(inplace=True,drop=True) 
            else:
                indexNames=decC[(((decC['DAY_x'] != (start_date_C_2021 + timedelta(n)).day) | (decC['MOIS_x'] != (start_date_C_2021 + timedelta(n)).month)) | ((decC['DAY_y'] != (start_date_C_2022 + timedelta(n)).day) | (decC['MOIS_y'] != (start_date_C_2022 + timedelta(n)).month)))].index
                decC.drop(indexNames , inplace=True)
                decC.reset_index(inplace=True,drop=True)
                frames = [decC,vac_dec_C]
                vac_dec_C = pd.concat(frames)
                vac_dec_C.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_dec_C['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_dec_C['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    # zone B
    if (int ((end_date_B_2021 - start_date_B_2021).days)) > (int ((end_date_B_2022 - start_date_B_2022).days)):
        print("bigger")
    elif (int ((end_date_B_2021 - start_date_B_2021).days)) < (int ((end_date_B_2022 - start_date_B_2022).days)):
        print("smaller")
    else:
        vac_dec_B=pd.DataFrame()
        for n in range(int((end_date_B_2021 - start_date_B_2021).days)):
            decB=df4.copy(deep=True)
            if n==0:
                indexNames=decB[(((decB['DAY_x'] != start_date_B_2021.day) | (decB['MOIS_x'] != start_date_B_2021.month)) | ((decB['DAY_y'] != start_date_B_2022.day) | (decB['MOIS_y'] != start_date_B_2022.month)))].index
                decB.drop(indexNames , inplace=True)
                decB.reset_index(inplace=True,drop=True)
                frames = [decB,vac_dec_B]
                vac_dec_B = pd.concat(frames)
                vac_dec_B.reset_index(inplace=True,drop=True) 
            else:
                indexNames=decB[(((decB['DAY_x'] != (start_date_B_2021 + timedelta(n)).day) | (decB['MOIS_x'] != (start_date_B_2021 + timedelta(n)).month)) | ((decB['DAY_y'] != (start_date_B_2022 + timedelta(n)).day) | (decB['MOIS_y'] != (start_date_B_2022 + timedelta(n)).month)))].index
                decB.drop(indexNames , inplace=True)
                decB.reset_index(inplace=True,drop=True)
                frames = [decB,vac_dec_B]
                vac_dec_B = pd.concat(frames)
                vac_dec_B.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(vac_dec_B['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_dec_B['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    # zone A

    if (int ((end_date_A_2021 - start_date_A_2021).days)) > (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("bigger")
    elif (int ((end_date_A_2021 - start_date_A_2021).days)) < (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("smaller")
    else:
        vac_dec_A=pd.DataFrame()
        for n in range(int((end_date_A_2021 - start_date_A_2021).days)):
            decA=df4.copy(deep=True)
            if n==0:
                indexNames=decA[(((decA['DAY_x'] != start_date_A_2021.day) | (decA['MOIS_x'] != start_date_A_2021.month)) | ((decA['DAY_y'] != start_date_A_2022.day) | (decA['MOIS_y'] != start_date_A_2022.month)))].index
                decA.drop(indexNames , inplace=True)
                decA.reset_index(inplace=True,drop=True)
                frames = [decA,vac_dec_A]
                vac_dec_A = pd.concat(frames)
                vac_dec_A.reset_index(inplace=True,drop=True) 
            else:
                indexNames=decA[(((decA['DAY_x'] != (start_date_A_2021 + timedelta(n)).day) | (decA['MOIS_x'] != (start_date_A_2021 + timedelta(n)).month)) | ((decA['DAY_y'] != (start_date_A_2022 + timedelta(n)).day) | (decA['MOIS_y'] != (start_date_A_2022 + timedelta(n)).month)))].index
                decA.drop(indexNames , inplace=True)
                decA.reset_index(inplace=True,drop=True)
                frames = [decA,vac_dec_A]
                vac_dec_A = pd.concat(frames)
                vac_dec_A.reset_index(inplace=True,drop=True)
        
    indexNames = df4[df4['ID'].isin(vac_dec_A['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(vac_dec_A['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    df4

    # Jours normaux
    start_date_A_2021 = date(2021, 1, 4)
    end_date_A_2021 = date(2022, 1, 3)
    start_date_A_2022 = date(2022, 1, 3)
    end_date_A_2022 = date(2023, 1, 2)

    # zone A

    if (int ((end_date_A_2021 - start_date_A_2021).days)) > (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("bigger")
    elif (int ((end_date_A_2021 - start_date_A_2021).days)) < (int ((end_date_A_2022 - start_date_A_2022).days)):
        print("smaller")
    else:
        normaux=pd.DataFrame()
        for n in range(int((end_date_A_2021 - start_date_A_2021).days)):
            norm=df4.copy(deep=True)
            if n==0:
                indexNames=norm[(((norm['DAY_x'] != start_date_A_2021.day) | (norm['MOIS_x'] != start_date_A_2021.month)) | ((norm['DAY_y'] != start_date_A_2022.day) | (norm['MOIS_y'] != start_date_A_2022.month)))].index
                norm.drop(indexNames , inplace=True)
                norm.reset_index(inplace=True,drop=True)
                frames = [norm,normaux]
                normaux = pd.concat(frames)
                normaux.reset_index(inplace=True,drop=True) 
            else:
                indexNames=norm[(((norm['DAY_x'] != (start_date_A_2021 + timedelta(n)).day) | (norm['MOIS_x'] != (start_date_A_2021 + timedelta(n)).month)) | ((norm['DAY_y'] != (start_date_A_2022 + timedelta(n)).day) | (norm['MOIS_y'] != (start_date_A_2022 + timedelta(n)).month)))].index
                norm.drop(indexNames , inplace=True)
                norm.reset_index(inplace=True,drop=True)
                frames = [norm,normaux]
                normaux = pd.concat(frames)
                normaux.reset_index(inplace=True,drop=True)
        
    indexNames = df4[df4['ID'].isin(normaux['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID REF'].isin(normaux['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    
    frames = [fusion1,shipswitch,ascension,pentecote,paques,vac_dec_A,vac_dec_B,vac_dec_C,vac_hiver_A,vac_hiver_B,vac_hiver_C,vac_ete,vac_oct_A,vac_oct_B,vac_oct_C,vac_printemps_A,vac_printemps_B,vac_printemps_C,normaux]
    result = pd.concat(frames)
    result.reset_index(inplace=True,drop=True)

    final= result.copy(deep=True)
    # sorting by first name
    final.sort_values("DATE REF", inplace=True)
    # dropping duplicate values
    final.drop_duplicates(keep='first',inplace=True)
    final.reset_index(inplace=True,drop=True)

    
    final['HOUR'] = final['DATE'].dt.hour
    final['HOURW'] = final['DATE REF'].dt.hour
    final["ECART"]=final['HOUR']-final['HOURW']

    # print(final)
    data = pd.DataFrame(columns=[
            'ARMATEUR', 'NAVIRE','VENTES', 'VENTESW','HOUR','HOURW' 'DATEHEUREDEPART', 'NAVIREW', 'DATEHEUREDEPARTW', 'MAXDATEFICHIER', 'INFO',
            'RESEAU', 'PORTDEP', 'PORTARR', 'PORTDEPW', 'PORTARRW', 'MODELE', 'NUMPACKAGE', 'NUMPACKAGEW', 'MINDATEFICHIER'
        ])
    data['ARMATEUR']=final['ARM_x']
    data['NAVIRE']=final['NAV']
    data["VENTES"]=final['VTES_x']
    data["VENTESW"]=final['VTES_y']
    data["HOUR"]=final['HOUR']
    data["HOURW"]=final['HOURW']
    data["ECART"]=final['ECART']
    data['DATEHEUREDEPART']=final['DATE']
    data['NAVIREW']=final['NAV REF']
    data['DATEHEUREDEPARTW']=final['DATE REF']
    data['RESEAU']='CSC'
    data['PORTDEP']=final['DEP_x']
    data['PORTARR']=final['ARR_x']
    data['PORTDEPW']=final['DEP_y']
    data['PORTARRW']=final['ARR_y']
    data['NUMPACKAGE']=final['PackageId_x']
    data['NUMPACKAGEW']=final['PackageId_y']

    data['DATEHEUREDEPART'].astype(str).tolist()
    data['DATEHEUREDEPARTW'].astype(str).tolist()

    ids = data["NUMPACKAGEW"]
    df_test_lc = data[ids.isin(ids[ids.duplicated()])]
    df_test_lc.sort_values(by=['NUMPACKAGEW','NUMPACKAGE'],
                           inplace=True)
    df_test_lc.reset_index(drop=True, inplace=True)
    print(len(df_test_lc))
    groups = df_test_lc.groupby(['NUMPACKAGEW'])

    print(len(groups["NAVIRE"]))

    data_ventes = pd.DataFrame(columns=[
        'ARMATEUR', 'NAVIRE','VENTES', 'VENTESW', 'DATEHEUREDEPART', 'NAVIREW', 'DATEHEUREDEPARTW', 'MAXDATEFICHIER', 'INFO',
            'RESEAU', 'PORTDEP', 'PORTARR', 'PORTDEPW', 'PORTARRW', 'MODELE', 'NUMPACKAGE', 'NUMPACKAGEW', 'MINDATEFICHIER'
    ])
    for name, group in groups:
        group = groups.get_group(name)
        group.reset_index(inplace=True)
        for i in range(len(group["NAVIRE"])):
            if i==0:
                if((int(group['ECART'][i])>3)):
                        data_ventes = data_ventes.append(
                        {
                            'ARMATEUR':
                            group["ARMATEUR"][i],
                            'NAVIRE':
                            group["NAVIRE"][i],
                            'VENTES':
                            group["VENTES"][i],
                            'VENTESW':
                            group["VENTESW"][i],
                            'DATEHEUREDEPART':
                            group["DATEHEUREDEPART"][i],
                            'NAVIREW':
                            group["NAVIREW"][i],
                            'DATEHEUREDEPARTW':
                            group["DATEHEUREDEPARTW"][i],
                            'MAXDATEFICHIER':
                            group["MAXDATEFICHIER"][i],
                            'INFO':
                            group["INFO"][i],
                            'RESEAU':
                            group["RESEAU"][i],
                            'PORTDEP':
                            group["PORTDEP"][i],
                            'PORTARR':
                            group["PORTARR"][i],
                            'PORTDEPW':
                            group["PORTDEPW"][i],
                            'PORTARRW':
                            group["PORTARRW"][i],
                            'MODELE':
                            group["MODELE"][i],
                            'NUMPACKAGE':
                            group["NUMPACKAGE"][i],
                            'NUMPACKAGEW':
                            group["NUMPACKAGEW"][i],
                            'MINDATEFICHIER':
                            group["MINDATEFICHIER"][i]
                        },
                        ignore_index=True)
                elif((int(group['ECART'][i])<-3)):
                        data_ventes = data_ventes.append(
                        {
                            'ARMATEUR':
                            group["ARMATEUR"][i],
                            'NAVIRE':
                            group["NAVIRE"][i],
                            'VENTES':
                            group["VENTES"][i],
                            'VENTESW':
                            group["VENTESW"][i],
                            'DATEHEUREDEPART':
                            group["DATEHEUREDEPART"][i],
                            'NAVIREW':
                            group["NAVIREW"][i],
                            'DATEHEUREDEPARTW':
                            group["DATEHEUREDEPARTW"][i],
                            'MAXDATEFICHIER':
                            group["MAXDATEFICHIER"][i],
                            'INFO':
                            group["INFO"][i],
                            'RESEAU':
                            group["RESEAU"][i],
                            'PORTDEP':
                            group["PORTDEP"][i],
                            'PORTARR':
                            group["PORTARR"][i],
                            'PORTDEPW':
                            group["PORTDEPW"][i],
                            'PORTARRW':
                            group["PORTARRW"][i],
                            'MODELE':
                            group["MODELE"][i],
                            'NUMPACKAGE':
                            group["NUMPACKAGE"][i],
                            'NUMPACKAGEW':
                            group["NUMPACKAGEW"][i],
                            'MINDATEFICHIER':
                            group["MINDATEFICHIER"][i]
                        },
                        ignore_index=True)
            else:
                if((int(group['ECART'][i])>3)):
                        data_ventes = data_ventes.append(
                        {
                            'ARMATEUR':
                            group["ARMATEUR"][i],
                            'NAVIRE':
                            group["NAVIRE"][i],
                            'VENTES':
                            group["VENTES"][i],
                            'VENTESW':
                            group["VENTESW"][i],
                            'DATEHEUREDEPART':
                            group["DATEHEUREDEPART"][i],
                            'NAVIREW':
                            group["NAVIREW"][i],
                            'DATEHEUREDEPARTW':
                            group["DATEHEUREDEPARTW"][i],
                            'MAXDATEFICHIER':
                            group["MAXDATEFICHIER"][i],
                            'INFO':
                            group["INFO"][i],
                            'RESEAU':
                            group["RESEAU"][i],
                            'PORTDEP':
                            group["PORTDEP"][i],
                            'PORTARR':
                            group["PORTARR"][i],
                            'PORTDEPW':
                            group["PORTDEPW"][i],
                            'PORTARRW':
                            group["PORTARRW"][i],
                            'MODELE':
                            group["MODELE"][i],
                            'NUMPACKAGE':
                            group["NUMPACKAGE"][i],
                            'NUMPACKAGEW':
                            group["NUMPACKAGEW"][i],
                            'MINDATEFICHIER':
                            group["MINDATEFICHIER"][i]
                        },
                        ignore_index=True)
                elif((int(group['ECART'][i])<-3)):
                        data_ventes = data_ventes.append(
                        {
                            'ARMATEUR':
                            group["ARMATEUR"][i],
                            'NAVIRE':
                            group["NAVIRE"][i],
                            'VENTES':
                            group["VENTES"][i],
                            'VENTESW':
                            group["VENTESW"][i],
                            'DATEHEUREDEPART':
                            group["DATEHEUREDEPART"][i],
                            'NAVIREW':
                            group["NAVIREW"][i],
                            'DATEHEUREDEPARTW':
                            group["DATEHEUREDEPARTW"][i],
                            'MAXDATEFICHIER':
                            group["MAXDATEFICHIER"][i],
                            'INFO':
                            group["INFO"][i],
                            'RESEAU':
                            group["RESEAU"][i],
                            'PORTDEP':
                            group["PORTDEP"][i],
                            'PORTARR':
                            group["PORTARR"][i],
                            'PORTDEPW':
                            group["PORTDEPW"][i],
                            'PORTARRW':
                            group["PORTARRW"][i],
                            'MODELE':
                            group["MODELE"][i],
                            'NUMPACKAGE':
                            group["NUMPACKAGE"][i],
                            'NUMPACKAGEW':
                            group["NUMPACKAGEW"][i],
                            'MINDATEFICHIER':
                            group["MINDATEFICHIER"][i]
                        },
                        ignore_index=True)
    
    #pprint("test1",data_ventes)
    data2=data[~(data.NUMPACKAGE.isin(data_ventes.NUMPACKAGE) & data.NUMPACKAGEW.isin(data_ventes.NUMPACKAGEW))]

    ids = data2["NUMPACKAGEW"]
    df_test_lc = data2[ids.isin(ids[ids.duplicated()])]
    df_test_lc.sort_values(by=['NUMPACKAGEW','NUMPACKAGE'],
                           inplace=True)
    df_test_lc.reset_index(drop=True, inplace=True)
    #pprint(len(df_test_lc))
    groups = df_test_lc.groupby(['NUMPACKAGEW'])

    data_ventes = pd.DataFrame(columns=[
        'ARMATEUR', 'NAVIRE','VENTES', 'VENTESW', 'DATEHEUREDEPART', 'NAVIREW', 'DATEHEUREDEPARTW', 'MAXDATEFICHIER', 'INFO',
            'RESEAU', 'PORTDEP', 'PORTARR', 'PORTDEPW', 'PORTARRW', 'MODELE', 'NUMPACKAGE', 'NUMPACKAGEW', 'MINDATEFICHIER'
    ])
    for name, group in groups:
        group = groups.get_group(name)
        group.reset_index(inplace=True)
        for i in range(len(group["NAVIRE"])):
            if i==0:
                if(group['NAVIRE'][i]==group['NAVIREW'][i]):
                    if(group['NAVIRE'][i+1]!=group['NAVIREW'][i+1]):
                        data_ventes = data_ventes.append(
                        {
                            'ARMATEUR':
                            group["ARMATEUR"][i+1],
                            'NAVIRE':
                            group["NAVIRE"][i+1],
                            'VENTES':
                            group["VENTES"][i+1],
                            'VENTESW':
                            group["VENTESW"][i+1],
                            'DATEHEUREDEPART':
                            group["DATEHEUREDEPART"][i+1],
                            'NAVIREW':
                            group["NAVIREW"][i+1],
                            'DATEHEUREDEPARTW':
                            group["DATEHEUREDEPARTW"][i+1],
                            'MAXDATEFICHIER':
                            group["MAXDATEFICHIER"][i+1],
                            'INFO':
                            group["INFO"][i+1],
                            'RESEAU':
                            group["RESEAU"][i+1],
                            'PORTDEP':
                            group["PORTDEP"][i+1],
                            'PORTARR':
                            group["PORTARR"][i+1],
                            'PORTDEPW':
                            group["PORTDEPW"][i+1],
                            'PORTARRW':
                            group["PORTARRW"][i+1],
                            'MODELE':
                            group["MODELE"][i+1],
                            'NUMPACKAGE':
                            group["NUMPACKAGE"][i+1],
                            'NUMPACKAGEW':
                            group["NUMPACKAGEW"][i+1],
                            'MINDATEFICHIER':
                            group["MINDATEFICHIER"][i+1]
                        },
                        ignore_index=True)
                elif(group['NAVIRE'][i]!=group['NAVIREW'][i]):
                    if(group['NAVIRE'][i+1]==group['NAVIREW'][i+1]):
                        data_ventes = data_ventes.append(
                        {
                            'ARMATEUR':
                            group["ARMATEUR"][i],
                            'NAVIRE':
                            group["NAVIRE"][i],
                            'VENTES':
                            group["VENTES"][i],
                            'VENTESW':
                            group["VENTESW"][i],
                            'DATEHEUREDEPART':
                            group["DATEHEUREDEPART"][i],
                            'NAVIREW':
                            group["NAVIREW"][i],
                            'DATEHEUREDEPARTW':
                            group["DATEHEUREDEPARTW"][i],
                            'MAXDATEFICHIER':
                            group["MAXDATEFICHIER"][i],
                            'INFO':
                            group["INFO"][i],
                            'RESEAU':
                            group["RESEAU"][i],
                            'PORTDEP':
                            group["PORTDEP"][i],
                            'PORTARR':
                            group["PORTARR"][i],
                            'PORTDEPW':
                            group["PORTDEPW"][i],
                            'PORTARRW':
                            group["PORTARRW"][i],
                            'MODELE':
                            group["MODELE"][i],
                            'NUMPACKAGE':
                            group["NUMPACKAGE"][i],
                            'NUMPACKAGEW':
                            group["NUMPACKAGEW"][i],
                            'MINDATEFICHIER':
                            group["MINDATEFICHIER"][i]
                        },
                        ignore_index=True)

    #pprint("test1",data_ventes)
    data3=data2[~(data2.NUMPACKAGE.isin(data_ventes.NUMPACKAGE) & data2.NUMPACKAGEW.isin(data_ventes.NUMPACKAGEW))]

    ids = data3["NUMPACKAGEW"]
    df_test_lc = data3[ids.isin(ids[ids.duplicated()])]
    df_test_lc.sort_values(by=['NUMPACKAGEW','NUMPACKAGE'],
                           inplace=True)
    df_test_lc.reset_index(drop=True, inplace=True)
    #pprint(len(df_test_lc))
    groups = df_test_lc.groupby(['NUMPACKAGEW'])

    data_ventes = pd.DataFrame(columns=[
        'ARMATEUR', 'NAVIRE','VENTES', 'VENTESW', 'DATEHEUREDEPART', 'NAVIREW', 'DATEHEUREDEPARTW', 'MAXDATEFICHIER', 'INFO',
            'RESEAU', 'PORTDEP', 'PORTARR', 'PORTDEPW', 'PORTARRW', 'MODELE', 'NUMPACKAGE', 'NUMPACKAGEW', 'MINDATEFICHIER'
    ])
    #pprint(len(groups["NAVIRE"]))
    for name, group in groups:
        group = groups.get_group(name)
        group.reset_index(inplace=True)
        for i in range(len(group["NAVIRE"])):
            if i==0:
                if(group['VENTES'][i]>group['VENTES'][i+1]):
                    data_ventes = data_ventes.append(
                        {
                            'ARMATEUR':
                            group["ARMATEUR"][i+1],
                            'NAVIRE':
                            group["NAVIRE"][i+1],
                            'VENTES':
                            group["VENTES"][i+1],
                            'VENTESW':
                            group["VENTESW"][i+1],
                            'DATEHEUREDEPART':
                            group["DATEHEUREDEPART"][i+1],
                            'NAVIREW':
                            group["NAVIREW"][i+1],
                            'DATEHEUREDEPARTW':
                            group["DATEHEUREDEPARTW"][i+1],
                            'MAXDATEFICHIER':
                            group["MAXDATEFICHIER"][i+1],
                            'INFO':
                            group["INFO"][i+1],
                            'RESEAU':
                            group["RESEAU"][i+1],
                            'PORTDEP':
                            group["PORTDEP"][i+1],
                            'PORTARR':
                            group["PORTARR"][i+1],
                            'PORTDEPW':
                            group["PORTDEPW"][i+1],
                            'PORTARRW':
                            group["PORTARRW"][i+1],
                            'MODELE':
                            group["MODELE"][i+1],
                            'NUMPACKAGE':
                            group["NUMPACKAGE"][i+1],
                            'NUMPACKAGEW':
                            group["NUMPACKAGEW"][i+1],
                            'MINDATEFICHIER':
                            group["MINDATEFICHIER"][i+1]
                        },
                        ignore_index=True)
                else:
                    data_ventes = data_ventes.append(
                        {
                            'ARMATEUR':
                            group["ARMATEUR"][i],
                            'NAVIRE':
                            group["NAVIRE"][i],
                            'VENTES':
                            group["VENTES"][i],
                            'VENTESW':
                            group["VENTESW"][i],
                            'DATEHEUREDEPART':
                            group["DATEHEUREDEPART"][i],
                            'NAVIREW':
                            group["NAVIREW"][i],
                            'DATEHEUREDEPARTW':
                            group["DATEHEUREDEPARTW"][i],
                            'MAXDATEFICHIER':
                            group["MAXDATEFICHIER"][i],
                            'INFO':
                            group["INFO"][i],
                            'RESEAU':
                            group["RESEAU"][i],
                            'PORTDEP':
                            group["PORTDEP"][i],
                            'PORTARR':
                            group["PORTARR"][i],
                            'PORTDEPW':
                            group["PORTDEPW"][i],
                            'PORTARRW':
                            group["PORTARRW"][i],
                            'MODELE':
                            group["MODELE"][i],
                            'NUMPACKAGE':
                            group["NUMPACKAGE"][i],
                            'NUMPACKAGEW':
                            group["NUMPACKAGEW"][i],
                            'MINDATEFICHIER':
                            group["MINDATEFICHIER"][i]
                        },
                        ignore_index=True)
    #pprint("test2",data_ventes)
    data4=data3[~(data3.NUMPACKAGE.isin(data_ventes.NUMPACKAGE) & data3.NUMPACKAGEW.isin(data_ventes.NUMPACKAGEW))]
    
    data4.drop_duplicates(subset=['NUMPACKAGEW'], keep='last',inplace=True)
    #pprint(len(data4))
    '''
    pascommun = df[~df.CLIENT.isin(common.CLIENT)]
    print("yes", pascommun)
    frames = [pascommun, toadd]
    result = pd.concat(frames)
    result.reset_index(inplace=True, drop=True)'''
    return data4


def concoCSC(df1,df2, annee1, annee2):
    
    df1=df1[['ARM','JOUR','NAV','DATE','HEURE','DEP','ARR','ID','PackageId','VTES']]
    df2=df2[['ARM','JOUR','NAV','DATE','HEURE','DEP','ARR','ID','PackageId','VTES']]

    df1["MOIS"]=pd.DatetimeIndex(df1['DATE']).month
    df1['DAY'] = pd.DatetimeIndex(df1['DATE']).day
    df1['YEAR'] = pd.DatetimeIndex(df1['DATE']).year

    df_new = df2.rename(columns={'ID': 'ID REF','NAV':'NAV REF','DATE':'DATE REF'})
    df_new["MOIS"]=pd.DatetimeIndex(df_new['DATE REF']).month
    df_new['DAY'] = pd.DatetimeIndex(df_new['DATE REF']).day
    df_new['YEAR'] = pd.DatetimeIndex(df_new['DATE REF']).year

    data=conco(df1,df_new, annee1, annee2)

    return data

def ConcoCSC(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        annee1 = request.POST["annee1"]
        annee2 = request.POST["annee2"]
        xls = pd.ExcelFile(File1)
        df1 = pd.read_excel(xls, 'CSC 2021')
        df2 = pd.read_excel(xls, 'CSC 2022')
        data=concoCSC(df1,df2,annee1,annee2)
    total = time.time() - start_time
    print(total)
    return HttpResponse(data.to_json(orient='records'))