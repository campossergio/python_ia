#IN está contido
x = 2 in(1, 2, 3, 4, 5)

print(x)

#no range o último número não entra na lista
y = 6 in range(1, 7)

print(y)

#valor inicial 2, valor final 11, pular de 2 em 2
z = 2 in range(2, 11, 2)

print(z)

xx = (2 or 10) in (1, 2, 3, 4, 5)
print(xx)

yy = (2 and 10) in range(1, 10)
print(yy)

