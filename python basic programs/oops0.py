class gp:
    def __init__(self , id):
        self.id = id

class p(gp):
    def __init__(self , id ,comp_code):
        super().__init__(id)
        self.comp_code = comp_code

obj = p(107,58593)
print(obj.id)