# Generated by Django 3.1.3 on 2021-11-26 17:47

from django.db import migrations, connection
import pprint
pp = pprint.PrettyPrinter()


def migrate_array_to_m2m(apps, schema_editor):
    Policy = apps.get_model('blog', 'Policy')
    Keyword = apps.get_model('blog', 'Keyword')
    for policy in Policy.objects.all():
        for keyword in policy.keywords_legacy:
            keyword_obj, _ = Keyword.objects.get_or_create(name=keyword)
            policy.keywords.add(keyword_obj)
        pp.pprint(connection.queries)
    pp.pprint(connection.queries)


def revert_m2m_to_array(apps, schema_editor):
    Policy = apps.get_model('blog', 'Policy')
    for policy in Policy.objects.all():
        keywords = set()
        for keyword in policy.keywords.all():
            keywords.add(keyword.name)
        policy.keywords_legacy = list(keywords)
        policy.save()
        pp.pprint(connection.queries)


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0007_add_many_to_many_keyword_field'),
    ]

    operations = [
        migrations.RunPython(migrate_array_to_m2m, revert_m2m_to_array)
    ]