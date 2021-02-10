'''
	@autor: Manrick Leal;
	@data: 09/02/2021;
	@nome: Extremamente Básico 1001 URI;
'''
num = float(input())

if (num >= 0.00) and (num <= 25.000):
    print('Intervalo [0,25]')
elif (num > 25.000) and (num <= 50.000):
    print('Intervalo (25,50]')
elif (num > 50.000) and (num <= 75.000):
    print('Intervalo (50,75]')
elif (num > 75.000) and (num <= 100.000):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
