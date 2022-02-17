# Generated by Django 3.1.2 on 2022-02-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField()),
                ('type', models.CharField(choices=[('SLEEP', 'Sport')], max_length=20)),
            ],
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(type__in=['SLEEP']), name='$(app_label)s_event_type_valid'),
        ),
    ]