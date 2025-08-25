class Cat:
    MEOWS = 3 # this is a class variable / default? / so is this a constant????

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()




