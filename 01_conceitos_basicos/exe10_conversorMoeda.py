''' exercicio: crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
considere o dolar Us$ 1.00 = 5,07'''

print('----------------- inicio ---------------------\n')
dl = 5.07 # valor do dolar no dia 27/05/2026.
# valor atual na carteira: 
vl = float(input('Digite o Valor na sua Carteira: '))# coletar o valor na carteira.


print(f'\n ------------- Conversor --------------')

print(f'\n>> Valor anterior: {vl} Reais')
print(f'>>Valor Atual em dolar: {vl/dl:.2f} US$')