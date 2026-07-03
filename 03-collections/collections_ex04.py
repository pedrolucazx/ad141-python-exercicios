# Exercicio 4
# Use um unico set para determinar a quantidade de palavras unicas na entrada do usuario.
#
# Voce pode usar o mesmo modelo de loop com while True e saida com "end".
# Em cada iteracao, adicione as palavras individuais no mesmo set.
# Ao terminar o loop, imprima:
# 1) o conteudo do set ordenado em ordem alfabetica
# 2) a quantidade total de palavras unicas

words = set()

while True:
    word = input("Digite uma palavra (ou a palavra 'end' para sair) ")
    if word == "end":
        break
    words.update(word.split())

for word in sorted(words):
    print(word)

print(len(words))
