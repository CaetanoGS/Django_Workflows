# Generated by Django 3.0.7 on 2020-06-19 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20200619_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='workFlow_steps',
        ),
        migrations.AddField(
            model_name='step',
            name='steps',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workFlow_steps', to='myapi.WorkFlow'),
        ),
    ]
