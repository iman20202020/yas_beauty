

from django.contrib import admin
from accounts.models import Teacher, Syllabus, PriceRange, LearnCategory, City, MyUser, State, ClassRequest, Student, \
    Comment

admin.site.register(Syllabus)
admin.site.register(PriceRange)
admin.site.register(LearnCategory)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Student)
admin.site.register(ClassRequest)
admin.site.register(MyUser)


class TeacherAdmin(admin.ModelAdmin):
    list_filter = ('is_confirmed', 'syllabus', 'state')
    search_fields = ['last_name', ]


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('is_confirmed',)


admin.site.register(Comment, CommentAdmin)

admin.site.register(Teacher, TeacherAdmin)
