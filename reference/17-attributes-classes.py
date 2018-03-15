class Education:
    def __init__(self, year_from, year_to, level):
        self.years = range(year_from, year_to + 1)
        self.level = level

class Person:
    '''Represents a person'''

    def __init__(self, name, age, education):
        self.name = name
        self.age = age
        self.education = education

e = Education(1990, 1995, 'high')
p = Person('John', 30, e)

print(p.education.years)