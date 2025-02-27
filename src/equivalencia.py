class Equivalencia:
    def __init__(self, codigo, equivalentes):
        self.codigo = codigo
        self.equivalentes = equivalentes  # Lista de códigos equivalentes

    def to_json(self):
        return {
            "codigo": self.codigo,
            "equivalentes": self.equivalentes,
        }
