# Generated by Django 3.0.6 on 2020-08-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delupdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conno', models.CharField(max_length=15)),
                ('recby', models.CharField(max_length=100)),
                ('deldate', models.CharField(max_length=10)),
            ],
        ),
    ]
