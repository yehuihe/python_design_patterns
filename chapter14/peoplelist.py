from faker import Faker
faker = Faker()


def populate():

    persons = []
    for _ in range(0, 20):
        p = {'firstname': faker.first_name(), 'lastname': faker.last_name()}
        persons.append(p)

    return iter(persons)


if __name__ == '__main__':
    new_persons = populate()

    new_data = [f"{p['firstname']} {p['lastname']}" for p in new_persons]
    new_data = ", ".join(new_data) + ", "

    with open('people.txt', 'a') as f:
        f.write(new_data)
