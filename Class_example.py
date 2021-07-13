class Dog:
    def __init__(self,name,color) :
        self.name=name
        self.color=color

    def bark(self):
        print("Woof!")

fido=Dog("corocoro","black")
print(fido.name)
fido.bark() 