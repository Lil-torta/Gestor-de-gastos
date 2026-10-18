from datetime import datetime, date

class Gasto:
    def __init__(self, monto, categoria, descripcion, fecha):
        
        
        
        self.monto = monto 
        self.categoria = categoria
        self.descripcion = descripcion
        self.fecha = fecha

    @classmethod
    def desde_diccionario(cls, monto, catetegoria, descripcion, fecha):
        if isinstance(fecha, str):
            fecha_limpia = datetime.fromisoformat(fecha)
        else:
            fecha_limpia = fecha

        return cls(monto, catetegoria, descripcion, fecha)

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