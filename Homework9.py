# Добавить к существующему коду 3 метода и 5 атрибутов.
class Student:
    def init(self, name, group, ages, status, profession, exp, hp, hg):
        self.name = name
        self.group = group
        self.ages = ages
        self.status = status
        self.profession = profession
        self.exp = exp
        self.hp = hp
        self.hg = hg

#    def new(cls, *args, **kwargs):
#        print('meow')
#        return super(Student, cls).new(cls)

    def introduce(self):
        print(f'Hi, I am {self.name} from group {self.group}')   #Hi повторяется 2 раза из данного кода

    def say_hi(self):
        print(f'Hi, {self.name}')      #Hi повторяется 2 раза из данного кода
        print(f'Health points are at {self.hp}')

    def age(self):
        print(f"{self.name} is {self.ages} years old")

    def being(self):
        print(f"{self.name} is {self.status}")
        print(f"Favorite food/drink: {self.hg}")

    def job(self):
        print(f"{self.name} is {self.profession}")
        print(f"Working experience is {self.exp}")

    def del(self):
        print(self.name, 'is deleted')

new_group = '11-250'
a = Student('Izida', new_group, 20, 'a human', 'a teacher', 6, 100, 'coffee')
b = Student('Kate', '11-210', 5, 'a cat', 'a homeless', 5, 9, 'whiskas')

a.say_hi()
a.introduce()
a.age()
a.being()
a.job()

b.say_hi()
b.introduce()
b.age()
b.being()
b.job()

class Collection:
    def init(self, list):
        self.list = list

    def len(self):
        return len(self.list)

list = ['Hi', 'Hello']
print(len(list))
