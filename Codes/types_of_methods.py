class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    # método de instancia (utiliza la instancia)
    def area(self):
        return self.width * self.height

    # método de clase (utiliza la clase)
    @classmethod
    def desde_iterable(cls, iterable):
        return cls(*iterable)

    # método estático (no utiliza ni la clase ni la instancia)
    @staticmethod
    def info():
        print('Este es un rectángulo')


r1 = Rectangle(3, 5)
r2 = Rectangle.desde_iterable([4, 7])

# r2.info()
# r2.area()

