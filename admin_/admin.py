from django.contrib import admin
from .models import absence, Admin, Stagiaire

admin.site.register(Admin)
admin.site.register(Stagiaire)
admin.site.register(absence)
