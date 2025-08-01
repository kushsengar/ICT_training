n = int(input("Enter n: "))
prev = 0
curr = 1
for i in range(n):
    next = curr + prev
    prev = curr
    curr = next

print(prev) 
