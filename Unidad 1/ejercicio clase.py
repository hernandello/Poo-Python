#Crear un programa que realice una funcion aritmetica que permite al usuario ingresar datos por la terminal acorde a distintas opciones. Para ello debemos definir una funcion que reciba parametros: Combinar funciones nativas, funciones definidas, condicionales y bucles. Si el usuario ingresa el Nro.1 realizar accion A y si ingresa el Nro.2 realizar accion B.



# condicion a = si el nro es decimal lo redondea.
# Condicion b = si el nro es entero muestra un cartel.

nro= float (input("Ingrese un numero:"))

def determinar_entero(nro):
    nro1 = round (nro)
    if (nro1 == nro) :
        cartel= f'{nro} es un numero entero'
    else:
        nro = round (nro)
        cartel =  f'se convirtio tu numero al {nro} entero'
    return cartel

print (determinar_entero(nro))