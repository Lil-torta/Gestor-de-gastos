from datetime import date
import json

# Normalizar la categoria, mejorar usando .strip.lower o capitalize
# Gasto(true ) pasa la validacion, mejorar con isinstance(True, int) y exclusion de bool
class Gasto:
    def __init__(self, monto, categoria, descripcion, fecha):
        if not isinstance(monto, (int, float)):
           raise TypeError(f'El monto debe ser un valor numerico: {monto}')
       
        if monto <= 0:
            raise ValueError(f'El monto debe ser mayor a cero: {monto}')

        if not isinstance(categoria, str):
            raise TypeError(f'La categoria debe ser un texto: {categoria}')
        
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
# Mejorar mensaje incluyendo type(gasto).__name__.
# Mejorar u convencion _gastos
#Usae sum() en total()
class Cuenta:
    def __init__(self,nombre):
        self.nombre = nombre
        self.gastos = []

    def agregar_gasto(self, gasto):
        if not isinstance(gasto, Gasto):
            raise TypeError(f'Solo se pueden agregar objetos del tipo Gasto')

        self.gastos.append(gasto)

    def total(self):
        suma_total = 0
        for gasto in self.gastos:
            suma_total += gasto.monto
        return suma_total

    def total_por_categoria(self):
        total = {} 
        for gasto in self.gastos:
            categoria = gasto.categoria
            monto = gasto.monto
            total[categoria] = total.get(categoria, 0) + monto
        return total
    def guardar(self, ruta):
        datos = {
            "nombre": self.nombre,
            'gastos':[gasto.a_diccionario() for gasto in self.gastos]
        }
        with open(ruta, 'w', encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)

    @classmethod
    def cargar(cls, ruta):
        with open(ruta, 'r', encoding="utf-8") as f:
           datos = json.load(f)
        cuenta = cls(datos['nombre'])

        for dato in datos['gastos']:
            gasto = Gasto.desde_diccionario(dato)
            cuenta.agregar_gasto(gasto)
        return cuenta
if __name__ == "__main__":
    cuenta = Cuenta("Cuenta personal")

    g1 = Gasto(150.5, "comida", "tacos", date(2026, 10, 13))
    g2 = Gasto(80, "transporte", "uber", date(2026, 10, 14))
    g3 = Gasto(250, "educación", "curso Python", date(2026, 10, 15))

    cuenta.agregar_gasto(g1)
    cuenta.agregar_gasto(g2)
    cuenta.agregar_gasto(g3)
    
    cuenta.guardar("gastos.json")

    print(cuenta.total())
    print(cuenta.total_por_categoria())
    #cuenta_cargada = Cuenta.cargar('gastos.json')
    #cuenta_cargada = Cuenta.cargar('sin_monto.json')
    cuenta_cargada = Cuenta.cargar('fecha_mala.json')
    #cuenta_cargada = Cuenta.cargar('sin_existencia.json')
    #cuenta_cargada = Cuenta.cargar('corrupto.json')
    #cuenta_cargada = cuenta.cargar('monto_negativo.json')
    
    print(cuenta_cargada.total())
    print(cuenta_cargada.total_por_categoria())
    
    print(cuenta.total() == cuenta_cargada.total())
    
    print(
        cuenta.total_por_categoria()
        ==
        cuenta_cargada.total_por_categoria()
        )
    assert cuenta.nombre == cuenta_cargada.nombre, 'Los nombres no coinciden'
    lista = [gasto.a_diccionario() for gasto in cuenta.gastos]
    lista2 = [gasto.a_diccionario() for gasto in cuenta_cargada.gastos]
    assert lista == lista2, 'los gastos son diferentes'