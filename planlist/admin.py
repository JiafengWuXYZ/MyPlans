from django.contrib import admin
from .models import Plan, Planer


class PlanAdmin(admin.ModelAdmin):
    list_display = ("content", "planer")


# Register your models here.
admin.site.register(Plan, PlanAdmin)
admin.site.register(Planer)
