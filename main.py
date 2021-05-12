# print('Hi this is Talha')
# name = input('What is your age:')
# print('Talha age is' + name)

# in python we can create our owm custom class
# creating a new instance or object in a class is called instantiation.

class BigObject: #class
    pass
obj1 = BigObject() #instanciate
obj2 = BigObject() #we can instantiate multiple objects

# more indepth class examples
class PlayersCharacter:
    def __init__(self,name,age): #special method, we can have multiple attributes for one method
        self.name = name #attributes that can be used by using a .notation.
        self.age = age

    def run(self):
        print('run')
        return 'done'
#this function will print run and None, It's not returning anything that's why it will print none

player1 = PlayersCharacter('Harry',44)
player1.attack = 50 #we can also add different attribute for the same object player1

print(player1)
print(player1.name)
print(player1.age)
print(player1.attack)
print(player1.run())
