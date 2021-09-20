from agency.models import Agency, Program
from django.contrib import admin


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    model = Agency
    list_display = ('name', )


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    model = Program
    list_display = ('go_from', 'go_to', 'go_date_time', 'price')
