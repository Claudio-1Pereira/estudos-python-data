lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

soma = [sum(i) for i in lista_de_listas]
print(soma)

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
terceiro_elemento = [lista_de_tuplas[i][2] for i in range(len(lista_de_tuplas))]
print(terceiro_elemento)

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
nome = [(i, lista[i]) for i in range(len(lista))]
print(nome)

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
valor_apar = [aluguel[i][1] for i in range(len(aluguel)) if aluguel[i][0] == 'Apartamento']
print(valor_apar)

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
mes_gasto = {meses[i]: despesa[i] for i in range(len(meses))}
print(mes_gasto)

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
vendas_maior = [venda[1] for venda in vendas if venda[0] == "2022" and venda[1] >= 6000]
print(vendas_maior)

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
gli = [("Hipoglicemia", v) if v <= 70 else ("Normal", v) if v >= 70 and v < 100 else ("Alterada", v) if v <= 125 else ("Diabetes", v) for v in glicemia]
print(gli)

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

tabela =  [('id', 'quantidade', 'preco', 'total')]
tabela += [(id[i], quantidade[i], preco[i], quantidade[i] * preco[i]) for i in range(len(id))]
print(tabela)

estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
estados_unicos = list(set(estados))

lista_de_listas = []
for estado in estados_unicos:
    lista = [uf for uf in estados if uf == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

contagem_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(contagem_valores)