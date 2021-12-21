from typing import List

from django import test
from django.core.exceptions import ValidationError
from django.utils import timezone

from enigma import validators, models


class PlugTestCase(test.TestCase):

    def setUp(self) -> None:
        self.setting = models.EnigmaSetting(date=timezone.now().date())
        self.setting.save()

    def test_create(self):
        """ A plug with 2 characters as substitutions should be ok """
        plug = models.EnigmaPlugSetting(setting=self.setting, substitution="AE")
        plug.save()

    def test_sequence_validation(self):
        """ A rotor with incorrect characters should not be validated """
        plug = models.EnigmaPlugSetting(setting=self.setting, substitution="ABC")
        try:
            plug.full_clean()
        except ValidationError as e:
            self.assertTrue(
                'substitution' in e.message_dict,
                f'The substitution should not have validated on '
                f'plug "{plug.substitution}".')
