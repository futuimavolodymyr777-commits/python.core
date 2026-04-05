class Animal: # ідентифікатор (назва) класу
    def __init__(self, name, type, sound) -> None:
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        print(f'Animal named {self.name} of type {self.type} makes sound {self.sound}')

    def __str__(self) -> str:
        return f'Name: {self.name}\nType: {self.type}\nSound: {self.sound}'

animal1 = Animal('Buddy', 'dog', 'WOOF') # конструктор класу
animal1.make_sound() # виклик методу
# print(animal1.type)

animal2 = Animal('Marcel', 'cat', 'MEOW')
# print(animal2.type)
animal2.make_sound()

# print(type(animal1))
print(animal1, animal2, sep='\n')