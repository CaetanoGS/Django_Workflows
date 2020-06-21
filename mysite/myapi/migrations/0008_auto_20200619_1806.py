# Generated by Django 3.0.7 on 2020-06-19 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_auto_20200619_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='last_name',
        ),
        migrations.AddField(
            model_name='musician',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musician',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
