# Generated by Django 3.2.4 on 2021-06-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=200)),
                ('circuito', models.CharField(max_length=200)),
                ('vueltas', models.IntegerField(default=0)),
                ('len_circuito', models.FloatField()),
            ],
        ),
    ]