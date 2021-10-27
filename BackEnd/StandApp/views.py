import calendar
import numpy as np
import pandas as pd
from pathlib import Path
from django.http import HttpResponse

def Stat_CSC(data_yesterday,data_today,annee,mois,cible, budget):
    table_reseau_armateur_today=pd.pivot_table(data_today[(data_today.RESEAU == "CORSE") & (data_today.ARMATEUR == "CL")], index=['ANNEE','MOIS'],aggfunc={'PAX':np.sum})
    table_reseau_armateur_today.reset_index(inplace=True)
    table_reseau_armateur_yesterday=pd.pivot_table(data_yesterday[(data_yesterday.RESEAU == "CORSE") & (data_yesterday.ARMATEUR == "CL")], index=['ANNEE','MOIS'],aggfunc={'PAX':np.sum})
    table_reseau_armateur_yesterday.reset_index(inplace=True)
    df = pd.DataFrame()
    df["ANNEE"]=table_reseau_armateur_yesterday['ANNEE']
    df["MOIS"]=table_reseau_armateur_yesterday['MOIS']
    df["CUMUL-18"]=table_reseau_armateur_yesterday['PAX']
    df["CUMUL-19"]=table_reseau_armateur_today['PAX']
    df['Vente journalière'] = table_reseau_armateur_today['PAX'] - table_reseau_armateur_yesterday['PAX']
    df_mask=df[df.ANNEE.eq(annee-1) | df.ANNEE.eq(annee)]
    df_mask=df_mask[df_mask.ANNEE.eq(annee)]

    if len(mois)==1:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0])]
    if len(mois)==2:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1])]
    if len(mois)==3:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2])]
    if len(mois)==4:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2]) | df_mask.MOIS.eq(mois[3])]
    if len(mois)==5:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2]) | df_mask.MOIS.eq(mois[3]) | df_mask.MOIS.eq(mois[4])]
    if len(mois)==6:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2]) | df_mask.MOIS.eq(mois[3]) | df_mask.MOIS.eq(mois[4]) | df_mask.MOIS.eq(mois[5])]
    if len(mois)==7:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2]) | df_mask.MOIS.eq(mois[3]) | df_mask.MOIS.eq(mois[4]) | df_mask.MOIS.eq(mois[5]) | df_mask.MOIS.eq(mois[6])]
    if len(mois)==8:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2]) | df_mask.MOIS.eq(mois[3]) | df_mask.MOIS.eq(mois[4]) | df_mask.MOIS.eq(mois[5]) | df_mask.MOIS.eq(mois[6]) | df_mask.MOIS.eq(mois[7])]
    if len(mois)==9:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2]) | df_mask.MOIS.eq(mois[3]) | df_mask.MOIS.eq(mois[4]) | df_mask.MOIS.eq(mois[5]) | df_mask.MOIS.eq(mois[6]) | df_mask.MOIS.eq(mois[7]) | df_mask.MOIS.eq(mois[8])]
    if len(mois)==10:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2]) | df_mask.MOIS.eq(mois[3]) | df_mask.MOIS.eq(mois[4]) | df_mask.MOIS.eq(mois[5]) | df_mask.MOIS.eq(mois[6]) | df_mask.MOIS.eq(mois[7]) | df_mask.MOIS.eq(mois[8]) | df_mask.MOIS.eq(mois[9])]
    if len(mois)==11:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2]) | df_mask.MOIS.eq(mois[3]) | df_mask.MOIS.eq(mois[4]) | df_mask.MOIS.eq(mois[5]) | df_mask.MOIS.eq(mois[6]) | df_mask.MOIS.eq(mois[7]) | df_mask.MOIS.eq(mois[8]) | df_mask.MOIS.eq(mois[9]) | df_mask.MOIS.eq(mois[10])]
    if len(mois)==12:
        df_mask_cumul=df_mask[df_mask.MOIS.eq(mois[0]) | df_mask.MOIS.eq(mois[1]) | df_mask.MOIS.eq(mois[2]) | df_mask.MOIS.eq(mois[3]) | df_mask.MOIS.eq(mois[4]) | df_mask.MOIS.eq(mois[5]) | df_mask.MOIS.eq(mois[6]) | df_mask.MOIS.eq(mois[7]) | df_mask.MOIS.eq(mois[8]) | df_mask.MOIS.eq(mois[9]) | df_mask.MOIS.eq(mois[10]) | df_mask.MOIS.eq(mois[11])]
    
    df_mask_cumul['BUDGET']=budget
    mesure=pd.DataFrame()
    mesure["CORSE ", annee] = df_mask_cumul['MOIS'].apply(lambda x: calendar.month_abbr[x])
    mesure["CIBLE/JR"] = cible
    mesure["VENTE JOUR"] = df_mask_cumul['Vente journalière']
    mesure["CUMUL"] = df_mask_cumul['CUMUL-19']
    mesure["BUDGET"] = (df_mask_cumul['CUMUL-19']/df_mask_cumul['BUDGET']).apply(lambda x: int(x*100))
    return mesure


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
        data = Stat_CSC(df1,df2,annee,mois,cible,budget)
        print('data : ', data)
    return HttpResponse(data.to_json(orient='records'))
