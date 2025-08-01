# def maxOfThreeNums(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else :
#         return c
    
# print(maxOfThreeNums(5,-4,0))

var = lambda a,b,c : max(a,b,c)
print(var(5,0,-5)) 