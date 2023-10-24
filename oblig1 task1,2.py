#!/usr/bin/env python
# coding: utf-8

# In[32]:


#CREATE a df from faker liste 
from faker import Faker
import pandas as pd
#from laundromat.spacy.spacy_model import SpacyModel
from faker.providers.credit_card import Provider as CreditCardProvider #Add creditcards to faker


# In[33]:


fake = Faker(['no_NO'])


# In[36]:


for _ in range(100):
    name=fake.name()
    addresse=fake.address()
    ssn=fake.ssn()
    credit=fake.credit_card_number()
    impv4=fake.ipv4()
    print(name, addresse, ssn, credit, impv4)
    print()
  


# In[37]:


df = pd.DataFrame(columns=['Navn','Adresse', 'PersonNr' ,'CreditCard', 'ipv4']) # Create a empty df
row1= fake.name()
row2= fake.address()
row3= fake.ssn()
row4= fake.credit_card_number()
row5= fake.ipv4()



df.loc['Navn']=row1
df.loc['Adresse']=row2
df.loc['PersonNr']=row3
df.loc['CreditCard']=row4
df.loc['ipv4']=row5
df.head(5)


# In[38]:


#Anonymization


# In[40]:


# gå fra df to array
textArray = []
for index, row in df.iterrows():

    name = row[0] 
    textArray=[]
for index, row in df.iterrows():

    name = row[0] 
    adress = row[1]
    ssn = row[2]
    cc = row[3]
    #Using f string we can now create a new string with the values, and
    #append (add) that string to the text array
    textArray.append(f'Hi, my name is {name}. I wonder if you deliver to {adress}')
    print(textArray)


# In[ ]:





# In[3]:





# In[4]:





# In[ ]:




