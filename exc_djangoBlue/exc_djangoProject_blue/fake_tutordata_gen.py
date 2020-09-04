import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exc_djangoProject_blue.settings")

import django
django.setup()

from random import choice
from djangoApp1.models import Tutor
from faker import Faker

fake_object = Faker()

list_of_major = ["Machine Learning", "Front-end web development", "Back-end web development", "Full-stack web development", "Data science", "Robotics", "Augmented reality", "Data visualization"]

def generate_data(numOfEntry=10):
    for _ in range(numOfEntry):
        fake_firstname = fake_object.first_name()
        fake_lastname = fake_object.last_name()
        fake_email = fake_object.email()
        fake_teachfield = choice(list_of_major)

        fake_tutor = Tutor.objects.get_or_create(tutor_firstname=fake_firstname, tutor_lastname=fake_lastname, tutor_email=fake_email, tutor_teach_field=fake_teachfield)

if __name__ == "__main__":
    print("Generating fake data. . .")
    generate_data(20)
    print("Fake data successfully generated.")