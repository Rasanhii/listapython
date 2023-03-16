minha_lista = []
trocado = True
num - int(input('Quantos elementos deseja? '))

for i range(num):
    val = float(input('Entre com o número: '))
    minha_lista.append(val)
    
while trocado:
    trocado = False
    for i in range(len(minha_lista) - 1):
        if minha_lista[i] > minha_lista[i +1]:
            trocado = True
            minha_lista[i], minha_lista[i+1] = minha_lista[i+1], minha_lista[i]

print('\nOrdenando')
print(minha_lista)