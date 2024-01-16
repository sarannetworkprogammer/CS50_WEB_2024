"""
lambda functions

square = lambda x: x*x
"""

people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"cho","house":"Ravenclaw" },
    {"name":"Draco", "house":"Slytherin"}
]




print(people)


def f(person):
    return person["name"]

people.sort(key=f)

print(people)