import timeit

def run():
    sum = 0
    for i in range(100):
        sum += 256

print(timeit.timeit(run))