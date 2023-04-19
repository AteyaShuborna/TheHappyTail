from django.contrib import admin
from .models import AdoptionPost,MissingPost,AdoptionRequest
# Register your models here.

admin.site.register(AdoptionPost)
admin.site.register(MissingPost)
admin.site.register(AdoptionRequest)
