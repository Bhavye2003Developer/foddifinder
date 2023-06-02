from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(contactDetail)
admin.site.register(Register)
admin.site.register(BioData)