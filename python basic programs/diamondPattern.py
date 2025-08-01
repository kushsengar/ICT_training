for i in range(0 , 9):
    if i < 5:
        for j in range(0 , i+1):
            print("*" , end =" ")
        print("\n")
    else:
        for j in range(0 , 9-i):
            print("*" , end =" ")
        print("\n")
       
   