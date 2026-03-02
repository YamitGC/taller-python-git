import math

def calcular_area(radio):
    return math.pi * radio**2

def calcular_perimetro(radio):
    return 2 * math.pi * radio


if __name__ == "__main__":
    r = float(input("Introduce el radio del círculo: "))
    area = calcular_area(r)
    perimetro = calcular_perimetro(r)
    print(f"El perimetro del círculo con radio {r} es: {perimetro} ")
    print(f"El área del círculo con radio {r} es: {area:.2f}")