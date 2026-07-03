# Exercicio 2
# Reescreva o exercicio anterior para que, alem da validacao,
# o programa tambem exiba quantos digitos ha no numero,
# caso o valor informado seja um numero inteiro.

luck_number = input("Digite seu numero da sorte: ")
has_sign = luck_number.startswith("+") or luck_number.startswith("-")
is_integer = luck_number.isnumeric() or (has_sign and luck_number[1:].isnumeric())


if not is_integer:
    print("O valor informado não é um número inteiro")
else:
    print("O valor informado é um número inteiro.")
    print(
        f"O número da sorte tem {len(luck_number) - 1 if has_sign else len(luck_number)} dígitos."
    )
