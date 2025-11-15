import random

from faker import Faker
faker = Faker(locale='FR_fr')

class LoginData():

    @staticmethod
    def email_creation_compte():
        return {
            "emailCreation": faker.email()
        }

    @staticmethod
    def formulaire_create_account():
        return {
            "firstName" : faker.first_name(),
            "lastName" : faker.last_name(),
            "pwd": faker.password(),
            "day": random.randint(1,28),
            "month" : random.randint(1,12),
            "year" : faker.year()

        }