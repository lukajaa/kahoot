import csv
import random

people = {}
questions = []
done_people = []

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
for person in people:
    done_people.append(person)
    information = people[person]

    options = []
    while len(options) < 3:
        random_person = random.choice(list(people.keys()))
        if len(done_people) > len(people) - 3:
            options.append(random_person)
        elif random_person not in done_people:
            options.append(random_person)

    random_index = random.randint(0, 3)
    options.insert(random_index, person)

    random_number = random.randint(1, 3)
    if random_number == 1 and information['fav_snack'] != '':
        question = f"This person's favorite asian snack is {information['fav_snack']}."
    elif random_number == 2 and information['fav_celeb'] != '':
        question = f"This person's favorite asian celebrity is {information['fav_celeb']}."
    else:
        if information['funfact_1'] == '':
            question = f"No fun facts."
        elif information['funfact_2'] == '':
            question = f"Fun Fact #1: {information['funfact_1']}."
        elif information['funfact_3'] == '':
            question = f"Fun Fact #1: {information['funfact_1']}. Fun Fact #2: {information['funfact_2']}."
            if len(question) > 95:
                question = f"Fun Fact #1: {information['funfact_1']}."
        else:
            question = f"Fun Fact #1: {information['funfact_1']}. Fun Fact #2: {information['funfact_2']}. Fun Fact #3: {information['funfact_3']}."
            if len(question) > 95:
                question = f"Fun Fact #1: {information['funfact_1']}. Fun Fact #2: {information['funfact_2']}."
                if len(question) > 95:
                    question = f"Fun Fact #1: {information['funfact_1']}."
                
    options.insert(0, question)
    options.append(20)
    options.append(random_index + 1)
    questions.append(options)

questions.append([
    "Which ASU leader's favorite artist is keshi?",
    "Sophia",
    "Lucas",
    "Gracie",
    "Valerie",
    20,
    1
])
questions.append([
    "Which ASU leader's favorite food is mandu-guk?",
    "Sophia",
    "Gracie",
    "Lucas",
    "Valerie",
    20,
    3
])
questions.append([
    "Which ASU leader's favorite artist is Laufey?",
    "Valerie",
    "Lucas",
    "Gracie",
    "Sophie",
    20,
    1
])
questions.append([
    "Which ASU leader's favorite food is pad krakow?",
    "Sophia",
    "Lucas",
    "Gracie",
    "Valerie",
    20,
    3
])

with open('questions.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for question in questions:
        writer.writerow(question)