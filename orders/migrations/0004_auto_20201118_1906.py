# Generated by Django 3.1.3 on 2020-11-18 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20201118_1736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в замовленні', 'verbose_name_plural': 'Товари в замовленні'},
        ),
    ]