# Generated by Django 4.1.3 on 2022-11-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Territorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTerritorio', models.CharField(max_length=10)),
                ('nombre', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]