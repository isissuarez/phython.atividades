Tempo_de_viagem = float(input())
velocidade_media = float(input())
km_por_litro = 12

combustivel_gasto = (Tempo_de_viagem * velocidade_media) / km_por_litro

print("%0.3f" %combustivel_gasto)