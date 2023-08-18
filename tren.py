

def tren(destino, valor):
    
    print("ingresó al sistema de pago")
    nombre=input("ingrese su nombre completo")
    while True:
        tarjeta=int(input("ingrese el número de tarjeta de crédito"))
        verificacion = 16
        if len(tarjeta) ==verificacion:
            break
    

    id=int(input("ingrese el número de identificación"))
    print(".....................................")
    print("Estación principal")
    print(".....................................")
    print(f"A nombre del cliente {nombre} ")
    print(f"Su número de identificación es: {id}")
    print( f"El destino es: {destino} " )
    print(f"El valor a pagar es: {valor} ")
    




while True:

    print("Bienvenido a la estación de trenes.")

    print("Los números de los destinos son los siguientes: ") 

    print("1: Berlín;  2: París;  3: Madrid;  4: Londres")
    opcion_menu=int(input("ingrese el destino"))

    if opcion_menu == 1:

        destino = "Berlín"
        valor = 10
        print("su destino es Berlín")
        tren(destino, valor)


    elif opcion_menu == 2:

        destino = "París"
        valor = 18
        print("su destino es París")
        tren(destino, valor)


    elif opcion_menu == 3:

        destino = "Madrid"
        valor = 15
        print("su destino es Madrid")
        tren(destino, valor)


    elif opcion_menu == 4:

        destino = "Londres"
        valor = 12
        print("su destino es Londres")
        tren(destino, valor)


        break

   










