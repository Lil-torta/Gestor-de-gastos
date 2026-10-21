from datetime import date

class Gasto:
    def __init__(self, monto, categoria, descripcion, fecha):
        if not isinstance(monto, (int, float)):
           raise TypeError(f'El monto debe ser un valor numerico: {monto}')
       
        if monto <= 0:
            raise ValueError(f'El monto debe ser mayor a cero: {monto}')

        if not isinstance(categoria, str):
            raise TypeError(f'La categoria debe ser un exto: {categoria}')
        
        if not categoria.strip():
            raise ValueError(f'La categoria no puede estar vacia: {categoria}')
        
        self.monto = monto 
        self.categoria = categoria
        self.descripcion = descripcion
        self.fecha = fecha

    @classmethod
    def desde_diccionario(cls, datos):
        
        if isinstance(datos['fecha'], str):
            fecha_limpia = date.fromisoformat(datos['fecha'])
        else:
            fecha_limpia = datos['fecha']

        return cls(datos['monto'],  datos['categoria'], datos['descripcion'], fecha_limpia)

    def __str__(self):
        return f"[{self.fecha}] {self.categoria} | {self.descripcion}: ${self.monto:.2f}"

    def a_diccionario(self):
        return {
            'monto': self.monto,
            'categoria': self.categoria,
            'descripcion': self.descripcion,
            'fecha': self.fecha.isoformat()
              }
if __name__ == "__main__":
    g1 = Gasto(150.5, "comida", "tacos", date(2026, 10, 13))
    d = g1.a_diccionario()
    g2 = Gasto.desde_diccionario(d)
    print(g1)
    print(g2)
    print(g1.a_diccionario() == g2.a_diccionario())   # debe dar True
