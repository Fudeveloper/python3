# coding=utf-8
list = []
with open('title.txt') as f:

    for i in range(200):
        line_data = f.readline()
        list.append(line_data)
    print list




