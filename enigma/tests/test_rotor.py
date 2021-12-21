from typing import List

from django import test
from django.core.exceptions import ValidationError

from enigma import validators, models


class RotorTestCase(test.TestCase):

    def test_create(self):
        """ A rotor with a roman numeral for a name and 26 different characters
        should not have any problems """
        rotor = models.EnigmaRotor(
            name="I", sequence="JGDQOXUSCAMIFRVTPNEWKBLZYH")
        rotor.save()

    def test_sequence_validation(self):
        """ A rotor with incorrect characters should not be validated """
        rotor = models.EnigmaRotor(
            name="I", sequence="JGDQOXUSCAMIFRVTPNEWKLZYH")
        try:
            rotor.full_clean()
        except ValidationError as e:
            self.assertTrue(
                'sequence' in e.message_dict,
                f'The sequence should not have validated on '
                f'sequence "{rotor.sequence}".')
