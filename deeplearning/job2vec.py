
# coding: utf-8

# In[1]:


import pandas as pd

def get_training_data(smol=0.01, seed=1337):
    h1b_data = pd.read_csv('data.csv')
    desired_cols = ['JOB_TITLE',
        'EMPLOYER_NAME',
        'WORKSITE_STATE',
        'WORKSITE_CITY',
        'WAGE_RATE_OF_PAY_FROM']
    a = h1b_data[desired_cols]
    a['WAGE_RATE_OF_PAY_FROM'] = a['WAGE_RATE_OF_PAY_FROM'].apply(lambda x: int(x.replace(',','')[:-3]))
    b = a[~(a['WAGE_RATE_OF_PAY_FROM'] < 10000)]
    b = b.dropna()
    c = b.copy()
    TECHIES = set(['SOFTWARE', 'PROGRAMMER', 'DEVELOPER', 'ENGINEER'])
    from numpy.random import rand
    is_a_techie = lambda job_title: any([word in TECHIES for word in job_title.upper().strip().split()]) and rand() <= 0.95
    c['HENRY'] = c['JOB_TITLE'].map(is_a_techie)
    return c.sample(frac=smol, replace=False, random_state=1337)

train = get_training_data(0.001)
print(len(train))
train.head()


# In[2]:


train['JOB_TITLE'].describe()


# In[3]:


from gensim.models import Word2Vec


# In[48]:


h1b_data = pd.read_csv('data.csv')
desired_cols = ['JOB_TITLE',
    'EMPLOYER_NAME',
    'WORKSITE_STATE',
    'WORKSITE_CITY',
    'WAGE_RATE_OF_PAY_FROM']
a = h1b_data[desired_cols]


# In[151]:


# a['JOB_TITLE']
# a['WORKSITE_CITY'].describe()

job_freqs = a[['JOB_TITLE', 'WORKSITE_CITY']].groupby('WORKSITE_CITY').count()
# print(job_freqs)


# In[161]:


top_96 = job_freqs[job_freqs['JOB_TITLE']>1000].sort_values('JOB_TITLE', ascending=False)


# In[174]:


pa_jobs = a[a['JOB_TITLE']=='BUSINESS ANALYST'][['JOB_TITLE', 'WORKSITE_CITY']].groupby('WORKSITE_CITY').count()
pa_jobs['WORKSITE_CITY'] = pa_jobs.index
top_96['WORKSITE_CITY'] = top_96.index

print(len(a[a['JOB_TITLE']=='BUSINESS ANALYST']))

pa_jobs.head()


# In[173]:


pd.merge(top_96, pa_jobs, how='left', on='WORKSITE_CITY')


# In[77]:


sentences=map(str, a['JOB_TITLE'].tolist())
print(list(sentences)[:10])
# model = Word2Vec(sentences=sentences)
model = Word2Vec(zip(sentences, ["sentence"]*len(list(sentences))), size=2, min_count=0)
# model.build_vocab(sentences=sentences, keep_raw_vocab=True)

model.wv.vocab


# In[137]:


import gensim
# sentences = ['ASSOCIATE DATA INTEGRATION', 'SENIOR ASSOCIATE', '.NET SOFTWARE PROGRAMMER', 'PROJECT MANAGER', 'ASSOCIATE - ESOTERIC ASSET BACKED SECURITIES', 'CREDIT RISK METRICS SPECIALIST', 'BUSINESS SYSTEMS ANALYST', 'PROGRAMMER ANALYST', 'PROGRAMMER ANALYST', 'PROGRAMMER ANALYST']
sentences = list(map(lambda x: [str(x)], a['JOB_TITLE'].tolist()))
sentence_tokens = list(map(lambda x: str(x).replace(',','').split(), a['JOB_TITLE'].tolist()))
print(sentences[:5])
print(sentence_tokens[:5])
# train word2vec on the two sentences
# model = gensim.models.Word2Vec(sentences, min_count=1)

# model = gensim.models.Word2Vec(zip(sentences, ["sentence"]*len(list(sentences))), size=2, min_count=0, window=1, sg=0, negative=4)
# model = gensim.models.Word2Vec(sentences, size=2, min_count=0, window=1, sg=0, negative=4)
model = gensim.models.Word2Vec(min_count=0, window=1, sg=0)
model.build_vocab(sentence_tokens)
# model.build_vocab(sentences)
model.train(sentences, total_examples=len(sentences), epochs=5)

# model = gensim.models.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)



# In[138]:


print(model.wv['ENGINEER'])
# print(dir(model))
model.predict_output_word(['VP'])
# print(model.wv['VP,'])
# print(model.wv['VP, SENIOR PREPARER OF FINANCIAL STATEMENTS'])
# model.most_similar('SOFTWARE DEVELOPER')


# In[18]:


model.save('job2vec.model')


# In[19]:


model = Word2Vec.load('job2vec.model')


# In[35]:


print(model)
print(dir(model))
# print(model.vocab.keys())
# model.scan_vocab(['engineer'])
print(model.raw_vocab)
# model.wv['ENGINEER']

