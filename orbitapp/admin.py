# myapp/admin.py
from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'designation', 'apply_link', 'location')

admin.site.register(Card, CardAdmin)
