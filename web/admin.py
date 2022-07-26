from django.contrib import admin

from web.models import CV,Contact

# Register your models here.


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'user_email', 'upload_date')
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'date')