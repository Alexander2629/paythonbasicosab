  # Tarifario
# Pedir distancia al usuario
# Evaluar valor introducido por el usuario
# Si valor negativo o cero, indicar que no es un valor correcto
# Hasta 3km C$ 30
# Más de 3 hasta 8 C# 50
# Más de 8 C$ 75
 
distancia = float(input("Ingrese la distancia en KM: "))
 
if distancia <= 0:
    tarifa = 0 
elif distancia <= 3:
    tarifa = 30
elif distancia <= 8:
    tarifa = 50
else:
    tarifa = 75
 
if tarifa <= 0:
    mensaje = "Que Camine"
else:
    mensaje = f"Tarifa: {tarifa}"
print("===== SERVICIO DE ENTREGA =====")
print(f"Distancia: {distancia}")
print(mensaje)
 
#if distancia <= 3:
#    tarifa = 30
#if distancia > 3 and distancia <= 8:
#    tarifa = 50
 
#print(tarifa)