import time
import random

from faker import Faker

LOCALE_TO_COUNTRY = {
    "en_US": "United States",
    "de_DE": "Germany",
    "fr_FR": "France",
    "ru_RU": "Russia",
}




def get_random_email(prefix: str = 'user', delimiter: str = '.') -> str:
    return f'{prefix}{delimiter}{time.time()}@mail.com'


class Fake:
    def __init__(self, faker: Faker, seed: int = None):
        self.faker = faker
        if seed is not None:
            self.faker.seed_instance(seed)


    def uuid(self)->str:
        return self.faker.uuid4()

    def email(self) -> str:
        return self.faker.email()

    def password(self) ->str:
        return self.faker.password()

    def sentence(self) -> str:
        return self.faker.sentence()

    def text(self)->str:
        return self.faker.text()

    def name(self) -> str:
        return f'{self.first_name()} {self.last_name()}'

    def first_name(self):
        return self.faker.first_name()

    def middle_name(self):
        return self.faker.middle_name()

    def last_name(self) ->str:
        return self.faker.last_name()

    def title(self) -> str:
        return random.choice(['Mr', 'Mrs'])

    def birth_day(self) ->str:
        return self.faker.day_of_month()

    def birth_month(self) ->str:
        return self.faker.month()

    def birth_year(self) ->str:
        return str(self.faker.random_int(min=1950, max=2000))

    def company(self) ->str:
        return self.faker.company()

    def address_1(self) ->str:
        return self.faker.address()

    def address_2(self) ->str:
        return self.faker.secondary_address()

    def country(self) ->str:
        return self.faker.country()

    def zipcode(self) ->str:
        return self.faker.zipcode()

    def state(self) ->str:
        return self.faker.state()

    def city(self) ->str:
        return self.faker.city()

    def mobile_number(self) ->str:
        return self.faker.phone_number()


class ProfileBuilder:
    def __init__(self, fake: Fake):
        self.fake = fake
        self.faker = fake.faker
        self.locale = self.faker.locales[0]
        self.country = LOCALE_TO_COUNTRY.get(self.locale, "United States")

    @staticmethod
    def gender() ->str:
        return random.choice(['male', 'female'])

    @staticmethod
    def random_gender_and_title() -> tuple[str, str]:
        gender = ProfileBuilder.gender()
        title = 'Mr' if gender == 'male' else 'Mrs'
        return gender, title

    def contextual_email(self, first_name: str, last_name: str) -> str:
        username = f"{first_name.lower()}.{last_name.lower()}"
        domain = self.faker.free_email_domain()
        return f"{username}@{domain}"

    def contextual_address(self) -> dict:
        return {
            "address1": self.faker.street_address(),
            "address2": self.faker.secondary_address(),
            "city": self.faker.city(),
            "state": self.faker.state(),
            "zipcode": self.faker.zipcode(),
            "country": self.country
        }

    def person_profile(self) -> dict:
        profile = self.faker.profile(fields=['name', 'sex', 'mail'])

        gender = 'male' if profile['sex'] == 'M' else 'female'
        title  = 'Mr' if gender == 'male' else 'Mrs'

        parts = profile["name"].split(" ", 1)
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else ""

        email = self.contextual_email(first_name, last_name)
        address = self.contextual_address()

        return {
            "gender": gender,
            "title": title,
            "first_name": first_name,
            "last_name": last_name,
            "name": profile['name'],
            "email": email,
            "phone": self.fake.mobile_number(),
            "birth_year": self.fake.birth_year(),
            "birth_month": self.fake.birth_month(),
            "birth_day": self.fake.birth_day(),
            "company": self.fake.company(),
            "address1": address["address1"],
            "address2": address["address2"],
            "city": address["city"],
            "state": address["state"],
            "zipcode": address["zipcode"],
            "country": address["country"]
        }

# class FakeFactory:
#     # def __init__(self, locale: str = "en_US", seed: int | None = None):
#     #     self.fake = Fake(locale=locale, seed=seed)
#     #     self.builder = ProfileBuilder(self.fake)
#
#     def __init__(self, faker: Faker, seed: int | None = None):
#         self.fake = Fake(faker=faker, seed=seed)
#         self.builder = ProfileBuilder(self.fake)
#
#     def generate_profile(self) -> dict:
#         return self.builder.person_profile()
#
#     def generate_email(self) -> str:
#         return self.fake.email()
#
#     def generate_password(self) -> str:
#         return self.fake.password()
#
#     def generate_uuid(self) -> str:
#         return self.fake.uuid()
#
#     def get_fake_object(self) -> Fake:
#         return self.fake


    
# fake = Fake(faker=Faker("en_US"))
# profile = ProfileBuilder(fake)

# factory = FakeFactory(faker=Faker("en_US"))
# profile = factory.generate_profile()
# fake = factory.get_fake_object()

fake = Fake(faker=Faker("en_US"))
fake_builder = ProfileBuilder(fake)
