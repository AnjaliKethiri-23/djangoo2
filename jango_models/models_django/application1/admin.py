from django.contrib import admin

# Register your models here.
from application1.models import Employee,students
class Employee_admin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','emp_salary','emp_email']
    ordering=['emp_id']
admin.site.register(Employee,Employee_admin)    

class students_admin(admin.ModelAdmin):
    list_display=['std_name','std_pin']
    ordering=['std_pin']
admin.site.register(students,students_admin)    