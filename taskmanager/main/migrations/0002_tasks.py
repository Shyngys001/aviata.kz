# Generated by Django 3.1 on 2023-04-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=55, verbose_name='Название')),
                ('tasks', models.TextField(verbose_name='Описания')),
            ],
        ),
    ]
