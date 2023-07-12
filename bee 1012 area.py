A = float(input())
B = float(input())
C = float(input())
Pi = 3.14159

Area_triangulo = (A * C) / 2
Area_circulo = Pi * C ** 2
Area_trapezio = ((A + B) * C) / 2 
Area_quadrado = B ** 2
Area_retangulo = A * B

print("TRIANGULO: %0.3f" %Area_triangulo)
print("CIRCULO: %0.3f" %Area_circulo)
print("TRAPEZIO: %0.3f" %Area_trapezio)
print("QUADRADO: %0.3f" %Area_quadrado)
print("RETANGULO: %0.3f" %Area_retangulo)