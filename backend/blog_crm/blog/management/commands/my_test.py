import random
import string
import logging

from django.core.management.base import BaseCommand

from blog.models import Policy

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        # for _ in range(10):
            # kw = [
            #     random.choice(string.ascii_lowercase),
            #     random.choice(string.ascii_lowercase),
            #     random.choice(string.ascii_lowercase),
            # ]
            # Policy.objects.create(keywords=kw)
        logger.debug("my test log !!111!!!!111!111!!11!1!1")
        p = Policy.objects.first()
        p.keyword_legacy = ["m", "a", "c"]
        p.save()
