vendedor = input()
salario_fixo = float( input())
vendas = float( input())

valor_a_receber = salario_fixo + (vendas * 0.15)

print('TOTAL = R$ %.2f'%valor_a_receber)