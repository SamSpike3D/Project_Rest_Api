# Generated by Django 4.2.3 on 2023-07-15 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('tecnologia', models.CharField(max_length=200)),
                ('fechacrt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
