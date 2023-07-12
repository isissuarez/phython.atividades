notas = input().split()
n1,n2,n3,n4 = notas

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10
print("Media: %.1f"%media)

if media >= 7.0:
    print("Aluno aprovado.")
if media < 5.0:
    print("Aluno reprovado.")
if 5.0 <= media < 7.0:
    print("aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame}")
    media_final = (media + nota_exame) / 2
    if media_final > 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f"%media_final)
    if media_final <= 5.0:
        print("Aluno reprovado.")
        print("Media final: %.1f"%media_final)