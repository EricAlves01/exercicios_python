''' faça um algoritmo que leia o preço de um produto e mostre  seu novo preço, com 5 % de desconto '''

print('-------------- INICIO --------------------')
p_produto =float(input('digite o preço do produto: ')) # coleta inicial do preço

d = p_produto*0.05 # variavel  desconto para fazer a subtração com o preço do produto
print('-------------- desconto --------------------') # aplicação do desconto
print('**Parabens compra Com desconto ativado !!!**\naplicando desconto....\naplicando desconto....')
print(f'>>Valor Atual com desconto : {p_produto-d:.2f} Reais \n>>Valor Anterior sem desconto: {p_produto} Reais');
