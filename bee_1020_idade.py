N = int(input())

anos = N // 365
N = N%365
meses = N//30
dias = N%30

print(f"""{anos} ano(s)
{meses} mes(es)
{dias} dia(s)""")
