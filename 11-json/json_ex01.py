#!/usr/bin/env python3

import json


def print_data(book, data):
    print(f"{book}:")
    for k, v in data.items():
        print(f"{k:>10}: {v}")


def main():
    with open("11-json/books.json", "r") as data:
        books = json.load(data)

    while True:
        book_to_find = input("Digite o titulo de um livro (q para sair): ")
        if book_to_find.lower() == "q":
            print("Adeus")
            break

        book = books.get(book_to_find)
        if book:
            print_data(book_to_find, book)
        else:
            print(book_to_find, "nao foi encontrado")


if __name__ == "__main__":
    main()
