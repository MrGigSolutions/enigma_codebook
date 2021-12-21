import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_iunique_word(word: str):
    """ Checks that sequence consists of case independent unique values. """
    if word is None:
        return

    character_set = set(character.upper() for character in word)

    if len(character_set) != len(word):
        raise ValidationError(
            _('%(word)s contains duplicate characters.'),
            params={'word': word}
        )


def validate_iincludes_only_letters(word: str):
    """ Checks that the sequence contains only letters of the alphabet. """
    # Special case: empty string
    if word is None:
        return

    letter_only_expression = re.compile(r'^[a-zA-Z]*$')

    if letter_only_expression.match(word) is None:
        raise ValidationError(
            _('%(word)s contains illegal characters.'),
            params={'word': word}
        )


def _validate_has_character_count(word: str, num: int):
    """ Checks that the word contains num characters """
    if word is None and num == 0:
        return

    if word is None and num != 0:
        raise ValidationError(
            _('%(word)s is None, so cannot contain %(num)d characters.'),
            params={'word': word, 'num': num})

    if len(word) != num:
        raise ValidationError(
            _('%(word)s contains %(length)d letters, not %(num)d.'),
            params={'word': word, 'length': len(word), 'num': num})


def validate_has_twenty_six_characters(word: str):
    """ Check that the word has 26 characters. """
    return _validate_has_character_count(word, 26)


def validate_has_two_characters(word: str):
    """ Check that the word has 2 characters. """
    return _validate_has_character_count(word, 2)
