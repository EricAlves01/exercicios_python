''' Operadores Aritméticos :
(+) Adição  e (-) Subtração 
(*) Multiplicação e (/) Divisão = 5/2 = 2,5
(//)Divisão Inteira:  5 / 2 = 2  e (%) modulo ou resto de divisao : 5 / 2 = 1
(**) Exponenciação : 5**2 --> 5*5 '''

print('------ exercicio Operadores Aritméticos --------')
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
print('\n')
print(f'Adição(+): {n1} + {n2} >> {n1+n2}')
print(f'Subtração(-): {n1} - {n2} >> {n1-n2}')
print(f'Multiplicação(*): {n1} * {n2} >> {n1*n2}')
print(f'Divisão(/): {n1} / {n2} >> {n1/n2}')
print(f'Divisão inteira(//): {n1} // {n2} >> {n1//n2}')
print(f'Modulo ou resto (%): {n1} % {n2} >>  {n1%n2}')
print(f'Exponenciação(**): {n1} ** {n2} >>  {n1**n2}')
print('\n------------------------//FIM//----------------------------')