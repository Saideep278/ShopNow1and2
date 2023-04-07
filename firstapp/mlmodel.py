import numpy as np
import pandas as pd
import joblib as jb
#CONTEXT BASED
pro = pd.read_csv(r'/Users/saideepchakilam/Desktop/projects/dataset2.csv')
#print(pro.head(1))
pro['tag'] = pro['tag'].apply(lambda x:x.lower())

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features =5000,stop_words='english')

vectors = cv.fit_transform(pro['tag']).toarray()

import nltk

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
  y = []
  for i in text.split():
    y.append(ps.stem(i))

  return " ".join(y)


pro['tag'] = pro['tag'].apply(stem)

from sklearn.metrics.pairwise import cosine_similarity

sm = cosine_similarity(vectors)

sorted(list(enumerate(sm[0])),reverse=True,key=lambda x:x[1])[1:6]

def recommend(product):
  d=[]
  did=[]
  distances = sm[product]
  lst = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

  for i in lst:
    print(pro.iloc[i[0]].tittle)
    d.append(pro.iloc[i[0]].tittle)
    did.append(pro.iloc[i[0]].id)


  return d

def recommendphoto(product):
  did=[]
  distances = sm[product]
  lst = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

  for i in lst:
    did.append(pro.iloc[i[0]].id)

  return did


def returnname(id):
    return pro.iloc[id].tittle
