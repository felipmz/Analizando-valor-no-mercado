soma = cont = cont2 = 0
barato = ''
lista = []
while True:
    nome = str(input ('qual o nome do produto: '))
    preco = int(input('qual o preço: '))
    quercon = str(input('quer continuar ?[S/N] ')).upper()[0]
    print (f'-=-'*17)
    cont2 += 1

    # soma
    soma += preco
    # se custa mais de 1000
    if preco > 1000 :
        cont += 1
    #menor valor
    lista += [preco]
    v = min(lista)
    #nome do produto mais barato
    if cont2 == 1:
        barato = nome
        p = v
    else :
        if preco < p:
            barato = nome

    if quercon == 'N':
        print (f'A soma dos valores das compras é {soma}')
        print (f'Tem mais de {cont} produtos que custam mais de 1000R$')
        print (f'O pruduto mais barato é {barato} e custa {v}')
        break
