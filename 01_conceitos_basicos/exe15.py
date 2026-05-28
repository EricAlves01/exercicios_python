''' escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar ,sabendo que o carro  custa 60 reais por dia e r$ 0.15 por km rodado'''

print('------------- Programa Aluguel de Carro ------------------')
#variavel para guardar o valor de km percorridos:
km = float(input('->> digite o valor do Kilometro(km) percorridos:  \n'))
km_cobranca = km*0.15 # variavel para  contificar o valor pelos dias alugados 

# varial para guardar os dias em que o carro foi alugado: 
dias_carro = int(input('->> digite a quantidade de dias em que o carro foi alugado:  \n'))
dias_alugado = dias_carro*60 # variavel para contificar o valor pelos kilometros percorridos 
print('------------- Verificação Valores a Pagar  ------------------')
print(f'o valor total final a pagar é: R$: {km_cobranca+dias_alugado:.2f}\ndias usados: {dias_carro} - Valor: {dias_alugado}\nKilimetros percorridos: {km} km - valor da kilometragem: R$ {km_cobranca}')

print('\n-------------*** Fim do Programa ***------------------')