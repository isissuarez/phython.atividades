N = int(input())
print(f"{N}")

N100 = N//100
N = N%100

N50 = N//50
N = N%50

N20 = N//20
N = N%20

N10 = N//10
N = N%10

N5 = N//5
N = N%5

N2 = N//2
N = N%2

print(f"{N100} nota(s) de R$ 100,00")
print(f"{N50} nota(s) de R$ 50,00")
print(f"{N20} nota(s) de R$ 20,00")
print(f"{N10} nota(s) de R$ 10,00")
print(f"{N5} nota(s) de R$ 5,00")
print(f"{N2} nota(s) de R$ 2,00")
print(f"{N} nota(s) de R$ 1,00")