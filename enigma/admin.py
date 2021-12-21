from django.contrib import admin

from . import models as local_models

# Register your models here.
admin.site.register(local_models.EnigmaSetting)
admin.site.register(local_models.EnigmaRotor)
admin.site.register(local_models.EnigmaPlugSetting)
admin.site.register(local_models.EnigmaRotorSetting)
admin.site.register(local_models.EnigmaRotorNotch)
