# Generated by Django 3.0.4 on 2020-11-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20201110_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishinghouse',
            name='phone',
            field=models.CharField(max_length=16),
        ),
    ]
