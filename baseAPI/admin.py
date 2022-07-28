from django.contrib import admin
from .models import Snippet
# Register your models here.

class EmpTable(admin.ModelAdmin):
    list_display = ('id', 'created', 'title', 'code', 'linenos')
admin.site.register(Snippet,EmpTable)
