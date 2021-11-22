from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Teacher, StudentSubmit, Syllabus, PriceRange, LearnCategory, City, MyUser

admin.site.register(Teacher)
admin.site.register(StudentSubmit)
admin.site.register(Syllabus)
admin.site.register(PriceRange)
admin.site.register(LearnCategory)
admin.site.register(City)
admin.site.register(MyUser, UserAdmin)
UserAdmin.fieldsets += ('Custom fields set', {'fields': ('phone_number', )}),