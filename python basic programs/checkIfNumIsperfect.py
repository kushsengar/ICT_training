
def checkIfperfect(n):
    sum = 0
    for i in range(1,n):
        if(n % i == 0):
            sum = sum + i

    return n==sum

n = int(input("Enter number :"))

print(checkIfperfect(n))