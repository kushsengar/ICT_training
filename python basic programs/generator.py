def gen(a):
    i=0
    while i<=a:
        yield i
        i+=1

for i in gen(5):
    print(i)