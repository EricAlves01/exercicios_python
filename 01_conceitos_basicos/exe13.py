''' exercicio reajuste salarial: faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento '''

print('------------------------ PDI aumento Salárial ------------------------------\n')
func = str(input('digite o nome do funcionario: ')) # variavel nome - somente para personalizar
salario =float(input('Digite seu salario: ')) # variavel para guardar o valor do salario.

aumento = salario*0.15 # variavel que multiplica o valor do salario pelos 15% 

print(f'\ncarregando pdi salaria .....\nfinalizando ........\n>>>funcionario: {func} - Novo Salário com aumento de 15% : {salario+aumento} Reais \n-------------------------fim pdi -------------------')
