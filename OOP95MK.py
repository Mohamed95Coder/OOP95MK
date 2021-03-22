from datetime import date
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return f"my name is {self.name} & my age is {self.age}"
class men(person):
    gender = 'male'
    no_of_men=0

    def __init__(self,name , age , voice):
        super().__init__(name,age)
        self.voice = voice
        men.no_of_men +=1

        def display(self):
            string = super().display()
            return string+f"my gender is {self.gender} my voice is{self.voice}"
class women(person):
    gender = 'female'
    no_of_women=0
    def __init__(self,name ,age ,hair):
        super().__init__(name,age)
        self.hair = hair
        women.no_of_women +=1
        def display(self):
            string = super().display()
            return string + f"my gender is {self.gender} my voice is{self.voice}"

           #print(isinstance(women,person)) -> false Why?

class Student:
    no_of_St = 0
    def __init__(self, name, age, think):
        self.__name = name
        self.__age = age
        self.__think = think
        Student.no_of_St += 1

    def describe(self):
        print(f"My name is {self.__name} and my age is {self.__age}")

    def is_ole(self, num):
        if not self.__age <= num:
            print("Too young")
        else:
            print("IS alder")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    @classmethod
    def initfrom(cls, name, birth):
        return cls(name, date.today().year - birth)

class MATH:
    @staticmethod
    def PI():
        return 3.14
class pizza:
    def __init__(self, ingre , radious):
        self.ingr = ingre
        self.radious=radious

    def __str__(self):
        return f'pizza irguments are {self.ingr}&radious is {self.radious}'
    def area(self):
        return pizza.circle_area(self.radious)
    @classmethod
    def veg(cls):
        return cls(["Tomato", "Egg", "greens"],20)

    @classmethod
    def mergr(cls):
        return cls(["Meet", "Fish", "hands"],25)

    @staticmethod
    def circle_area(r):
        return (r**2)*MATH.PI()

stu1 = Student("MK", 30, "ML")
stu2 = Student("Zeyt", 25, "L")
stu1.name = "Megggaaa"
print(stu1.get_name())

stu1.describe()
pizza1 = pizza(["olives", "flafeel", "beans"],30)
pizza2 = pizza.veg()
pizza3 = pizza.mergr()
print(pizza1, pizza2, pizza3)
print(pizza2.area())

man1=men("ALI", 24 , "hard")
men2=men("MK",20,"roboot")
men3=men("MLM",30,"soft")
women1=women("maryam",20,"soft")
wonen2=women("Nour",15,"curle")
print(men2.display())
print(women1.display())
print(women.no_of_women)
print(isinstance(women,person))
# inhertance @classmethod
# encapsulation __name be more secuirty
#inhertance -> class man(person ) part from main class 