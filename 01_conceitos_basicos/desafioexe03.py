# DESAFIO 004 DO EXE03 : FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVEIS SOBRE ELE:


print('----Digite o Tipo -----')
n = (input('digite algo: '))

print(f"O tipo primitivo do valor é: {type(n)}\n\n ---> Informações : \n")

print(f'a variavel é numerica : {n.isnumeric()}')
print(f' a variavel é alfabetica: {n.isalpha()}')
print(f'a variavel é um alfanumerico: {n.isalnum()}')
print(f'a  variavel é um decimal:{n.isdecimal()}')
print(f' A veriavel é um digito : {n.isdigit()}')
print(f'A variavel é um espaço: {n.isspace()}')