from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
#COLLABRATIVE
import numpy as np
import pandas as pd
prod = pd.read_csv(r'/Users/saideepchakilam/Desktop/projects/d_export.csv',index_col=0)
prod = prod.fillna(0)

ratings_std=prod
item_sim = cosine_similarity(ratings_std.T)
item_sim_df = pd.DataFrame(item_sim,index=prod.columns,columns=prod.columns)

def similar_prod(mn,ur):
  similar_score = item_sim_df[mn]*ur
  similar_score = similar_score.sort_values(ascending = False)

  rlist = list(similar_score.keys())
  a=[]
  for i in range(2,7):
      a.append(rlist[i])

  return  a
