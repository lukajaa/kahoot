import csv

people = {}

with open('data.csv', newline='', encoding='utf-8') as f:
    data = csv.reader(f)
    for row in data:
        if row[0] == 'Timestamp':
            continue
        name = row[1].split(' ')[0].capitalize()
        funfact_1 = row[2]
        funfact_2 = row[3]
        funfact_3 = row[4]
        fav_snack = row[5]
        fav_celeb = row[6]
        people[name] = {
            'funfact_1': funfact_1,
            'funfact_2': funfact_2,
            'funfact_3': funfact_3,
            'fav_snack': fav_snack,
            'fav_celeb': fav_celeb,
        }

print(people['Jeslyn'])