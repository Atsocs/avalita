from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Student, Professor, Course, Rating


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'


class ProfessorInline(admin.StackedInline):
    model = Professor
    can_delete = False
    verbose_name_plural = 'professor'


class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline, ProfessorInline)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Rating)
