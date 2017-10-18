# coding:utf-8
data = ""
with open('idea.txt') as f:
    data = f.read().decode('utf-8')

def get_content_by_start(start_index):
    return data[start_index:start_index+50].encode('utf-8')

# print get_content_by_start(0)

# print len(data)