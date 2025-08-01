numbers = (5,7,9,5,6,3,10,12,16)
n = len(numbers)
cntEven = 0
cntOdd = 0
for i in range(0 , n):
    if numbers[i]%2==0:
        cntEven+=1
    else:
        cntOdd+=1
print("Count of Even numbers is :" , cntEven)
print("count of Odd numbers is :" , cntOdd)