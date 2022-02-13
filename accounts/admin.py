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
# UserAdmin.fieldsets += ('Custom fields set', {'fields': ('phone_number', )}),

#
# class SoftwareVersionAdmin(ModelAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         # Proper kwargs are form, fields, exclude, formfield_callback
#         if obj: # obj is not None, so this is a change page
#             kwargs['exclude'] = []
#         else: # obj is None, so this is an add page
#             kwargs['fields'] = ['phone_number',]
#         return super(SoftwareVersionAdmin, self).get_form(request, obj, **kwargs)