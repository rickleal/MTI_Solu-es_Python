'''
	@autor: Manrick Leal;
	@data: 09/02/2021;
	@nome: Extremamente Básico 1001 URI;
''' 
primeiro = 0
segundo = 1
fibo = [primeiro, segundo]
for i in range(2,46):
    aux = segundo + primeiro
    primeiro = segundo
    segundo = aux
    fibo.append(aux)
entrada = int(input())
for i in range(0, entrada):
    if i == entrada-1:
        print('{}'.format(fibo[i]))
    else:
        print('{}'.format(fibo[i]), end= ' ')
