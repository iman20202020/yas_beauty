from django.contrib import admin

from accounts.models import Teacher, Student, Syllabus, PriceRange, LearnCategory, City

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Syllabus)
admin.site.register(PriceRange)
admin.site.register(LearnCategory)
admin.site.register(City)

