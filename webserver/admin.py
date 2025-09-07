from django.contrib import admin
from . models import Sign_in


class Sign_inAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("firstname", "lastname")}


admin.site.register(Sign_in, Sign_inAdmin)
