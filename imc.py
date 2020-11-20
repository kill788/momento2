nombre = input('¿Cuál es tu nombre?: ')
estatura = input('¿Cuál es tu estatura(Cm)?: ')
peso = input('¿Cuál es tu peso(Kg)?: ')

def calcularImc(nombre, estatura, peso):
    metros = float(estatura) / 100
    totalPeso = float(peso) / (pow(float(metros), 2))
    if(totalPeso < 18.5):
        return print(f'Hola {nombre}, tu indice de masa corporal es {totalPeso}, estas bajo de peso.')
    elif(totalPeso > 18.5 and totalPeso < 24.9):
        return print(f'Hola {nombre}, tu indice de masa corporal es {totalPeso}, estas en una condición normal.')
    elif(totalPeso > 25.0 and totalPeso < 29.9):
        return print(f'Hola {nombre}, tu indice de masa corporal es {totalPeso}, estas en sobrepeso.')
    elif(totalPeso > 30):
        return print(f'Hola {nombre}, tu indice de masa corporal es {totalPeso}, estas en una condición de obesidad.')
    else: 
        return print('Ingresa un valor correcto.')

calcularImc(nombre, estatura, peso)