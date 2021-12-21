# Generated by Django 4.0 on 2021-12-19 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enigma', '0002_alter_enigmaplug_setting'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EnigmaPlug',
            new_name='EnigmaPlugSetting',
        ),
        migrations.RenameModel(
            old_name='EnigmaSettingRotorOrder',
            new_name='EnigmaRotorSetting',
        ),
        migrations.AlterModelOptions(
            name='enigmaplugsetting',
            options={'ordering': ['setting__date', 'substitution'], 'verbose_name': 'plug setting', 'verbose_name_plural': 'plug settings'},
        ),
        migrations.AlterModelOptions(
            name='enigmarotor',
            options={'ordering': ['name'], 'verbose_name': 'rotor', 'verbose_name_plural': 'rotors'},
        ),
        migrations.AlterModelOptions(
            name='enigmarotorsetting',
            options={'ordering': ['setting__date', 'order'], 'verbose_name': 'rotor setting', 'verbose_name_plural': 'rotor settings'},
        ),
        migrations.AlterModelOptions(
            name='enigmasetting',
            options={'ordering': ['date'], 'verbose_name': 'setting', 'verbose_name_plural': 'settings'},
        ),
        migrations.AlterUniqueTogether(
            name='enigmaplugsetting',
            unique_together={('setting', 'substitution')},
        ),
        migrations.AlterIndexTogether(
            name='enigmaplugsetting',
            index_together={('setting', 'substitution')},
        ),
    ]
