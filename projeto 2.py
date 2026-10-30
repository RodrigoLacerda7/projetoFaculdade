def lista_produtos():
    produtos = {"arroz": 27.90,
                "feijao": 8.20,
                "açucar": 5.00,
                "suco": 1.50,
                "farinha de trigo": 5.50,
                "sal": 2.00,
                "bolacha recheada": 3.50,
                "leite": 7.00,
                "molho de tomate": 3.20,
                "cafe": 14.00,
                "azeite": 35.00,
                "oleo": 6.00,
                "pao de forma": 12.40 }
    return produtos
produtos = lista_produtos()
total = 0
while True:
    pergunta1 = (input("escreva o nome do produto:"))
    pergunta2 = int(input("digite a quantidade desse produto:"))
    duvida = input("você quer adicionar um outro produto?")
    preco = produtos[pergunta1]
    subtotal = preco*pergunta2
    total = total + subtotal
    print(subtotal)
    if duvida == "nao":
        break
print(total)

