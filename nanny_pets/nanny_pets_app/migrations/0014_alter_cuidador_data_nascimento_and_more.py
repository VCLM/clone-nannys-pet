# Generated by Django 5.0 on 2023-12-22 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanny_pets_app', '0013_remove_cuidador_caracteristicas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuidador',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='plataformaIndicação',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
