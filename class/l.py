class Gazirovka:
    def __init__(self, fruit):
        if isinstance(fruit, str):
            self.fruit = fruit
        else:
            self.fruit = None

    def show_lemonade(self):
        if self.fruit:
            print("У Вас лимонад с ", self.fruit)
        else:
            print("У Вас классический лимонад")

a = Gazirovka("")
b = Gazirovka('малина')
b1 = Gazirovka(1)
a.show_lemonade()
b.show_lemonade()
b1.show_lemonade()

