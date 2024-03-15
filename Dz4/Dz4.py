class Plane:
    def __init__(self, fuel: int = 367, speed: int = 1001):
        self.fuel = fuel
        self.speed = speed

    def drive(self, person):
        if person.age < 18:
            print(f"{person.name} вам недостатньо років, щоб вести літак")
        else:
            print(f"{person.name} веде літак зі швидкістю {self.speed} км/год")

    def print_info(self):
        print(f"Пальне:{self.fuel}")


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


name1 = input("Введіть ім'я: ")
age1 = int(input("Введіть вік: "))

person1 = Human(name1, age1)
plane = Plane()

plane.drive(person1)
plane.print_info()
