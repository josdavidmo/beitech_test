# Generated by Django 2.1.2 on 2018-10-06 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
