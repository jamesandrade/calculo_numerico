
##### Metodo de Euler para resolução P.V.I  (10.1)                ######
#####     {    y' = -y + x + 2                                    ######
#####     {    y(0) = 2, x E [0 , 0.3],      h = 0.1              ######
#####

h = 0.1   #passo

# y(0) = 2
xzero = 0      
yzero = 2

# x E [0 , 0.3]
xprocuray = 0.3

# inicia x e y com x0 e y0
x = xzero
y = yzero

indice = 0 #indice de x e y

# esse loop será repetido até que encontre valor de y para x = 0.3
while(x <= xprocuray):
     yeuler = (2.71828 ** (-x)) + x + 1 # e^-x + x + 1
     print(f'x[{indice}] = {x:.1f} | y[{indice}] = {y:.4f} | y(x[{indice}]) = {yeuler:.5f}')
     
     fo = -y + x + 2
     foo =  y - x - 1
     fooo = -y + x + 1
     y = y + h * fo + ((h ** 2) /  2) * foo + ((h ** 3) / (3*2*1)) * fooo
     
     x = x + h    
     indice = indice + 1

#aqui o valor de y para x = 0.3 foi encontrado, então esta fora do loop:
yeuler = (2.71828 **(-x)) + x + 1
print(f'x[{indice}] = {x:.1f} | y[{indice}] = {y:.4f} | y(x[{indice}]) = {yeuler:.5f}')




