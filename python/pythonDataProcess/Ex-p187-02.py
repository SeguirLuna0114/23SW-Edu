import pandas as pd

filename = 'data02.csv'
df = pd.read_csv(filename, header=None, index_col=0, names=['학년','국어','영어','수학'])

df.index.name = '이름'
df.loc[['강호민'],['영어']] = 40
df.loc[['박영희'],['국어']] = 30

print(df)
#       학년    국어    영어  수학
# 이름
# 강호민    1  10.0  40.0  20
# 신사임당   2  20.0  30.0  40
# 박영희    1  30.0  60.0  20
# 심형식    1  60.0  50.0  30