# -*- coding: utf-8 -*-
__author__ = "LY"


class A():
    name = 'adsd'
    age = 12

    def __init__(self):
        self.name = 'aaaa'
        self.age = 14

    def say(self):
        print(self.name)
        print(self.age)


a = A()
a.say()
A.say(A)
