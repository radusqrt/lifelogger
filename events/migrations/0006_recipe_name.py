# Generated by Django 3.1.2 on 2022-02-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20220217_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='N/A', max_length=20),
            preserve_default=False,
        ),
    ]
