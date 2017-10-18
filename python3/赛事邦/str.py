str = ''
with open('1.txt', 'r') as f:
    data = f.read()
    for i in data:
        if i==' 'or i=='\n':
            pass
        else:
            str += i
    print(len(str))
