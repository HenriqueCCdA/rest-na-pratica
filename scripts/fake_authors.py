import csv

from faker import Faker

Faker.seed(1234)
fake = Faker()

with open('authors.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for _ in range(100):
        spamwriter.writerow([fake.name()])
