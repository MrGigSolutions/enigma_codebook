# DJANGO ENIGMA CODE BACKEND


## Summary

This application is a simple database that contains
code book settings and rotor settings used in an Enigma machine.
It exposes a small API that allows a user to retrieve the
rotor information and codebook settings entered in the database,
which can then be consumed by an enigma code machine.

## Endpoints

The following endpoints are exposed:
### Rotors

    enigma/api/v1/rotors/

This allows downloading of the wiring schemes of the rotors.

### Codebooks
The other endpoint is the code book settings:

    enigma/api/v1/codes/<date>/

This endpoint contains the code book for the entered date.

## JSON files

### Rotors
Rotor files are formatted as below:

    {
        'name': 'I',
        'sequence': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'notch_set': ['C', 'D']
    }

Parameters are:
- The name of the rotor. This is usually a roman numeral but can be anything.
- The letter sequence representing the wiring of the rotor. The first letter
  represents the output of the letter 'A' with no offset. The second letter is
  'B', etc. This needs to be a string of 26 characters, all alphabetic, 
  all different.
  *Note:* reflectors are almost the same as rotors, but have no notches.
  A normal rotor may also be used as a reflector, in which case its notches
  are ignored.
- The notch indicates the letter that is indicated on the rotor when it causes
  the rotor to its left to turn. In the example above, then the rotor position
  is 'C', and a letter is typed, the rotor turns to 'D', but because 'C' is a 
  notch, the rotor to its left also turns.

# Codebook
Codebook files are formatted as below:

    {
        'date': '2021-12-19',
        'rotors': ['I', 'IV', 'II']
        'indicator': 'AVQ'
        'plug_set': ['AE', 'BC', 'DQ', 'JK']
    }

Parameters are:
- Date of the setting. Settings were typcially changed once per day.
- Rotors: The rotor order in the machine, from left to right
- Indicator: the indicator used to encode messages for the day.
  Indicators have as many letters as there are rotors, and represent the 
  letters showing on the display, representing the rotor offset.
- The plug set is a set of characters that is interchanged 
  prior to encoding through the rotors. When a message is encoded, 
  the plugs are reversed.
