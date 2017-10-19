sum = 0
with open('complete.txt') as f:
    for line in f:
        # sum+=1
        # print line.strip()
        with open('final.txt','a') as final:
            final.write(line.strip().split('----')[1]+'\n')


