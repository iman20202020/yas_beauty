from django.shortcuts import render
from accounts.models import Teacher, Syllabus


def show_blog(request, blog_num):
    blog_template = 'blog' + str(blog_num)+'.html'
    return render(request, blog_template, {})

def view_all_teachers(request):
    number_of_teachers = Teacher.objects.filter(is_confirmed=True).count()
    return render(request, 'all_teachers.html', { 'num_teachers': number_of_teachers, })

def teacher_list_generator(request):
    teachers = Teacher.objects.filter(is_confirmed=True).order_by('-points')
    syllabuses = Syllabus.objects.all()
    return render(request,'teacher_list_generator.html',{'teachers': teachers, 'syllabuses': syllabuses})


