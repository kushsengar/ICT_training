class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("hello my name is" ,self.name  , "and my age is " ,self.age)

class person1(person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
        
class person2(person1):
    def __init__(self, name, age, gender, address):
        super().__init__(name, age, gender)
        self.address = address


p2 = person2("ankita",22,"F","rau")
print(p2.name)