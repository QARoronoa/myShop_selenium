from faker import Faker

faker = Faker(locale="Fr_fr")
class AddressData:

    @staticmethod
    def form_address():
        return {
            "adr1" : faker.address(),
            "city" : faker.city(),
            "address_title" : faker.password()
    }