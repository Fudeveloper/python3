# coding:utf-8
data = ""
with open('finance.txt') as f:
    data = f.read().decode('utf-8')

def get_finance_by_start_index(start_index):
    return data[start_index:start_index+50].encode('utf-8')

# print get_finance_by_start_index(0)

