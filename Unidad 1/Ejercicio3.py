""" Crea una función llamada veriﬁcar_caliﬁcacion que reciba tres parámetros: nota1, nota2 y nota3
    Dentro de la función calcular el promedio de notas
    Si el promedio es mayor o igual a 6, entonces la función debe retornar un mensaje “Aprobado”, en caso contrario “Reprobado”
    
    """


def verificar_calificacion(nota1,nota2,nota3):
    promedio = (nota1+nota2+nota3)/3

    if promedio >= 6:
        cartel = f'APROBADO'

    else:
        cartel = f'REPROBADO'

    return cartel

print (verificar_calificacion(7,8,5))

print (verificar_calificacion(4,8,5))

    