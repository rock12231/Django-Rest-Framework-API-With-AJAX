from django.contrib import admin
from .models import Emp
# Register your models here.

class EmpTable(admin.ModelAdmin):
    list_display = ('id','name','position','salary','start_date','office','extn')
admin.site.register(Emp,EmpTable)
