import pandas as pd

h1b_data = pd.read_csv('data.csv')
desired_cols = ['JOB_TITLE',
        'EMPLOYER_NAME',
        'WORKSITE_STATE',
        'WORKSITE_CITY',
        'WAGE_RATE_OF_PAY_FROM']

# Remove non-yearly-rate WAGE_RATE_OF_PAY_FROM records
a = h1b_data[desired_cols]

a['WAGE_RATE_OF_PAY_FROM'] = a['WAGE_RATE_OF_PAY_FROM'].apply(
    lambda x: int(x.replace(',','')[:-3]))
b = a[~(a['WAGE_RATE_OF_PAY_FROM'] < 10000)]
b = b.dropna()

c = b.copy()
TECHIES = set(['SOFTWARE', 'PROGRAMMER', 'DEVELOPER', 'ENGINEER'])
from numpy.random import rand
TECHIE_PRIOR = 0.95
# 95% of the time, TECHIES will be identified as a HENRY
is_a_techie = lambda job_title: any([word in TECHIES for word in job_title.upper().strip().split()]) and rand() <= TECHIE_PRIOR
c['HENRY'] = c['JOB_TITLE'].map(is_a_techie)


c.to_csv('h1b_sampler.tsv', sep='\t', index=False)
import random
random.seed(1337)
c.sample(frac=0.01, replace=True).to_csv('h1b_henry_sampler_{}_prior.tsv'.format(TECHIE_PRIOR), sep='\t', index=False, header=False)

