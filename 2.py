lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

tam = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)

print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")


def tabuada(num):
    for i in range(0, 11):
        print(num * i)

tabuada(7)


lista1 = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]


def multiplica3(list):
    mult_3 = []
    for i in list:
        mult_3.append(i*3)
    return mult_3

print(multiplica3(lista1))

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

elevado = map(lambda x: x**2, lista2)
print(list(elevado))
