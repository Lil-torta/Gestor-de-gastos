from datetime import date

class Gasto:
    def __init__(self, monto, categoria, descripcion, fecha):
        self.monto = monto 
        self.categoria = categoria
        self.descripcion = descripcion
        self.fecha = fecha

    def __str__(self):
        return self.a_diccionario()

    def a_diccionario(self):
        return {
            'monto': self.monto,
            'categoria': self.categoria,
            'descripcion': self.descripcion,
            'fecha': self.fecha.isoformat()
              }

g = Gasto(150.5, "comida", "tacos", date.today())
print(g.a_diccionario())