def fileExHandle():
    try:
        with open("fille.txt",'r') as v:
            print(v.read())
    except:
        print("file not found")
    finally:  
        print("I will always be there ")  
fileExHandle()
