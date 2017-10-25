import numpy as np
import pandas as pd
from tempfile import NamedTemporaryFile

data = pd.read_excel('1.xls')
# print(data)

df = pd.DataFrame(data)
# [1:]
# print(int(df['联系电话'][1]))

# print(pd.DataFrame(df.head()))



phone_list = []
with open('final.txt') as f:
    for i in f:
        phone_list.append(i.strip())
# print(phone_list)


wang =[]
sum = 0
for index in range(len(df)):
    # print(1)

    now_phone = str((df['联系电话'][index])).split('.')[0]

    if now_phone not in phone_list:
        # pass
        # print(now_phone)
        df =df.drop(index)
        # print(now_phone)
        # print(df[index:index+1])
        # wang.append(df[index:index+1])
    # else:
    #     print(now_phone)
print(df)
res = pd.DataFrame(df)
writer = pd.ExcelWriter('output.xlsx')
res.to_excel(writer,'phone')
writer.save()


