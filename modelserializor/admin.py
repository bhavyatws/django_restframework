from django.contrib import admin

# Register your models here.
from . models import Student_Table
# Register your models here.
@admin.register(Student_Table)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']