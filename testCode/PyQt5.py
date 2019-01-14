import psycopg2
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re

import os
os.chdir(r'C:\Users\212712961\Desktop')

### Input ###
kw = 'RAB6-D'
mydate = '2018-04-12'
#############

print ('Collecting results using keyword %s' % kw)



# Step 1.1: Load StatisData
from wx_query import connect_acoustic
conn=connect_acoustic()
from wx_query import load_stat
df_stat = load_stat (conn, kw, mydate)


# Step 1.2: Format conversion and cleaning of the StatisData

from wx_analysis import stat_sig_conv, distinct_sn
from wx_vistools import feature_trend_lite

df_stat = stat_sig_conv(df_stat)
sn_stat_kw = distinct_sn(df_stat['sn'])

# Step 2: Load EDHR Data
from wx_query import connect_psg, load_edhrv3
conn=connect_psg()
df_edhr_full = load_edhrv3 (conn, kw, mydate)


# Step 3: Load edms for the defects

print ('loading scrap report' )
df_scrap = pd.read_csv('scrap_RAB6D_2018.csv', encoding='utf-8')

df_scrap = df_scrap.rename(columns={'S/N':'sn'})
from wx_analysis import description_mapping as dm
df_scrap['defect_category']=df_scrap['Defect'].map(dm)

sn_scrap = distinct_sn(df_scrap['sn'])
print('total edms distinct entries: %d' % len(sn_scrap))


# Step 4.0: Filtering edhr table by route_step and line_num of interest
### Input ###
route_step_name = '010'
line_number = '20'
#############

df_edhr = df_edhr_full[(df_edhr_full['route_step_name']==route_step_name) &
                      (df_edhr_full['line_number']==line_number)]
sn_edhr_kw = distinct_sn(df_edhr['object_name'])


# Step 4.1: Filtering statsdata and edhr by joining
from wx_analysis import sn_join
dict_sn_cmp = sn_join (sn_stat_kw, sn_edhr_kw, pflag=True)
sn_scope = dict_sn_cmp ['inner']

df_stat = df_stat[df_stat['sn'].isin(sn_scope)]
df_edhr = df_edhr[df_edhr['object_name'].isin(sn_scope)]
sn_stat_kw = sn_scope
sn_edhr_kw = sn_scope


# Step 4.2: Filtering the edms with sn_scope

df_scrap_kw =df_scrap[df_scrap['sn'].isin(sn_scope)]
sn_scrap_kw = distinct_sn(df_scrap_kw['sn'])
print ('after filtering with keyword %s, %d entries left' % (kw, len(sn_scrap_kw)))

dict_sn_cmp = sn_join (sn_scope, sn_scrap_kw, pflag=True)
sn_defect = dict_sn_cmp ['inner']
sn_good = dict_sn_cmp ['left_only']


# Step 5: Visualize good from bad
df_vis = pd.merge(df_edhr, df_stat, how='inner', left_on='object_name', right_on='sn')
df_vis = pd.merge(df_vis, df_scrap_kw, how='left', left_on='object_name', right_on='sn')
df_vis.defect_category = df_vis.defect_category.fillna('NA')

### Input ###
defect_of_interest = ['NA', 'lg']
#############

df_vis_sub = df_vis[df_vis['defect_category'].isin(defect_of_interest)]

### Input: ANOVA X, Y ###
anovaX = 'user_name'
fields = ['fl6_mean', 'fl6_std']
fields_to_choose_from = df_vis.columns
#############

for f in fields:
    plt.figure()
    sns.stripplot (x='user_name', y=f,
                   hue='defect_category', data=df_vis_sub, jitter=True,
                   alpha=0.5, dodge=True, ax=plt.gca())

from wx_vistools import feature_trend_stat
feature_trend_stat (df_vis_sub, xfactor=anovaX, fields=fields,
                        cfactor='defect_category', crange=['NA', 'lg'], ttl='')
