from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Teacher, StudentSubmit, Syllabus, PriceRange, LearnCategory, City, MyUser,RequestClass

admin.site.register(Teacher)
admin.site.register(StudentSubmit)
admin.site.register(RequestClass)
admin.site.register(Syllabus)
admin.site.register(PriceRange)
admin.site.register(LearnCategory)
admin.site.register(City)


class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'phone_number')
        }))


admin.site.register(MyUser, MyUserAdmin)
# UserAdmin.fieldsets += ('Custom fields set', {'fields': ('phone_number', )}),