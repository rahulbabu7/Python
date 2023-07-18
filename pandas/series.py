import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
index= [100,101,102,103]
s = pd.Series(data,index= index)
print(s)