# coding:utf-8
data = ""
with open('vision.txt') as f:
    data = f.read().decode('utf-8')

def get_vision_by_start_index(start_index):
    return data[start_index:start_index+50].encode('utf-8')

# print get_content_by_start_and_end(0,200)

# print len(data)