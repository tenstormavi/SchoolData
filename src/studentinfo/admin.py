from django.contrib import admin

# Register your models here.
from .models import StudentInfo


class StudentInfoAdmin(admin.ModelAdmin):
	class Meta:
		model = StudentInfo

admin.site.register(StudentInfo, StudentInfoAdmin)
