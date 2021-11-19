def main(recebendo_dois_valores, somando_dois_valores,exibindo_mensagem):
    exibindo_mensagem(somando_dois_valores(recebendo_dois_valores))

def exibindo_mensagem(somando_dois_valores):
    print(f"A soma desses dois valores é = {somando_dois_valores}")

def recebendo_dois_valores():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    return a, b

def somando_dois_valores(recebendo_dois_valores):
    valores = recebendo_dois_valores()
    print(f"Somando {valores[0]} + {valores[1]}")
    return valores[0] + valores[1]

main(recebendo_dois_valores, somando_dois_valores, exibindo_mensagem)
