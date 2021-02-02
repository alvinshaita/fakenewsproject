# Generated by Django 3.1.5 on 2021-01-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canonWord', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryURL', models.URLField(verbose_name='URL of news article')),
            ],
        ),
    ]