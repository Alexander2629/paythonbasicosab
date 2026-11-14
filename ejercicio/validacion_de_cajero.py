def validar_retiro(saldo, monto):
    # 1. Si el saldo es negativo, mostrar error en la información
    if saldo < 0:
        return "Error: Existe un error en la información del saldo."
    
    # 2. Si el monto a retirar es igual o inferior a cero, rechazar
    if monto <= 0:
        return "Operación rechazada: El monto a retirar debe ser mayor a cero."
    
    # 3. Si el monto supera el saldo disponible, rechazar el retiro
    if monto > saldo:
        return "Retiro rechazado: El monto supera el saldo disponible."
    
    # 4. Si cumple todas las condiciones, calcular saldo restante
    saldo_restante = saldo - monto
    
    # Resultado esperado
    return (
        "===== CAJERO AUTOMÁTICO =====\n\n"
        "Retiro autorizado.\n"
        f"Saldo restante: C$ {saldo_restante:.2f}"
    )

# --- Bloque principal para solicitar datos al usuario ---
try:
    saldo_disponible = float(input("Saldo disponible: "))
    monto_retirar = float(input("Monto a retirar: "))
    
    # Llamamos a la función y mostramos el resultado
    resultado_final = validar_retiro(saldo_disponible, monto_retirar)
    print("\n" + resultado_final)

except ValueError:
    print("Error: Por favor, ingrese valores numéricos válidos.")