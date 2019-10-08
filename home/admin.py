from django.contrib import admin

# Register your models here.
from home.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'creatat')
    list_filter = ('status', 'creatat')
admin.site.site_title = "summer  project admin panel"
admin.site.site_header = "summer  project admin panel"
admin.site.index_title = "summer  project admin panel Home"

admin.site.register(Contact, ContactAdmin)