from django.contrib import admin
from .models import Card
from .models import Quote

class CardAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'designation', 'location', 'apply_link')
    search_fields = ('company_name', 'designation', 'location')

admin.site.register(Card, CardAdmin)
admin.site.register(Quote)

   