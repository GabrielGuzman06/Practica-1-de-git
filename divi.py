def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

print("=== Programa de División ===")
a = float(input("Ingrese el dividendo: "))
b = float(input("Ingrese el divisor: "))
print("El resultado de la división es:", division(a, b))
