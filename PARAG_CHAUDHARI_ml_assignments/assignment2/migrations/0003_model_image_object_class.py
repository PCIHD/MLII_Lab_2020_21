# Generated by Django 3.0.3 on 2020-09-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2', '0002_auto_20200901_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_image',
            name='object_class',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
