# Generated by Django 2.1.2 on 2018-10-15 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_auto_20181015_1941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ('collection', 'number'), 'verbose_name': 'card', 'verbose_name_plural': 'cards'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ('id',), 'verbose_name': 'collection', 'verbose_name_plural': 'collections'},
        ),
    ]
