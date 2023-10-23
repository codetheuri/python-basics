class animals:
    def speak(self):
        print("Animal speaking")
class dog(animals):
    def bark(self):
        print("dog barks")

class dogChild(dog):
     def eats(self):
         print("drinking milk")

dog=dog()
dog.speak()
dog.bark()
dogs=dogChild()
dogs.eats()
dogs.bark()
dogs.speak()