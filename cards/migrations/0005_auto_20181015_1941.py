# Generated by Django 2.1.2 on 2018-10-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20181015_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='number',
            field=models.PositiveIntegerField(null=True, verbose_name='number'),
        ),
        migrations.AddField(
            model_name='card',
            name='subtype',
            field=models.CharField(max_length=255, null=True, verbose_name='subtype'),
        ),
        migrations.AlterField(
            model_name='card',
            name='first_type',
            field=models.CharField(max_length=255, null=True, verbose_name='first type'),
        ),
        migrations.AlterField(
            model_name='card',
            name='rarity',
            field=models.CharField(max_length=255, null=True, verbose_name='rarity'),
        ),
        migrations.AlterField(
            model_name='card',
            name='second_type',
            field=models.CharField(max_length=255, null=True, verbose_name='second type'),
        ),
    ]
