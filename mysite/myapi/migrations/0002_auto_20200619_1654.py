# Generated by Django 3.0.7 on 2020-06-19 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='steps',
        ),
        migrations.AddField(
            model_name='step',
            name='workFlow_steps',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='myapi.WorkFlow'),
        ),
    ]
