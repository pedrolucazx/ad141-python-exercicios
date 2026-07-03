# Exercicio 4
# Leia um arquivo com tres valores por linha (OwnerName ComputerType ComputerValue)
# e crie um dicionario de dicionarios onde as chaves sao os proprietarios
# e os valores sao dicionarios de tipo de computador e valor total.

result = {}

with open("computers.txt") as f:
    for line in f:
        owner, comp_type, value = line.split()
        value = int(value)
        owner_dict = result.get(owner)
        if owner_dict:
            current = owner_dict.get(comp_type)
            if current:
                owner_dict[comp_type] += value
            else:
                owner_dict[comp_type] = value
        else:
            result[owner] = {comp_type: value}

print(result)
