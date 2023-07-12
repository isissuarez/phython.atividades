A = float(input())
B = float(input())
C = float(input())
delta = B**2 - (4*A*C)


if(A == 0 or delta <0):
    print("impossível calcular")
else:
    raiz1 = (-B + (delta**0.5)) / (2*A)
    raiz2 = (-B - (delta**0.5)) / (2*A)
    print("R1 = %0.5f"%raiz1)
    print("R2 = %0.5f"%raiz2)