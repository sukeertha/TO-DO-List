from django.contrib import admin
from .models import taskes

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at')
    search_fields=('tasks',)
admin.site.register(taskes,TaskAdmin)
