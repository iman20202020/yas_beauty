from django.http import HttpResponse
from django.shortcuts import render



from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from accounts.models import Student, Teacher, MyUser
from teachme.send_sms import *


def index(request):
    return render(request, 'teachme/index.html', {})


def teacher_list(request):
    user_select = MyUser.objects.get(id=request.user.pk)
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
    student_user_id = request.user.id
    teacher_selected = Teacher.objects.get(pk=teacher_id)
    context = {
        'teacher_selected': teacher_selected,
        'student_user_id': student_user_id,
    }
    return render(request, 'teachme/teacher_detail.html', context)

def teacher_request(request):
    teacher_id = request.POST.get('teacher_selected_id')

    teacher_requested = Teacher.objects.get(id=teacher_id)
    # teacher_requested_user_id = getattr(teacher_requested,'user_id')
    # teacher_requested_user_params = MyUser.objects.get(id=teacher_requested_user_id)
    # teacher_phone = teacher_requested_user_params.phone_number

    student_user_id = request.POST.get('student_user_id')
    # student = Student.objects.get(user_id=student_user_id)
    student_user_params = MyUser.objects.get(id=student_user_id)
    student_phone = student_user_params.phone_number
    send_sms_stu(student_phone,teacher_requested.last_name)

    return HttpResponse(student_phone)



    # response = send_otp(mobile_number)