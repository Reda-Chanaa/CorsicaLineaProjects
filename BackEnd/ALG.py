import calendar
import numpy as np
import pandas as pd
from pathlib import Path
from django.http import HttpResponse

def Stat_ALG(data_yesterday,data_today,annee,mois):
    table_reseau_armateur_today=pd.pivot_table(data_today[(data_today.RESEAU == "ALGERIE") & (data_today.ARMATEUR == "CL")], index=['ANNEE','MOIS'],aggfunc={'PAX':np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_yesterday=pd.pivot_table(data_yesterday[(data_yesterday.RESEAU == "ALGERIE") & (data_yesterday.ARMATEUR == "CL")], index=['ANNEE','MOIS'],aggfunc={'PAX':np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    df = pd.DataFrame()
    df["ANNEE"]=table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"]=table_reseau_armateur_yesterday['MOIS']
    df["CUMUL"]=table_reseau_armateur_yesterday['PAX']
    df['VENTE'] = table_reseau_armateur_today['PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask=df[df.ANNEE.eq(annee-1) | df.ANNEE.eq(annee)]
    df_mask_2020=pd.DataFrame()
    df_mask_2020=df_mask[df_mask.ANNEE.eq(annee-1)]

    if len(mois)==1:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0])]
    if len(mois)==2:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1])]
    if len(mois)==3:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2])]
    if len(mois)==4:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2]) | df_mask_2020.MOIS.eq(mois[3])]
    if len(mois)==5:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2]) | df_mask_2020.MOIS.eq(mois[3]) | df_mask_2020.MOIS.eq(mois[4])]
    if len(mois)==6:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2]) | df_mask_2020.MOIS.eq(mois[3]) | df_mask_2020.MOIS.eq(mois[4]) | df_mask_2020.MOIS.eq(mois[5])]
    if len(mois)==7:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2]) | df_mask_2020.MOIS.eq(mois[3]) | df_mask_2020.MOIS.eq(mois[4]) | df_mask_2020.MOIS.eq(mois[5]) | df_mask_2020.MOIS.eq(mois[6])]
    if len(mois)==8:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2]) | df_mask_2020.MOIS.eq(mois[3]) | df_mask_2020.MOIS.eq(mois[4]) | df_mask_2020.MOIS.eq(mois[5]) | df_mask_2020.MOIS.eq(mois[6]) | df_mask_2020.MOIS.eq(mois[7])]
    if len(mois)==9:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2]) | df_mask_2020.MOIS.eq(mois[3]) | df_mask_2020.MOIS.eq(mois[4]) | df_mask_2020.MOIS.eq(mois[5]) | df_mask_2020.MOIS.eq(mois[6]) | df_mask_2020.MOIS.eq(mois[7]) | df_mask_2020.MOIS.eq(mois[8])]
    if len(mois)==10:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2]) | df_mask_2020.MOIS.eq(mois[3]) | df_mask_2020.MOIS.eq(mois[4]) | df_mask_2020.MOIS.eq(mois[5]) | df_mask_2020.MOIS.eq(mois[6]) | df_mask_2020.MOIS.eq(mois[7]) | df_mask_2020.MOIS.eq(mois[8]) | df_mask_2020.MOIS.eq(mois[9])]
    if len(mois)==11:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2]) | df_mask_2020.MOIS.eq(mois[3]) | df_mask_2020.MOIS.eq(mois[4]) | df_mask_2020.MOIS.eq(mois[5]) | df_mask_2020.MOIS.eq(mois[6]) | df_mask_2020.MOIS.eq(mois[7]) | df_mask_2020.MOIS.eq(mois[8]) | df_mask_2020.MOIS.eq(mois[9]) | df_mask_2020.MOIS.eq(mois[10])]
    if len(mois)==12:
        df_mask_cumul_2020=df_mask_2020[df_mask_2020.MOIS.eq(mois[0]) | df_mask_2020.MOIS.eq(mois[1]) | df_mask_2020.MOIS.eq(mois[2]) | df_mask_2020.MOIS.eq(mois[3]) | df_mask_2020.MOIS.eq(mois[4]) | df_mask_2020.MOIS.eq(mois[5]) | df_mask_2020.MOIS.eq(mois[6]) | df_mask_2020.MOIS.eq(mois[7]) | df_mask_2020.MOIS.eq(mois[8]) | df_mask_2020.MOIS.eq(mois[9]) | df_mask_2020.MOIS.eq(mois[10]) | df_mask_2020.MOIS.eq(mois[11])]
    
    del df_mask_cumul_2020["ANNEE"]
    df_mask_cumul_2020.columns = ['MOIS', 'CUMUL N-1', 'VENTE N-1']
    df_mask_cumul_2020.reset_index(drop=True, inplace=True)

    df_mask_2021=pd.DataFrame()
    df_mask_2021=df_mask[df_mask.ANNEE.eq(annee)]
    
    if len(mois)==1:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0])]
    if len(mois)==2:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1])]
    if len(mois)==3:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2])]
    if len(mois)==4:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2]) | df_mask_2021.MOIS.eq(mois[3])]
    if len(mois)==5:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2]) | df_mask_2021.MOIS.eq(mois[3]) | df_mask_2021.MOIS.eq(mois[4])]
    if len(mois)==6:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2]) | df_mask_2021.MOIS.eq(mois[3]) | df_mask_2021.MOIS.eq(mois[4]) | df_mask_2021.MOIS.eq(mois[5])]
    if len(mois)==7:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2]) | df_mask_2021.MOIS.eq(mois[3]) | df_mask_2021.MOIS.eq(mois[4]) | df_mask_2021.MOIS.eq(mois[5]) | df_mask_2021.MOIS.eq(mois[6])]
    if len(mois)==8:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2]) | df_mask_2021.MOIS.eq(mois[3]) | df_mask_2021.MOIS.eq(mois[4]) | df_mask_2021.MOIS.eq(mois[5]) | df_mask_2021.MOIS.eq(mois[6]) | df_mask_2021.MOIS.eq(mois[7])]
    if len(mois)==9:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2]) | df_mask_2021.MOIS.eq(mois[3]) | df_mask_2021.MOIS.eq(mois[4]) | df_mask_2021.MOIS.eq(mois[5]) | df_mask_2021.MOIS.eq(mois[6]) | df_mask_2021.MOIS.eq(mois[7]) | df_mask_2021.MOIS.eq(mois[8])]
    if len(mois)==10:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2]) | df_mask_2021.MOIS.eq(mois[3]) | df_mask_2021.MOIS.eq(mois[4]) | df_mask_2021.MOIS.eq(mois[5]) | df_mask_2021.MOIS.eq(mois[6]) | df_mask_2021.MOIS.eq(mois[7]) | df_mask_2021.MOIS.eq(mois[8]) | df_mask_2021.MOIS.eq(mois[9])]
    if len(mois)==11:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2]) | df_mask_2021.MOIS.eq(mois[3]) | df_mask_2021.MOIS.eq(mois[4]) | df_mask_2021.MOIS.eq(mois[5]) | df_mask_2021.MOIS.eq(mois[6]) | df_mask_2021.MOIS.eq(mois[7]) | df_mask_2021.MOIS.eq(mois[8]) | df_mask_2021.MOIS.eq(mois[9]) | df_mask_2021.MOIS.eq(mois[10])]
    if len(mois)==12:
        df_mask_cumul_2021=df_mask_2021[df_mask_2021.MOIS.eq(mois[0]) | df_mask_2021.MOIS.eq(mois[1]) | df_mask_2021.MOIS.eq(mois[2]) | df_mask_2021.MOIS.eq(mois[3]) | df_mask_2021.MOIS.eq(mois[4]) | df_mask_2021.MOIS.eq(mois[5]) | df_mask_2021.MOIS.eq(mois[6]) | df_mask_2021.MOIS.eq(mois[7]) | df_mask_2021.MOIS.eq(mois[8]) | df_mask_2021.MOIS.eq(mois[9]) | df_mask_2021.MOIS.eq(mois[10]) | df_mask_2021.MOIS.eq(mois[11])]
    
    del df_mask_cumul_2021["ANNEE"]
    df_mask_cumul_2021.columns = ['MOIS', 'CUMUL N', 'VENTE N']
    df_mask_cumul_2021.reset_index(drop=True, inplace=True)

    mesure=pd.DataFrame()
    mesure["ALGERIE"] = df_mask_cumul_2020['MOIS'].apply(lambda x: calendar.month_abbr[x])
    mesure["VENTE N-1"] = df_mask_cumul_2020['VENTE N-1'].apply(lambda x: x)
    mesure["VENTE N"] = df_mask_cumul_2021['VENTE N'].apply(lambda x: x)
    mesure["CUMUL N-1"] = df_mask_cumul_2020['CUMUL N-1'].apply(lambda x: x)
    mesure["CUMUL N"] = df_mask_cumul_2021['CUMUL N'].apply(lambda x: x)
    mesure["ECART vs N-1"] = ((df_mask_cumul_2021['CUMUL N']-df_mask_cumul_2020['CUMUL N-1'])/df_mask_cumul_2020['CUMUL N-1']).apply(lambda x: int(x*100))

    mesure = mesure.reset_index(drop=True)
    BS1=pd.DataFrame(columns = ['ALGERIE' , 'VENTE N-1', 'VENTE N',"CUMUL N-1","CUMUL N","ECART vs N-1"])
    MS1=pd.DataFrame(columns = ['ALGERIE' , 'VENTE N-1', 'VENTE N',"CUMUL N-1","CUMUL N","ECART vs N-1"])
    HS=pd.DataFrame(columns = ['ALGERIE' , 'VENTE N-1', 'VENTE N',"CUMUL N-1","CUMUL N","ECART vs N-1"])
    MS2=pd.DataFrame(columns = ['ALGERIE' , 'VENTE N-1', 'VENTE N',"CUMUL N-1","CUMUL N","ECART vs N-1"])
    BS2=pd.DataFrame(columns = ['ALGERIE' , 'VENTE N-1', 'VENTE N',"CUMUL N-1","CUMUL N","ECART vs N-1"])
    for i in mesure.index:
    #  1 BS
        if mesure["ALGERIE"][i]=="Jan":
            BS1.loc[0]=["Janvier",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
        if mesure["ALGERIE"][i]=="Feb":
            BS1.loc[1]=["Février",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
        if mesure["ALGERIE"][i]=="Mar":
            BS1.loc[2]=["Mars",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
            if len(BS1) == 3:
                BS1.loc[3]=["BASSE SAISON 1", BS1["VENTE N-1"][0]+BS1["VENTE N-1"][1]+BS1["VENTE N-1"][2],BS1["VENTE N"][0]+BS1["VENTE N"][1]+BS1["VENTE N"][2],BS1["CUMUL N-1"][0]+BS1["CUMUL N-1"][1]+BS1["CUMUL N-1"][2],BS1["CUMUL N"][0]+BS1["CUMUL N"][1]+BS1["CUMUL N"][2],(BS1["ECART vs N-1"][0]+BS1["ECART vs N-1"][1]+BS1["ECART vs N-1"][2])]
            elif len(BS1) == 2:
                BS1.loc[3]=["BASSE SAISON 1", BS1["VENTE N-1"][1]+BS1["VENTE N-1"][2],BS1["VENTE N"][1]+BS1["VENTE N"][2],BS1["CUMUL N-1"][1]+BS1["CUMUL N-1"][2],BS1["CUMUL N"][1]+BS1["CUMUL N"][2],(BS1["ECART vs N-1"][1]+BS1["ECART vs N-1"][2])]
            else:
                BS1.loc[3]=["BASSE SAISON 1", BS1["VENTE N-1"][1],BS1["VENTE N"][1],BS1["CUMUL N"][1],BS1["ECART vs N-1"][1]]
        #  1 MS
        if mesure["ALGERIE"][i]=="Apr":
            MS1.loc[0]=["Avril",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
        if mesure["ALGERIE"][i]=="May":
            MS1.loc[1]=["Mai",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
        if mesure["ALGERIE"][i]=="Jun":
            MS1.loc[2]=["juin",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
            if len(MS1) == 3:
                MS1.loc[3]=["MOYENNE SAISON 1", MS1["VENTE N-1"][0]+MS1["VENTE N-1"][1]+MS1["VENTE N-1"][2],MS1["VENTE N"][0]+MS1["VENTE N"][1]+MS1["VENTE N"][2],MS1["CUMUL N-1"][0]+MS1["CUMUL N-1"][1]+MS1["CUMUL N-1"][2],MS1["CUMUL N"][0]+MS1["CUMUL N"][1]+MS1["CUMUL N"][2],(MS1["ECART vs N-1"][0]+MS1["ECART vs N-1"][1]+MS1["ECART vs N-1"][2])]
            elif len(MS1) == 2:
                MS1.loc[3]=["MOYENNE SAISON 1", MS1["VENTE N-1"][1]+MS1["VENTE N-1"][2],MS1["VENTE N"][1]+MS1["VENTE N"][2],MS1["CUMUL N-1"][1]+MS1["CUMUL N-1"][2],MS1["CUMUL N"][1]+MS1["CUMUL N"][2],(MS1["ECART vs N-1"][1]+MS1["ECART vs N-1"][2])]
            else:
                MS1.loc[3]=["MOYENNE SAISON 1", MS1["VENTE N-1"][1],MS1["VENTE N"][1],MS1["CUMUL N-1"][1],MS1["CUMUL N"][1],MS1["ECART vs N-1"][1]]
        #  HS
        if mesure["ALGERIE"][i]=="Jul":
            HS.loc[0]=["Juillet",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
        if mesure["ALGERIE"][i]=="Aug":
            HS.loc[1]=["Août",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
            if len(HS) == 2:
                HS.loc[2]=["HAUTE SAISON 2", HS["VENTE N-1"][0]+HS["VENTE N-1"][1],HS["VENTE N"][0]+HS["VENTE N"][1],HS["CUMUL N-1"][0]+HS["CUMUL N-1"][1],HS["CUMUL N"][0]+HS["CUMUL N"][1],(HS["ECART vs N-1"][0]+HS["ECART vs N-1"][1])]
            else:
                HS.loc[2]=["HAUTE SAISON 2", HS["VENTE N-1"][1],HS["VENTE N"][1],HS["CUMUL N"][1],HS["ECART vs N-1"][1]]
        #  2 MS
        if mesure["ALGERIE"][i]=="Sep":
            MS2.loc[0]=["Septembre",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
        if mesure["ALGERIE"][i]=="Oct":
            MS2.loc[1]=["Octobre",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
            if len(MS2) == 2:
                MS2.loc[2]=["MOYENNE SAISON 2", MS2["VENTE N-1"][0]+MS2["VENTE N-1"][1],MS2["VENTE N"][0]+MS2["VENTE N"][1],MS2["CUMUL N-1"][0]+MS2["CUMUL N-1"][1],MS2["CUMUL N"][0]+MS2["CUMUL N"][1],(MS2["ECART vs N-1"][0]+MS2["ECART vs N-1"][1])]
            else:
                MS2.loc[2]=["MOYENNE SAISON 2", MS2["VENTE N-1"][1],MS2["VENTE N"][1],MS2["CUMUL N-1"][1],MS2["CUMUL N"][1],MS2["ECART vs N-1"][1]]
        #  2 BS
        if mesure["ALGERIE"][i]=="Nov":
            BS2.loc[0]=["Novembre",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
        if mesure["ALGERIE"][i]=="Dec":
            BS2.loc[1]=["Décembre",mesure["VENTE N-1"][i],mesure["VENTE N"][i],mesure["CUMUL N-1"][i],mesure["CUMUL N"][i],mesure["ECART vs N-1"][i]]
            if len(BS2) == 2:
                BS2.loc[2]=["BASSE SAISON 2", BS2["VENTE N-1"][1]+BS2["VENTE N-1"][0],BS2["VENTE N"][0]+BS2["VENTE N"][1],BS2["CUMUL N-1"][0]+BS2["CUMUL N-1"][1],BS2["CUMUL N"][0]+BS2["CUMUL N"][1],int((((BS2["CUMUL N"][0]+BS2["CUMUL N"][1])-(BS2["CUMUL N-1"][0]+BS2["CUMUL N-1"][1]))/(BS2["CUMUL N-1"][0]+BS2["CUMUL N-1"][1]))*100)]
            else:
                BS2.loc[2]=["BASSE SAISON 2", BS2["VENTE N-1"][1],BS2["VENTE N"][1],BS2["CUMUL N-1"][1],BS2["CUMUL N"][1],BS2["ECART vs N-1"][1]]
    
    if len(BS1)!=0 and len(MS1)!=0 and len(HS)!=0 and len(MS2) !=0 and len(BS2)!=0:
        reporting = pd.concat([BS1,MS1,HS,MS2,BS2])
    elif len(MS1)!=0 and len(HS)!=0 and len(MS2) !=0 and len(BS2)!=0:
        reporting = pd.concat([MS1,HS,MS2,BS2])
    elif len(HS)!=0 and len(MS2)!=0 and len(BS2)!=0:
        reporting = pd.concat([HS,MS2,BS2])
    elif len(MS2)!=0 and len(BS2)!=0:
        reporting = pd.concat([MS2,BS2])
    else:
        reporting = BS2
    return reporting

# Files stats with Django


def StandFile(request):
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        File2 = request.FILES["file2"]
        annee= request.FILES["annee"]
        mois= request.FILES["mois"]
        cible= request.FILES["cible"]
        budget= request.FILES["budget"]
        df1 = pd.read_csv(File1)
        df2 = pd.read_csv(File2)
        # Stats
        data = Stat_ALG(df1,df2,annee,mois,cible,budget)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))
