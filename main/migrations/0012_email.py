# Generated by Django 3.1.5 on 2021-04-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210121_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'emails',
                'ordering': ['-id'],
            },
        ),
    ]