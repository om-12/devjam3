# Generated by Django 3.0.6 on 2020-05-18 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_image_rent_your_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='rent_your_house',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='first.Rentyourhouse'),
            preserve_default=False,
        ),
    ]
