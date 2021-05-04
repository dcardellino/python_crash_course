people = []

dominic = {
    'first_name': 'Dominic',
    'last_name': 'Cardellino',
    'age': 29,
    'city': 'Herrenberg'
}

people.append(dominic)

lisa = {
    'first_name': 'Lisa',
    'last_name': 'Müller',
    'age': 29,
    'city': 'Lodnon'
}

people.append(lisa)

robyn = {
    'first_name': 'Robyn',
    'last_name': 'Maier',
    'age': 27,
    'city': 'Stockholm'
}

people.append(robyn)

for person in people:
    print(f"I know a person, his first name is {person['first_name']}.")
    print(f"I know a person, his last name is {person['last_name']}.")
    print(f"I know a person, his age is {person['age']}.")
    print(f"I know a person, he lives in {person['city']}.")
    print("")