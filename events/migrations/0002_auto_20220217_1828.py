# Generated by Django 3.2.5 on 2022-02-17 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.activity'),
        ),
        migrations.AlterField(
            model_name='event',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.food'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sleep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.sleep'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.sport'),
        ),
        migrations.AlterField(
            model_name='event',
            name='symptom_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.symptomgroup'),
        ),
    ]