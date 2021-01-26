# Generated by Django 3.1.5 on 2021-01-24 13:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'question_hire',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=500)),
                ('vote', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hire.question')),
            ],
            options={
                'db_table': 'choice_hire',
                'ordering': ['-id'],
            },
        ),
    ]