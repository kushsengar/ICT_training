class calculator:
    @staticmethod
    def add(val1 , val2):
        return val1 + val2
    @staticmethod
    def subtract(val1 , val2):
        return val1 - val2
    @staticmethod
    def multiply(val1 , val2):
        return val1 * val2
    @staticmethod
    def divide(val1 , val2):
        if val2 == 0:
            return "Error: Division by zero is not allowed"
        return val1 / val2
    
cal = calculator()
print(cal.add(5, 7))  
print(cal.subtract(5, 7))  
print(cal.multiply(5, 7))
print(cal.divide(12,0))