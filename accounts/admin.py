from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Teacher, Syllabus, PriceRange, LearnCategory, City, MyUser, State, ClassRequest, Student

admin.site.register(Teacher)
# admin.site.register(StudentSubmit)
# admin.site.register(RequestClass)
admin.site.register(Syllabus)
admin.site.register(PriceRange)
admin.site.register(LearnCategory)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Student)
admin.site.register(ClassRequest)


class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'phone_number')
        }))


admin.site.register(MyUser, MyUserAdmin)

