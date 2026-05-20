# aula 06 : crie um algoritmo que leia um número e mostre o seu dobro , triplo e raiz quadrada: 

n = int(input('digite um numero: '))

d = n * 2  # dobro
t = n * 3   # triplo
rq = n **(1/2) # raiz quadrada 

print(f"O dobro de {n} é {d}")
print(f"O triplo de {n} é {t}")
print(f"A raiz quadrada de {n} é {rq:.2f}")