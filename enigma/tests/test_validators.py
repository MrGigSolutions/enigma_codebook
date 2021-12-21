from typing import List

from django import test
from django.core.exceptions import ValidationError

from enigma import validators


class ValidatorsTestCase(test.TestCase):

    def test_validate_iunique_word(self):
        """ All characters in a word are unique. """

        # These sequences are all valid and should raise no errors
        valid_sequences = ["abc", "ABC", "abCdEZ17", None]
        for v in valid_sequences:
            try:
                validators.validate_iunique_word(v)
            except ValidationError:
                self.fail(f'Word "{v}" contained only unique characters, '
                          f'but caused a validation error.')

        # These are the sequences that should raise validation errors
        invalid_sequences = ["AA", "aA"]
        for i in invalid_sequences:
            with self.assertRaises(ValidationError):
                validators.validate_iunique_word(i)

    def test_validate_iincludes_only_letters(self):
        """ Word contains only letters of the alphabet. """

        # These sequences are all valid and should raise no errors
        valid_sequences = ["abc", "ABC", None]
        for v in valid_sequences:
            try:
                validators.validate_iincludes_only_letters(v)
            except ValidationError:
                self.fail(f'Word "{v}" contained only letters, '
                          f'but caused a validation error.')

        # These are the sequences that should raise validation errors
        invalid_sequences = ["A1", "#"]
        for i in invalid_sequences:
            with self.assertRaises(ValidationError):
                validators.validate_iincludes_only_letters(i)

    def test_include_twentysix_characters(self):
        """ Word consists exactly of 26 characters """

        # These should all pass muster
        valid_sequences = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                           "abcdefghijklmnopqrstuvwxyz",
                           "aaaaaaaaaaaaaaaaaaaaaaaaaa",
                           "$#^##$$#&&^*&^$%#GEA4535y4"]
        for v in valid_sequences:
            try:
                validators.validate_has_twenty_six_characters(v)
            except ValidationError:
                self.fail(f'Word "{v}" contained 26 characters, '
                          f'but caused a validation error.')

        # These are the sequences that should raise validation errors
        invalid_sequences = [None, "a", "", "abcdefghijklmnopqrstuvwxyz!",
                             "abcdefghijklmnopqrstuvwxy"]
        for i in invalid_sequences:
            with self.assertRaises(ValidationError):
                validators.validate_has_twenty_six_characters(i)

    def test_include_two_characters(self):
        """ Word consists exactly of 2 characters """

        # These should all pass muster
        valid_sequences = ["AB",
                           "ac",
                           "aa",
                           "$^"]
        for v in valid_sequences:
            try:
                validators.validate_has_two_characters(v)
            except ValidationError:
                self.fail(f'Word "{v}" contained 2 characters, '
                          f'but caused a validation error.')

        # These are the sequences that should raise validation errors
        invalid_sequences = [None, "a", "", "abc"]
        for i in invalid_sequences:
            with self.assertRaises(ValidationError):
                validators.validate_has_two_characters(i)
