# -*- coding: utf-8 -*-
# Coded by HoxoMaxwell
# Apr.10.2019

import gc
import os
import warnings
import psutil
import json
import pickle
import collections as cl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tqdm import tqdm

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.options.mode.chained_assignment = None
# dir(pd.options.display)
warnings.simplefilter(action='ignore', category=FutureWarning)

plt.style.use('ggplot')

comp = pd.read_csv('./teams/Competitions.csv',
                   parse_dates=['EnabledDate', 'DeadlineDate'])
teams = pd.read_csv('./teams/Teams.csv.zip')

teams_gp = teams.groupby('CompetitionId').apply(
    lambda x: round(x.loc[:,
                    ["PublicLeaderboardRank",
                     "PrivateLeaderboardRank"]].corr('spearman').values[0, 1],
                    6)
).reset_index()
teams_gp.columns = ['Id', 'spearman_R']

comp_m = teams_gp.merge(comp, on='Id', how='left')
del comp, teams, teams_gp

comp_m.sort_values('DeadlineDate', ascending=False, inplace=True)
comp_m = comp_m[comp_m.CanQualifyTiers == True]
comp_m.to_csv('./shakeshake.csv', index=False)
