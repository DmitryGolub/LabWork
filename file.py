class Figur:
    def __init__(self, color, s):
        self.color = color
        self.s = s

    def get_data(self):
        return f"{self.color} {self.s}"


class Rectangle(Figur):
    def __init__(self, color, s, a, b):
        super().__init__(color, s)
        self.a = a
        self.b = b

    def get_data(self):
        return super().get_data() + f" {self.a} {self.b}"

r1 = Rectangle('red', 20, 4, 5)
print(r1.get_data())


