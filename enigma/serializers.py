from rest_framework import serializers
from . import models as local_models


class EnigmaNotchStringRelatedField(serializers.StringRelatedField):
    def get_queryset(self):
        return local_models.EnigmaRotorNotch.objects.all()

    def to_representation(self, instance):
        return instance.notch

    def to_internal_value(self, data):
        raise serializers.ValidationError(
            'Updating notches from the API is not supported.')


class EnigmaRotorSerializer(serializers.ModelSerializer):
    """ Serializes a rotor by name"""
    name = serializers.CharField(max_length=255)
    sequence = serializers.CharField(max_length=26)
    notch_set = EnigmaNotchStringRelatedField(many=True)

    class Meta:
        model = local_models.EnigmaRotor
        fields = ['name', 'sequence', 'notch_set']


class EnigmaPlugSettingSerializer(serializers.ModelSerializer):
    """ Serializes a plug by substitution """
    substitution = serializers.CharField(max_length=2)

    class Meta:
        model = local_models.EnigmaPlugSetting
        fields = ['substitution']


class EnigmaRotorNameRelatedField(serializers.StringRelatedField):
    def get_queryset(self):
        return local_models.EnigmaRotor.objects.all()

    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        try:
            return local_models.EnigmaRotor.get(name=data)
        except local_models.EnigmaRotor.DoesNotExist:
            raise serializers.ValidationError(
                f'Rotor \'{data}\' was not found in the code book.')


class EnigmaPlugSubstitutionRelatedField(serializers.StringRelatedField):
    def get_queryset(self):
        return local_models.EnigmaPlugSetting.objects.all()

    def to_representation(self, instance):
        return instance.substitution

    def to_internal_value(self, data):
        raise serializers.ValidationError(
            'It is currently not possible to set plug settings '
            'through the serializer.')


class EnigmaSettingSerializer(serializers.ModelSerializer):
    """ A serializer for an Enigma codebook setting that can be consumed
    by an Enigma machine """
    date = serializers.DateField()
    rotors = EnigmaRotorNameRelatedField(many=True)
    plug_settings_set = EnigmaPlugSubstitutionRelatedField(many=True)
    indicator = serializers.CharField(max_length=3)
    reflector = EnigmaRotorNameRelatedField()

    class Meta:
        model = local_models.EnigmaSetting
        fields = ['date', 'rotors', 'plug_settings_set', 'indicator',
                  'reflector']

