import pandas as pd
import csv
import matplotlib.pyplot as plt
import platform
import csv
f = open('subwaytime.csv', encoding = 'utf-8-sig')
data = csv.reader(f)
next(data)
next(data)


import pandas as pd
df = pd.read_csv ('subwaytime.csv')

print(df)

df[('호선명', 'Unnamed: 1_level_1')]
df[('지하철역', 'Unnamed: 3_level_1')]