''' Crie um programa que leia um número real pelo teclado e mostre na tela sua parte inteira 

ex: digite um número: 6.127
o número 6.127 tem a parte inteira 6'''

import math 
# from math import ceil
from math import floor

num = float(input('digite um numero: '))

print(f'>> numero digitado: {num}\n>> porção inteira {floor(num)}')