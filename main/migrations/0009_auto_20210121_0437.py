# Generated by Django 3.1.5 on 2021-01-21 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210121_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='main.category'),
        ),
    ]
