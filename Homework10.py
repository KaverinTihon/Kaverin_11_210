class Asasas:
    def __init__(self, kind, height):
         self.kind = kind
         self.age = 0
         self.height = height  
    def grow(self):
        self.age += 1
        self.height += 0.5
    def grow2(self, height):
        self.age += 5
        self.height += height
    def a(self):
        self.kind += 'a'
class Cocky(Asasas):
    def __init__(self, kind, height, width, length):
        super().__init__(kind, height)
        self.width = width
        self.length = length
    def grow(self):
        self.age += 10
        self.height += 1000
    def shrink(self):
        self.width -= 1
        self.height -= 0.5
        self.length -= 1
    def shrink2(self):
        self.width -= self.width/2
        self.height -= self.height/2
        self.length -= self.length/2
class Balals(Cocky):
    def __init__(self, kind, height, width, length, amount, productivity):
        super().__init__(kind, height, width, length)
        self.amount = amount
        self.productivity = productivity
    def grow(self):
        self.age = 1
        self.height += 1000
    def multiply(self):
        self.amount *= 10
    def production(self):
        self.productivity = self.amount/((self.width+self.height+self.length)/3)
    def info(self):
         print ("age: {}. type: {}. height: {} meters. width: {} meters. length: {} meters. amount: {}. productivity: {}".format(self.age, self.kind, self.height, self.width, self.length, self.amount, self.productivity))  
ananas=Balals('small',30,1000,1000,1000000,2000)
ananas.grow()
ananas.shrink2()
ananas.multiply()
ananas.production()
ananas.a()
ananas.info()

