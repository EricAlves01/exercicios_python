''' Faça um Programa que leia a largura e a altura de uma parede em metros , calcule sua área e a quantidade de tinta
necessária para pintá-la , sabendo que cada litro de tinta , pinta uma area de 2m²'''

largura = float(input('digite a largura: '))
altura = float(input('digite a altura: '))

area = largura*altura

print(f' sua parede possui a dimensão de {largura} X {altura} e sua aréa de {area} 2M²')

tinta = area/2

print(f' a quantidade de litros de tinta da area: {area} é >> {tinta} litros por metros')