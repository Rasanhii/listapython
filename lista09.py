numeros = [10,20,30,40,50]

#criando a variavel que irá armazenar o maior numero
maior = numeros[0]

#usando um loop 'for' para percorrer a lista e encontrar o maior numero
for numero in numeros:
    if numero > maior:
        maior = numero

print('o maior numero da minha lista é', maior)