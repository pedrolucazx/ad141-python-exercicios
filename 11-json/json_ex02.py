#!/usr/bin/env python3

import json


def main():
    word_frequency = {}
    max_count = 0
    max_word = ""
    with open("11-json/cyclone.txt", "r") as data:
        for line in data:
            for word in line.split():
                count = word_frequency.get(word, 0) + 1
                word_frequency[word] = count
                if count > max_count:
                    max_count = count
                    max_word = word

    with open("11-json/frequencies.json", "w") as frequency:
        json.dump(word_frequency, frequency, indent="\t")

    print("'{}' ocorreu {} vez(es)".format(max_word, max_count))


if __name__ == "__main__":
    main()
