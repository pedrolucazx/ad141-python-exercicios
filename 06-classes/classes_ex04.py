#!/usr/bin/env python3
# Exercicio 4
# Implemente a seguinte hierarquia de classes:
#
# Worker: name, salary, years. pension() = years * 10% do salary.
# Manager(Worker): pension() = years * 20% do salary.
# Executive(Manager): pension() = years * 30% do salary.
#
# Implemente um metodo name() na classe Worker como @property
# e tenha isso como metodo padrao para todas as classes derivadas.

from worker import Worker, Manager, Executive


def main():
    w = Worker("John", 50000, 10)
    m = Manager("Alice", 80000, 8)
    e = Executive("Bob", 120000, 5)

    print(w)
    print(m)
    print(e)


if __name__ == "__main__":
    main()