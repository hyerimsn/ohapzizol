# Generated by Django 3.0.6 on 2020-06-02 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_auto_20200601_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='beerimage',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
