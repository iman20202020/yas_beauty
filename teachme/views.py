from django.shortcuts import render



from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from accounts.models import Student, Teacher


def index(request):
    return render(request, 'teachme/index.html', {})


def teacher_list(request):
    user_select = User.objects.get(id=request.user.pk)
    student_selected = Student.objects.get(user=user_select)
    student_city = student_selected.city
    student_learn_type = student_selected.learn_type
    student_category = student_selected.category
    student_syllabus = student_selected.syllabus
    student_price_range = student_selected.price_range
    # student_mobile_number = student_selected.mobile_number
    if student_selected.learn_type < 2:
        teachers = Teacher.objects.filter( category=student_category, syllabus=student_syllabus,
                                      price_range=student_price_range)
    else:
        teachers = Teacher.objects.filter(category=student_category, syllabus=student_syllabus,
                                          price_range=student_price_range,city=student_city,learn_type=student_learn_type)
    teachers = Paginator(teachers, 5)
    page_number = request.GET.get('page')
    page_obj = teachers.get_page(page_number)
    context = {
        'teachers': teachers,
        'page_obj': page_obj,
    }
    return render(request, 'teachme/teacher_list.html', context)


def teacher_detail(request, teacher_id):
    teacher_selected = Teacher.objects.get(pk=teacher_id)
    context = {
        'teacher_selected': teacher_selected,
    }
    return render(request, 'teachme/teacher_detail.html', context)

