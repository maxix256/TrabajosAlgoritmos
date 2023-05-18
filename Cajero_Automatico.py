saldo = 10000
contador = 1

while contador <= 3:
    print("Escribir contraseña")
    contraseña = input()
    if contraseña == "1234":
        contador = 4
        respuesta = 0
        print("1: Retirar dinero")
        print("2: Salir")
        respuesta = int(input())
        if respuesta == 1:
            print("Ingresar monto a retirar")
            monto = int(input())
            if monto <= saldo:
                saldo -= monto
                print("Por favor retire el dinero")
                print("Tu saldo actual es=", saldo)
            else:
                print("Saldo insuficiente")
                print("Tu saldo actual es=", saldo)
    else:
        contador += 1
        if contador == 4:
            print("Numeros de intentos superados")
        else:
            print("La cotraseña es incorrecta")