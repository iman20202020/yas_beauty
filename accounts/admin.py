

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Teacher, Syllabus, PriceRange, LearnCategory, City, MyUser, State, ClassRequest, Student, \
    Comment

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
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email','phone_number')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class TeacherAdmin(admin.ModelAdmin):
    list_filter = ('is_confirmed','syllabus','state')
    search_fields = ['last_name',]


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('is_confirmed',)
    # search_fields = ['content',]


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Teacher, TeacherAdmin)