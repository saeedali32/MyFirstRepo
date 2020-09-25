class Dog:

    legs = 4

    def __init__(self, name_parameter_value):
        self.name = name_parameter_value
   
    def woof(self):
        return "WOOF"

abc = Dog("rover")
xyz = Dog("Lucy")


print(f"The dog's name is {abc.name}")
print(f"A dog has {abc.legs} legs")
print(f"A dog says {abc.woof()}")
print(f"The dog's name is {xyz.name}")
print(f"A dog has {xyz.legs} legs")
print(f"A dog says {xyz.woof()}")