from django.db import models

from . import validators


class EnigmaRotor(models.Model):
    """
    Details about a rotor on the Enigma machine
    """
    # The name of the wheel. Typically, this is a roman numeral.
    name = models.CharField(
        db_index=True, max_length=255)
    # The sequence of letters on the wheel. Should be a string of
    # 26 unique uppercase letters.
    sequence = models.CharField(
        max_length=26,
        validators=[validators.validate_iunique_word,
                    validators.validate_iincludes_only_letters,
                    validators.validate_has_twenty_six_characters])

    class Meta:
        ordering = ['name']
        verbose_name = "rotor"
        verbose_name_plural = "rotors"

    def __str__(self):
        return self.name


class EnigmaRotorNotch(models.Model):
    """ Represents a notch in a rotor wheel. When the wheel hits the notch,
    it signals the next wheel to rotate. Some wheels have multiple notches,
    so this must be represented as a many to one relation.
    """
    rotor = models.ForeignKey(
        to=EnigmaRotor, related_name='notch_set', on_delete=models.CASCADE)
    notch = models.CharField(max_length=1)

    class Meta:
        ordering = ['rotor', 'notch']
        verbose_name = "rotor notch"
        verbose_name_plural = "rotor notches"

    def __str__(self):
        return f'{self.rotor}: {self.notch}'


class EnigmaSetting(models.Model):
    """ Code book setting for a given day """
    date = models.DateField(db_index=True)
    rotors = models.ManyToManyField(
        to=EnigmaRotor, related_name='+', through='EnigmaRotorSetting',
        through_fields=('setting', 'rotor'))
    # plug_set is defined in plug setting
    indicator = models.CharField(max_length=255)
    reflector = models.ForeignKey(
        to=EnigmaRotor, on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['date']
        verbose_name = "setting"
        verbose_name_plural = "settings"

    def __str__(self):
        return f'{self.date}'


class EnigmaRotorSetting(models.Model):
    """ Wheel order of the settings """
    setting = models.ForeignKey(
        EnigmaSetting, on_delete=models.CASCADE)
    rotor = models.ForeignKey(
        EnigmaRotor, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        unique_together = [['setting', 'rotor'], ['setting', 'order']]
        index_together = [['setting', 'order']]
        ordering = ['setting__date', 'order']
        verbose_name = "rotor setting"
        verbose_name_plural = "rotor settings"

    def __str__(self):
        return f'{self.setting.date}/{self.order}: {self.rotor.name}'


class EnigmaPlugSetting(models.Model):
    """ A plug board setting for a given day. """
    setting = models.ForeignKey(
        EnigmaSetting, on_delete=models.CASCADE, related_name='plug_settings_set')
    # A two-letter code indicating character substitutions before passing
    # to the rotors
    substitution = models.CharField(
        max_length=2,
        validators=[validators.validate_iunique_word,
                    validators.validate_iincludes_only_letters,
                    validators.validate_has_two_characters])

    class Meta:
        unique_together=[['setting', 'substitution']]
        index_together=[['setting', 'substitution']]
        ordering = ['setting__date', 'substitution']
        verbose_name = "plug setting"
        verbose_name_plural = "plug settings"

    def __str__(self):
        return f'{self.setting.date}: {self.substitution}'
