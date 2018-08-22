# -*- coding: utf-8 -*-

import pandas as pd

houses = pd.read_csv('../vhouse.csv')
houses_detail = pd.read_csv('../detail.csv')

houses = pd.merge(houses, houses_detail, how='inner', on=['title', 'link'])

houses.to_csv('results.csv')

