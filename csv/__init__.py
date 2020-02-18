import csv

class Person():
    def __init__(self, first_name='', last_name='', age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return "First Name: %s\nLast Name: %s\nAge: %s" % (self.first_name, self.last_name, self.age)


csv_path = './recipes.csv'

recipes = []


with open(csv_path, 'r') as csv_file:
    rows = csv.reader(csv_file), delimiter=|
    for row in rows:
        recipes.append(Person(first_name=row[0], last_name=row[1], age=row[2]))


for person in recipes:
    print(person)
