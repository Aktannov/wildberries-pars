# Generated by Django 4.0.5 on 2022-06-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='articul',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='brend',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Brend',
        ),
    ]
