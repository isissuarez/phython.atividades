import divisao

A = float(input())
B = float(input())

def velocidade(espaco, tempo):
    v = divisao(espaco, tempo)
    return v

print("Velocidade = %0.1f km/h"%velocidade(A, B))
