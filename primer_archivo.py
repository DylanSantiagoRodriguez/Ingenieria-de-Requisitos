#creado por Dylan Santiago Rodriguez y Sara Maria Ojeda 
#version 1.2, creada 18 de agosto del año 2023

import json
data = json

def inicio_sesion(Correo, Contraseña,data):
    data = {
        Nombre, Apellidos, Edad, Correo, Contraseña
    }
    Correo = str(input('Ingrese su nombre de usuario:'))
    Contraseña = str(input('Ingrese la contraseña de usuario: '))
    
    if Correo and Contraseña in data:
        print("Inicio de sesion verificado")
    else:
        print("Revisa contraseña y vuelve a iniciar")

def crear_usuario(Nombre, Apellidos, Edad, Correo, Contraseña, tarjeta, data):
    data = [
        Nombre, Apellidos, Edad, Correo, Contraseña
    ]
    print('Para crear su usuario de esta pagina llene las siguientes casillas')
    Nombre = str(input('Ingrese su nombre:'))
    Apellidos = str(input('Ingrese su/sus apellidos: '))
    Edad = int(input('Ingrese su edad (Recuerde que para tener acceso a nuestra página debe ser mayor de 14 años): '))
    Correo = str(input('Ingrese un correo electronico valido: '))
    while '@' not in Correo:
        print('A su correo le hace falta "@"')
        Correo = str(input('Ingrese un correo electronico valido: '))
        
    Contraseña = str(input('Ingrese la contraseña:'))
    tarjeta = int(input('Ingrese su numero de tarjeta: '))
    if Edad < 14:
        print('Su edad no es la suficiente para continuar navegenado en nuestra pagina')
    else:        
        print('Cuenta correctamente creada')
        print('Inicie sesiòn')
        inicio_sesion(Correo, Contraseña, data)
        
def pagina_web():
    while True:    
        print('')
        print('-------------------')
        print('Bienvenido a FAndroid')
        print('-------------------')
        print('')
        productos={
            '1' : '"MATRIX"-----15000 COP' ,
            '2' : '"JURASSIC PARK"-----16900 COP',
            '3' : '"TERMINATOR 2"-----13500 COP',
            '4' : '"INTERESTELAR"-----12500 COP',
            '5' : '"VOLVER AL FUTURO"-----15000 COP'
        }
        print('A continuación se indicaran los productos')
    
        print(productos)
        compra=int(print('¿Cual de los produtos desea compar?'))
        
        while compra >= 6:
            compra=int(print('¿Cual de los produtos desea compar?'))
        if compra==1:
            valor=15000
            puntos = 70
            print()
            print(f"Esta a punto de comprar la aplicacion llamada {productos['{compra}']}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
            opcion_elegida=int(input(""))
            if opcion_elegida==1:
                print('Aqui tiene su recibo')
                print ("Este es su recibo, gracias por su compra")
                print("TIENDA APLICACIONES DE FANDROID")
                print("--------------------------------------")
                print(f"cobrado al usuario-----------{Nombre+Apellidos}")
                print(f"tarjeta usada----------------{tarjeta}")
                print(f"aplicacion comprada-----------{productos['{compra}']}cop")
                print(f"puntos sumados a la cuenta-----{puntos}")
                print("--------------------------------------")
                print(f"Valor total cobrado-------------{valor}cop")
                
            elif opcion_elegida==2:
                break
            if compra==2:
                valor=16900
                puntos = 80
                print()
                print(f"Esta a punto de comprar la aplicacion llamada {productos['{compra}']}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    print('Aqui tiene su recibo')
                    print ("Este es su recibo, gracias por su compra")
                    print("TIENDA APLICACIONES DE FANDROID")
                    print("--------------------------------------")
                    print(f"cobrado al usuario-----------{Nombre+Apellidos}")
                    print(f"tarjeta usada----------------{tarjeta}")
                    print(f"aplicacion comprada-----------{productos['{compra}']}cop")
                    print(f"puntos sumados a la cuenta-----{puntos}")
                    print("--------------------------------------")
                    print(f"Valor total cobrado-------------{valor}cop")
                    
                elif opcion_elegida==2:
                    break
            if compra==3:
                valor=13500
                puntos = 50
                print()
                print(f"Esta a punto de comprar la aplicacion llamada {productos['{compra}']}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    print('Aqui tiene su recibo')
                    print ("Este es su recibo, gracias por su compra")
                    print("TIENDA APLICACIONES DE FANDROID")
                    print("--------------------------------------")
                    print(f"cobrado al usuario-----------{Nombre+Apellidos}")
                    print(f"tarjeta usada----------------{tarjeta}")
                    print(f"aplicacion comprada-----------{productos['{compra}']}cop")
                    print(f"puntos sumados a la cuenta-----{puntos}")
                    print("--------------------------------------")
                    print(f"Valor total cobrado-------------{valor}cop")
                    
                elif opcion_elegida==2:
                    break
            if compra==4:
                valor=12500
                puntos = 40
                print()
                print(f"Esta a punto de comprar la aplicacion llamada {productos['{compra}']}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    print('Aqui tiene su recibo')
                    print ("Este es su recibo, gracias por su compra")
                    print("TIENDA APLICACIONES DE FANDROID")
                    print("--------------------------------------")
                    print(f"cobrado al usuario-----------{Nombre+Apellidos}")
                    print(f"tarjeta usada----------------{tarjeta}")
                    print(f"aplicacion comprada-----------{productos['{compra}']}cop")
                    print(f"puntos sumados a la cuenta-----{puntos}")
                    print("--------------------------------------")
                    print(f"Valor total cobrado-------------{valor}cop")
                    
                elif opcion_elegida==2:
                    break
            if compra==5:
                valor=15000
                puntos = 70
                print()
                print(f"Esta a punto de comprar la aplicacion llamada {productos['{compra}']}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    print('Aqui tiene su recibo')
                    print ("Este es su recibo, gracias por su compra")
                    print("TIENDA APLICACIONES DE FANDROID")
                    print("--------------------------------------")
                    print(f"cobrado al usuario-----------{Nombre+Apellidos}")
                    print(f"tarjeta usada----------------{tarjeta}")
                    print(f"aplicacion comprada-----------{productos['{compra}']}cop")
                    print(f"puntos sumados a la cuenta-----{puntos}")
                    print("--------------------------------------")
                    print(f"Valor total cobrado-------------{valor}cop")
                    
                elif opcion_elegida==2:
                    break
    print('Gracias por comprar en esta pagina')

Nombre = str
Apellidos = str
Edad = int
Correo = str
Contraseña = str
tarjeta = int
puntos = int

pregunta_inicio_sesion = str(input('¿Tiene cuenta ya en la pagina? s/n | o si desea salir presione "e":'))
while True:
    if pregunta_inicio_sesion == "s":
        inicio_sesion(Correo, Contraseña, data)
        pagina_web()
    elif pregunta_inicio_sesion == "n":
        crear_usuario(Nombre, Apellidos, Edad, Correo, Contraseña,data)
    elif pregunta_inicio_sesion == "e":
        break
    else:
        print('Opcion incorrecta')