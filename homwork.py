# ejemplos de ejercicios de Python que involucran el uso de 
# las estructuras de control  if  y  else :
 
#1. Verificar si un número es positivo, negativo o cero:
 
# Verificar si un número es positivo, negativo o cero
num = float(input("Ingrese un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
 
 
#2. Determinar si un número es par o impar:
 
# Determinar si un número es par o impar
num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
 
 
#3. Calcular el máximo de tres números:
 
# Calcular el máximo de tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

maximo = max(num1, num2, num3)
print("El máximo de los tres números es:", maximo)
 
 
#4. Determinar si un año es bisiesto o no:
 
# Determinar si un año es bisiesto o no
anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
 
 
