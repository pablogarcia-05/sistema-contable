movimientos = []

def registrar_movimiento(tipo, concepto, monto):
    movimientos.append({
        "tipo": tipo,
        "concepto": concepto,
        "monto": monto
    })
    print("Movimiento registrado correctamente.\n")


def mostrar_movimientos():
    if not movimientos:
        print("No hay movimientos registrados.\n")
        return

    print("\n===== LIBRO CONTABLE =====")
    for i, mov in enumerate(movimientos, start=1):
        print(f"{i}. {mov['tipo']} | {mov['concepto']} | ${mov['monto']:.2f}")
    print()


def calcular_saldo():
    saldo = 0
    for mov in movimientos:
        if mov["tipo"] == "Ingreso":
            saldo += mov["monto"]
        else:
            saldo -= mov["monto"]
    return saldo


while True:
    print("===== SISTEMA CONTABLE =====")
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Ver movimientos")
    print("4. Ver saldo")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        concepto = input("Concepto del ingreso: ")
        monto = float(input("Monto: "))
        registrar_movimiento("Ingreso", concepto, monto)

    elif opcion == "2":
        concepto = input("Concepto del gasto: ")
        monto = float(input("Monto: "))
        registrar_movimiento("Gasto", concepto, monto)

    elif opcion == "3":
        mostrar_movimientos()

    elif opcion == "4":
        print(f"\nSaldo actual: ${calcular_saldo():.2f}\n")

    elif opcion == "5":
        print("Gracias por usar el sistema contable.")
        break

    else:
        print("Opción no válida.\n")