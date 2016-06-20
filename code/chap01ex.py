
# coding: utf-8

# In[1]:

import thinkstats2

dct_file='2002FemPreg.dct'
dat_file='2002FemPreg.dat.gz'


# In[2]:

dct = thinkstats2.ReadStataDct(dct_file)


# In[4]:

df = dct.ReadFixedWidth(dat_file, compression='gzip')


# In[16]:

print(df['pregnum'])


# In[17]:

df.caseid


# In[13]:

from collections import defaultdict

d = defaultdict(list)


# In[14]:

for index, caseid in df.caseid.iteritems():
    d[caseid].append(index)


# In[15]:

d

