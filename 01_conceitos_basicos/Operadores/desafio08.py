''' escreva um programa que leia um valor em metros e exiba convertido em centimentros e milimetros
 -- > (Conversor de Medidas): Converta metros para centímetros (m * 100) e milímetros (m * 1000) '''

print('\n==================| PROGRAMA CONVERSOR DE MEDIDAS [C]entimetros/[M]ilimetros |=======================')
metros = float(input('\n>> digite O valor em Metros:  '))

# conversão de valores: 
Centimetro = metros * 100 
Milimetro  = metros * 1000

print(f'\n >>>>>>>>>> Valores Convertidos: ')
print(f'--> Centimetros: {Centimetro}')
print(f'--> Milimetro : {Milimetro}')

print(f'\n =============================// FIM //=================================')
