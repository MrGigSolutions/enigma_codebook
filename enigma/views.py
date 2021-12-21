from . import models as local_models
from . import serializers as local_serializers
from django.http import Http404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class EnigmaRotorListView(
        mixins.ListModelMixin,
        generics.GenericAPIView):
    queryset = local_models.EnigmaRotor.objects.all()
    serializer_class = local_serializers.EnigmaRotorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EnigmaSettingsListView(
        mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = local_serializers.EnigmaSettingSerializer

    def __init__(self):
        super().__init__()
        self.date = timezone.now().date()

    def get_queryset(self):
        return local_models.EnigmaSetting.objects.filter(date=self.date)

    def get(self, request, *args, **kwargs):
        self.date = kwargs['date']
        return self.list(request, *args, **kwargs)


