class Student:
    def __init__(self):
        self.name = "Robzi"
        self.age = 6
        self.height = 213
        self.school = "Minecraft Monster School"

    def Eat(self):
        super().eat()


    def AboutMe(self):
        print("My name is " + self.name)
        print("My age is " + self.age.__str__())
        print("My height is " + self.height.__str__())


def nextSquare():
    i = 2

    while True:
        yield i * i
        i += 2



for num in nextSquare():
    if num > 100:
        break
    print(num)