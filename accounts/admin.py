

from django.contrib import admin
from accounts.models import Teacher, Syllabus, PriceRange, LearnCategory, City, MyUser, State, ClassRequest, Student, \
    Comment

admin.site.register(Syllabus)
admin.site.register(PriceRange)
admin.site.register(LearnCategory)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Student)
# admin.site.register(ClassRequest)
# admin.site.register(MyUser)

class MyUserAdmin(admin.ModelAdmin):
    search_fields = ['username', ]

class TeacherAdmin(admin.ModelAdmin):
    list_filter = ('is_confirmed', 'syllabus', 'state')
    search_fields = ['last_name', ]
    readonly_fields = ['created', 'updated', ]


class ClassRequestAdmin(admin.ModelAdmin):
    list_filter = ('teacher', 'student', 'teacher_phone', 'student_phone', 'category', 'syllabus', 'price',
                   'workshop_price', 'city', 'created', 'updated')
    readonly_fields = ['created', 'updated', ]

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('is_confirmed', ('content', admin.EmptyFieldListFilter))


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(ClassRequest, ClassRequestAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Teacher, TeacherAdmin)
