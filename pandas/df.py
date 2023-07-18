import pandas as pd
import numpy as np

mydict = {
    'name':['rahul','ronaldo'],
    'age':[20,10]
}
index= [1,2]
df = pd.DataFrame(mydict,index=index)
print(df)

d=pd.read_csv("Test.csv")
print(d)
df.to_csv("Test.csv",index=False)
