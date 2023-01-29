class fish:
    def __init__(self, z, p):
        self.name = z
        self.food = p

    @property
    def eat(self):
        return f" {self.name} eats {self.food}"


a = fish("nemo ", "worm ")
print(a.name, a.food)
print(a.eat)
