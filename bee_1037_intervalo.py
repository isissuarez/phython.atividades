X = float(input())
if (0<= X <= 25):
    print('Intervalo [0,25]')
if (25< X <= 50):
    print('Intervalo (25,50]')
if (50< X <= 75):
    print('Intervalo (50,75]')
if (75< X <= 100):
    print('Intervalo (75,100]')
if (X >100 or X<0):
    print('Fora de intervalo')