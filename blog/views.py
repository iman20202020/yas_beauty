from django.shortcuts import render
from accounts.models import Teacher


def show_blog(request, blog_num):
    blog_template = 'blog' + str(blog_num)+'.html'
    return render(request, blog_template, {})

def view_all_teachers(request):
    teachers = Teacher.objects.filter(is_confirmed=True)
    number_of_teachers = teachers.count()
    return render(request, 'all_teachers.html', {'teachers': teachers, 'num_teachers': number_of_teachers, })