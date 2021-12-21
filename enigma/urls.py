import datetime

from django.urls import path, include, register_converter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value.strftime(value, '%Y-%m-%d')


register_converter(DateConverter, 'reverse_date')

urlpatterns = [
    path('api/v1/', include([
        path('codes/<reverse_date:date>/',
             views.EnigmaSettingsListView.as_view()),
        path('rotors/', views.EnigmaRotorListView.as_view()),
    ])),
]

urlpatterns = format_suffix_patterns(urlpatterns)