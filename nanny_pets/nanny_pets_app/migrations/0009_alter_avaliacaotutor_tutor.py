# Generated by Django 4.2.3 on 2023-10-31 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nanny_pets_app', '0008_alter_avaliacaocuidador_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacaotutor',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to='nanny_pets_app.tutor'),
        ),
    ]
