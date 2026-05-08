''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode compra'''

# variavel para receber o valor do dolar a ser comprado na cotação:
dolar = 4.92 # valor de cotação dia 08/05/2026

print('\n|>>>>>>>>>>>>>> Programa Conversor de Moeda <<<<<<<<<<<<<<<<|\n')

din = float(input('Digite o valor que você possue na carteira para cotação: '))
conversao = din / dolar  # faz a divisao do valor em reais para o valor em dolar

print('\n------ Extrato da carteira -------\n')
print(f'>> VALOR ATUAL R$: {din}')
print(f'>>> VALOR OBTIDO EM DOLAR US$: {conversao:.2f}\n')
print('-------------- fim ------------------')
