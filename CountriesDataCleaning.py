#!/usr/bin/env python
# coding: utf-8

# In[220]:


import pandas as pd
import numpy as np


# In[238]:


countries = pd.read_csv("country_profile_variables.csv")
##Data observations 
countries.info()
countries


# In[239]:


##Treating invalid values: we can see that instead of NANs, most of the columns contain "-99"; since we do not want these values to skew
##our data, we will replace these wtih NANs
countries = countries.replace('-99', np.NaN)
countries = countries.replace(-99, np.NaN)
countries


# In[240]:


##we want to look at male/female information seperately; right now, that infromation is seperated by a "/ "
countries[['Labour force participation: female','Labour force participation: male']] = countries['Labour force participation (female/male pop. %)'].str.split("/", expand = True)
countries[['Education: Primary gross enrol. ratio: female','Education: Primary gross enrol. ratio: male']] = countries['Education: Primary gross enrol. ratio (f/m per 100 pop.)'].str.split("/", expand = True)
countries[['Education: Secondary gross enrol. ratio: female','Education: Second gross enrol. ratio: male']] = countries['Education: Secondary gross enrol. ratio (f/m per 100 pop.)'].str.split("/", expand = True)
countries[['Education: Tertiary gross enrol. ratio: female','Education: Tertiary gross enrol. ratio: male']] = countries['Education: Tertiary gross enrol. ratio (f/m per 100 pop.)'].str.split("/", expand = True)
countries[['Pop. using improved drinking water %: urban','Pop. using improved drinking water %: rural']] = countries['Pop. using improved drinking water (urban/rural, %)'].str.split("/", expand = True)
countries[['Life expectancy at birth: female','Life expectancy at birth: male']] = countries['Life expectancy at birth (females/males, years)'].str.split("/", expand = True)

countries.info()


# In[241]:


countries = pd.melt(countries, id_vars = ['country','Region'])
#countries
countries
#countries


# In[247]:





# In[242]:


##countries.info()
##we will exclude certain columns 

countries = countries[countries.columns[~countries.columns.isin(['Population age distribution (0-14 / 60+ years, %)','Life expectancy at birth (females/males, years)'
                                                                 ,'Forested area (% of land area)', 'Pop. using improved sanitation facilities (urban/rural, %)'
                                                                 ,'Pop. using improved drinking water (urban/rural, %)', 'Education: Tertiary gross enrol. ratio (f/m per 100 pop.)'
                                                                 , 'Education: Secondary gross enrol. ratio (f/m per 100 pop.)', 'Education: Primary gross enrol. ratio (f/m per 100 pop.)'
                                                                 ,'International migrant stock (000/% of total pop.)'
                                                
                                                                 
                                                                 
                                                                ])]]


# In[249]:


countries['value'] = pd.to_numeric(countries.value, errors = 'coerce')

countries.info()


# In[ ]:


countries.to_csv('countries_updated.csv')

