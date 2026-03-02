import math

def calcular_area(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    r = float(input("Introduce el radio del círculo: "))
    area = calcular_area(r)
    print(f"El área del círculo con radio {r} es: {area:.2f}")