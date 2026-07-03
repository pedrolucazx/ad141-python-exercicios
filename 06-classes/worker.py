#!/usr/bin/env python3
class Worker:

    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def years(self):
        return self._years

    @years.setter
    def years(self, years):
        self._years = years

    def pension(self):
        return self.years * (self.salary * 0.10)

    def __str__(self):
        return f"{self.name}: pension={self.pension()}"


class Manager(Worker):

    def pension(self):
        return self.years * (self.salary * 0.20)


class Executive(Manager):

    def pension(self):
        return self.years * (self.salary * 0.30)