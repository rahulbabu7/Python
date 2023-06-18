import pandas as pd
import numpy as np

examResult = {
    'REGNO':["SJC24CS067","SJC24CS069","SJC24CS089"],
    'name':["Rahul","Hari","Christy "],
    'physics':[78,90,66],
    'chemistry':[67,88,88],
    'maths':[95,77,55]
}

df = pd.DataFrame(examResult,index=[1,2,3])

#! writing dataframe to csv
df.to_csv("EXAMresult.csv",index=False)
print(df)