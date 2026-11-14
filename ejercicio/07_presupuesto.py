# Alexander
# Tarea: 07_presupuesto.py
# Ayuda externa: usé Claude como apoyo. El programa pide los datos, calcula el
# total y el saldo, y comprueba si el presupuesto alcanza.

descripcion = input("Descripción del producto: ")
presupuesto = float(input("Presupuesto disponible: C$ "))
precio_unitario = float(input("Precio del producto: C$ "))
cantidad = int(input("Cantidad: "))

total = precio_unitario * cantidad
saldo = presupuesto - total

# El presupuesto alcanza cuando el saldo no es negativo (saldo >= 0).
es_suficiente = saldo >= 0

print("RESUMEN DEL PRESUPUESTO")
print(f"Producto: {descripcion}")
print(f"Presupuesto: C$ {presupuesto:.2f}")
print(f"Total: C$ {total:.2f}")
print(f"Saldo disponible: C$ {saldo:.2f}")
print(es_suficiente)

if es_suficiente:
    print("El presupuesto es suficiente.")
else:
    print(f"El presupuesto NO es suficiente: faltan C$ {-saldo:.2f}")
    