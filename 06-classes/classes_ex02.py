#!/usr/bin/env python3
# Exercicio 2
# Crie uma classe chamada Family.
#
# Family nao estende Person, mas deve ser composta por dois objetos Person
# representando os pais e uma lista de objetos Person representando os filhos.
#
# O metodo __init__() deve receber dois parametros obrigatorios (os pais),
# seguidos por um numero variavel de argumentos (os filhos).

from person import Person
from family import Family


def main():
    mother = Person("Mom", 45, "F")
    father = Person("Dad", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")
    myFamily = Family(mother, father, kid1, kid2)
    kid3 = Person("Paulie", 1, "M")
    myFamily.add(kid3)
    print(myFamily)


if __name__ == "__main__":
    main()