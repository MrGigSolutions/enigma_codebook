# Generated by Django 4.0 on 2021-12-20 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enigma', '0005_enigmasetting_indicator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enigmasetting',
            name='reflector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='enigma.enigmarotor'),
        ),
    ]