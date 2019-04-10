# -*- coding: utf-8 -*-
# Coded by HoxoMaxwell
# Mar.23.2019

import os
from kaggle.api.kaggle_api_extended import KaggleApi

os.makedirs('./users', exist_ok=True)
os.makedirs('./teams', exist_ok=True)

api = KaggleApi()
api.authenticate()
api.dataset_download_cli(
    dataset='kaggle/meta-kaggle',
    file_name='UserAchievements.csv',
    path='./users'
)

# api.dataset_download_cli(
#     dataset='kaggle/meta-kaggle',
#     file_name='UserOrganizations.csv',
#     path='./users'
# )
#
# api.dataset_download_cli(
#     dataset='kaggle/meta-kaggle',
#     file_name='Users.csv',
#     path='./users'
# )

api.dataset_download_cli(
    dataset='kaggle/meta-kaggle',
    file_name='Teams.csv',
    path='./teams'
)

api.dataset_download_cli(
    dataset='kaggle/meta-kaggle',
    file_name='Competitions.csv',
    path='./teams'
)
