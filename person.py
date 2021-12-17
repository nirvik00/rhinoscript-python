class Person(object):
    def __init__(self, x, y):
        self.age = x
        self.name=y
    def increment_age(self):
        self.age+=1