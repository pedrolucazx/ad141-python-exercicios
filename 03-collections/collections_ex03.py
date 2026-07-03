# Exercicio 3
# Escreva um programa que fique em loop pedindo para o usuario inserir um numero.
# Repita ate o usuario digitar a palavra "end".
#
# Armazene os numeros em um set.
# Antes de inserir cada numero, verifique se ele ja existe no set.
# Se ja existir, atualize um contador que registra quantos elementos nao foram adicionados.
#
# Antes do programa encerrar, imprima:
# 1) o conteudo do set em uma linha
# 2) a quantidade de elementos NAO adicionados na linha seguinte

numbers = set()
amount = 0

while True:
    data = input("Digite um numero (ou a palavra 'end' para sair) ")
    if data == "end":
        break
    if not data.isdigit():
        print("Entrada invalida. Digite um numero ou 'end'.")
        continue

    if int(data) not in numbers:
        numbers.add(int(data))
    else:
        amount += 1

print(numbers)
print(amount)
