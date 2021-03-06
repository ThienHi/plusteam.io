# Generated by Django 3.1.4 on 2021-01-15 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=None)),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
