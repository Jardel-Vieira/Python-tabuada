print('Digite um número possitivo para que seja feito a tabuada do mesmo: ')
n = int (input())
while(n<0 or n>10):
    print('VALOR INVÁLIDO')
    n = int (input())
for i in range(1,11):
    print(f'{n}x{i}={n*i}')
