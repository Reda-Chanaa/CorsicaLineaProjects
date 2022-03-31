import time
from django.http import HttpResponse
from datetime import datetime
from datetime import timedelta, date
import pandas as pd
import numpy as np
import datetime

def conco(df1,df_new):

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
    indexNames = pentecote[ (((pentecote['DAY_x'] != 21) | (pentecote['MOIS_x'] != 5)) | ((pentecote['DAY_y'] != 3) | (pentecote['MOIS_y'] != 6))) 
    & (((pentecote['DAY_x'] != 22) | (pentecote['MOIS_x'] != 5)) | ((pentecote['DAY_y'] != 4) | (pentecote['MOIS_y'] != 6)))
    & (((pentecote['DAY_x'] != 23) | (pentecote['MOIS_x'] != 5)) | ((pentecote['DAY_y'] != 5) | (pentecote['MOIS_y'] != 6))) 
    & (((pentecote['DAY_x'] != 24) | (pentecote['MOIS_x'] != 5)) | ((pentecote['DAY_y'] != 6) | (pentecote['MOIS_y'] != 6))) ].index
    pentecote.drop(indexNames , inplace=True)
    pentecote.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(pentecote['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    indexNames = df4[df4['ID REF'].isin(pentecote['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    paques=df4.copy(deep=True)
    indexNames = paques[ (((paques['DAY_x'] != 2) | (paques['MOIS_x'] != 4)) | ((paques['DAY_y'] != 15) | (paques['MOIS_y'] != 4))) 
    & (((paques['DAY_x'] != 3) | (paques['MOIS_x'] != 4)) | ((paques['DAY_y'] != 16) | (paques['MOIS_y'] != 4)))
    & (((paques['DAY_x'] != 4) | (paques['MOIS_x'] != 4)) | ((paques['DAY_y'] != 17) | (paques['MOIS_y'] != 4))) 
    & (((paques['DAY_x'] != 5) | (paques['MOIS_x'] != 4)) | ((paques['DAY_y'] != 18) | (paques['MOIS_y'] != 4))) ].index
    paques.drop(indexNames , inplace=True)
    paques.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(paques['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    indexNames = df4[df4['ID REF'].isin(paques['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    ascension=df4.copy(deep=True)
    indexNames = ascension[ (((ascension['DAY_x'] != 12) | (ascension['MOIS_x'] != 5)) | ((ascension['DAY_y'] != 25) | (ascension['MOIS_y'] != 5))) 
    & (((ascension['DAY_x'] != 13) | (ascension['MOIS_x'] != 5)) | ((ascension['DAY_y'] != 26) | (ascension['MOIS_y'] != 5)))
    & (((ascension['DAY_x'] != 14) | (ascension['MOIS_x'] != 5)) | ((ascension['DAY_y'] != 27) | (ascension['MOIS_y'] != 5))) 
    & (((ascension['DAY_x'] != 15) | (ascension['MOIS_x'] != 5)) | ((ascension['DAY_y'] != 28) | (ascension['MOIS_y'] != 5)))
    & (((ascension['DAY_x'] != 16) | (ascension['MOIS_x'] != 5)) | ((ascension['DAY_y'] != 29) | (ascension['MOIS_y'] != 5))) ].index
    ascension.drop(indexNames , inplace=True)
    ascension.reset_index(inplace=True,drop=True)

    indexNames = df4[df4['ID'].isin(ascension['ID'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)
    indexNames = df4[df4['ID REF'].isin(ascension['ID REF'])].index
    df4.drop(indexNames , inplace=True)
    df4.reset_index(inplace=True,drop=True)

    ete=df4.copy(deep=True)
    start_date_2021 = date(2021, 7, 8)
    end_date_2021 = date(2021, 9, 1)
    start_date_2022 = date(2022, 7, 7)
    end_date_2022 = date(2022, 8, 31)
    
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

    start_date_A_2021 = date(2021, 4, 9)
    end_date_A_2021 = date(2021, 4, 25)
    start_date_A_2022 = date(2022, 4, 15)
    end_date_A_2022 = date(2022, 5, 1)

    start_date_B_2021 = date(2021, 4,23)
    end_date_B_2021 = date(2021, 5, 9)
    start_date_B_2022 = date(2022, 4, 8)
    end_date_B_2022 = date(2022, 4, 24)

    start_date_C_2021 = date(2021, 4, 16)
    end_date_C_2021 = date(2021, 5, 2)
    start_date_C_2022 = date(2022, 4, 22)
    end_date_C_2022 = date(2022, 5, 8)

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
    
    start_date_A_2021 = date(2021, 2, 5)
    end_date_A_2021 = date(2021, 2, 21)
    start_date_A_2022 = date(2022, 2, 11)
    end_date_A_2022 = date(2022, 2, 27)

    start_date_B_2021 = date(2021, 2,19)
    end_date_B_2021 = date(2021, 3, 7)
    start_date_B_2022 = date(2022, 2, 4)
    end_date_B_2022 = date(2022, 2, 20)

    start_date_C_2021 = date(2021, 2, 12)
    end_date_C_2021 = date(2021, 2, 28)
    start_date_C_2022 = date(2022, 2, 18)
    end_date_C_2022 = date(2022, 3,6)

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

    # Octobre
    start_date_A_2021 = date(2021, 10, 22)
    end_date_A_2021 = date(2021, 11, 7)
    start_date_A_2022 = date(2022, 10, 21)
    end_date_A_2022 = date(2022, 11, 6)

    start_date_B_2021 = date(2021, 10, 22)
    end_date_B_2021 = date(2021, 11, 7)
    start_date_B_2022 = date(2022, 10, 21)
    end_date_B_2022 = date(2022, 11, 6)

    start_date_C_2021 = date(2021, 10, 22)
    end_date_C_2021 = date(2021, 11, 7)
    start_date_C_2022 = date(2022, 10, 21)
    end_date_C_2022 = date(2022, 11, 6)

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
    end_date_C_2022 = date(2023, 1, 1)

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

    data = pd.DataFrame(columns=[
            'ARMATEUR', 'NAVIRE', 'DATEHEUREDEPART', 'NAVIREW', 'DATEHEUREDEPARTW', 'MAXDATEFICHIER', 'INFO',
            'RESEAU', 'PORTDEP', 'PORTARR', 'PORTDEPW', 'PORTARRW', 'MODELE', 'NUMPACKAGE', 'NUMPACKAGEW', 'MINDATEFICHIER'
        ])
    data['ARMATEUR']=final['ARM_x']
    data['NAVIRE']=final['NAV']
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
    print(data)

    return data


def concoCSC(df1,df2):
    
    df1=df1[['ARM','JOUR','NAV','DATE','HEURE','DEP','ARR','ID','PackageId']]
    df2=df2[['ARM','JOUR','NAV','DATE','HEURE','DEP','ARR','ID','PackageId']]

    df1["MOIS"]=pd.DatetimeIndex(df1['DATE']).month
    df1['DAY'] = pd.DatetimeIndex(df1['DATE']).day
    df1['YEAR'] = pd.DatetimeIndex(df1['DATE']).year

    df_new = df2.rename(columns={'ID': 'ID REF','NAV':'NAV REF','DATE':'DATE REF'})
    df_new["MOIS"]=pd.DatetimeIndex(df_new['DATE REF']).month
    df_new['DAY'] = pd.DatetimeIndex(df_new['DATE REF']).day
    df_new['YEAR'] = pd.DatetimeIndex(df_new['DATE REF']).year

    data=conco(df1,df_new)

    return data

def ConcoCSC(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        xls = pd.ExcelFile(File1)
        df1 = pd.read_excel(xls, 'CSC 2021')
        df2 = pd.read_excel(xls, 'CSC 2022')
        data=concoCSC(df1,df2)
    total = time.time() - start_time
    print(total)
    return HttpResponse(data.to_json(orient='records'))