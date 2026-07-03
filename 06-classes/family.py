#!/usr/bin/env python3
from person import Person


class Family:

    def __init__(self, parent1, parent2, *children):
        self.parent1 = parent1
        self.parent2 = parent2
        self.children = list(children)

    def add(self, child):
        self.children.append(child)

    def __str__(self):
        members = [str(self.parent1), str(self.parent2)]
        members.extend(str(c) for c in self.children)
        return "\n".join(members)

    def __lt__(self, other):
        return len(self.children) < len(other.children)

    def __eq__(self, other):
        return len(self.children) == len(other.children)

    def __gt__(self, other):
        return len(self.children) > len(other.children)