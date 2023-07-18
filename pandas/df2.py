import pandas as pd

topperdata = {

    'RegNo':['sjc20cs101','sjc20cs102','sjc20cs103','sjc20cs104',],
    'name':['rahul','arun','ajmal','ali'],
    'sem':['s8','s7','s6','s5'],
    'college':['sjcet','vjscet','ajcet','cet'],
    'cgpa':[9.9,9.8,9.9,9.9]

}
index = [1,2,3,4]
df = pd.DataFrame(topperdata,index=index)
print(df)

#!writing to csv
df.to_csv("topper.csv",index =False) #!no need of index in the csv