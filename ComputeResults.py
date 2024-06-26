from scipy.stats import ttest_ind_from_stats
import pandas as pd
data = pd.read_csv(r'C:\Users\elkhillc\OneDrive - The University of Colorado Denver\MIP\Writing\Meetings\SIPAIM 2024\AggregatedResults.csv', index_col= 0)

types = ['pixel','volume']
baseline = 'our model'
comparisons = ['PCA']
models = ["brain ageing", "pca model", "dcgan", "no ad", "no cond"]

for t in types:
    for model in models:
        res = ttest_ind_from_stats(data.loc['mean',f'{baseline} {t}'], data.loc['std',f'{baseline} {t}'], data.loc['nobs',f'{baseline} {t}'], data.loc['mean',f'{model} {t}'], data.loc['std',f'{model} {t}'], data.loc['nobs',f'{model} {t}'])
        print(f'{model} {t}: {res.pvalue:0.6f}')