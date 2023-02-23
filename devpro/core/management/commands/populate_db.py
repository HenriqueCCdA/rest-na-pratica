from random import randint, choices
from datetime import datetime

from django.core.management.base import BaseCommand
from django.db import transaction
from devpro.core.models import Author, Book

from faker import Faker

fake = Faker()


START_DATE = datetime(year=1950, month=1, day=1)
END_DATE = datetime(year=2023, month=1, day=1)
MAX_AUTHORS_BOOK = 10


class Command(BaseCommand):
    help = 'Popula o banco de dados'

    def add_arguments(self, parser):
        parser.add_argument('number_of_books', type=int)
        parser.add_argument('number_of_auhtors', type=int)

    def handle(self, *args, **options):

        random_date = fake.date_between(start_date=START_DATE, end_date=END_DATE)

        number_of_books = options['number_of_books']
        number_of_auhtors = options['number_of_auhtors']

        books = [
            Book(
                name=fake.sentence(nb_words=4),
                edition=randint(1, 8),
                publication_year=random_date.year
            )
            for _ in range(number_of_books)
        ]


        authors = [Author(name=fake.name())  for _ in range(number_of_auhtors)]

        with transaction.atomic():
            Book.objects.bulk_create(books)
            Author.objects.bulk_create(authors)

            authors_max_by_book = min(number_of_auhtors, MAX_AUTHORS_BOOK)

            for book in books:
                number_authors_in_book = randint(1, authors_max_by_book)
                list_authores = choices(authors, k = number_authors_in_book)
                book.authors.add(*list_authores)
