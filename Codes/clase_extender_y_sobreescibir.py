class Producto:
    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio
    def info(self) -> None:
        print(f'{self.nombre} cuesta {self.precio}')
    def costo_final(self) -> float:
        """El costo final incluye un 16% de iva"""
        return 1.16 * self.precio

class Libro(Producto):
    # Extendiendo el inicializador
    def __init__(self, nombre, precio, autor) -> None:
        super().__init__(nombre, precio)
        self.autor = autor
    # Extendiendo método
    def info(self):
        super().info()
        print(f'autor: {self.autor}')

class Leche(Producto):
    # Reemplazando método
    def costo_final(self) -> float:
        """Productos de la canasta básica no tienen iva"""
        return self.precio
