# Exercicio 6
# Reescreva o Exercicio 4 para contar a frequencia de cada palavra informada pelo usuario.
#
# Use um dict onde:
# - as chaves sao as palavras
# - os valores sao as contagens de ocorrencia
#
# Ao final, imprima os resultados:
# 1) ordenados pelas palavras
# 2) ordenados pelas contagens

words = {}
while True:
    word = input("Digite uma palavra (ou a palavra 'end' para sair) ")
    if word == "end":
        break

    for word in word.split():
        words[word] = words.get(word, 0) + 1

keys_list = list(words.keys())
print("Ordenado pelas palavras:")
for key in sorted(keys_list):
    print(f"{key}: {words[key]}")

print("Ordenado pelas contagens:")
keys_list.sort(key=words.get)
for word in keys_list:
    print(f"{word}: {words[word]}")
