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

b = b.sample(frac=0.01, replace=True)

b.to_csv('h1b_sampler.tsv', sep='\t', index=False)
