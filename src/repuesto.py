class Repuesto:
    def __init__(self, codigo, nombre, descripcion, marca, tipo, precio, stock=0, ubicacion="", imagen_path=""):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
        self.stock = stock
        self.ubicacion = ubicacion
        self.imagen_path = imagen_path

    def to_json(self):
        """Convierte el objeto en un diccionario para exportar a JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "marca": self.marca,
            "tipo": self.tipo,
            "precio": self.precio,
            "stock": self.stock,
            "ubicacion": self.ubicacion,
            "imagen_path": self.imagen_path,
        }
