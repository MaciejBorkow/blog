import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

from blog.models import Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        # clean data
        User.objects.all().delete()
        Article.objects.all().delete()

        # Users
        User.objects.create_superuser(username='admin', password='admin')
        users = []
        for i in range(10):
            users.append(User.objects.create_user(fake.name(), fake.email(), 'fakepassword'))

        # Articles
        for i, user in enumerate(users):
            Article.objects.create(
                title=fake.text(15).title(),
                body=fake.text(500),
                author=user,
                background_uri=os.path.join('static/images/', str(i)+'.jpg')
            )
