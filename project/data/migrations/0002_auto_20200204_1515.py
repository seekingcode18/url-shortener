# Generated by Django 3.0.2 on 2020-02-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='short_url',
            field=models.CharField(default='fgchh', max_length=5),
        ),
    ]
