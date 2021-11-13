from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from accounts.models import Student, Teacher, MyUser
from teachme.send_sms import *
from yas7 import settings


# def index(request):
#     return render(request, 'teachme/index.html', {})


def teacher_list(request):
    learn_type_to_show =None
    user_select = MyUser.objects.get(id=request.user.pk)
    student_selected = Student.objects.get(user=user_select)
    student_city = student_selected.city
    city_to_show = student_selected.city.city_name
    student_learn_type = student_selected.learn_type

    if student_learn_type == 0:
        learn_type_to_show = 'آنلاین یا حضوری'
    if student_learn_type == 1:
        learn_type_to_show = 'آنلاین '
    if student_learn_type == 2:
        learn_type_to_show = 'حضوری'



    student_category = student_selected.category
    student_syllabus = student_selected.syllabus
    student_price_range = student_selected.price_range
    # student_mobile_number = student_selected.mobile_number
    if student_selected.learn_type < 2:
        teachers = Teacher.objects.filter(category=student_category, syllabus=student_syllabus,
                                          price_range=student_price_range,is_confirmed=True)
    else:
        teachers = Teacher.objects.filter(category=student_category, syllabus=student_syllabus,
                                          price_range=student_price_range, city=student_city,
                                          learn_type=student_learn_type,is_confirmed=True)

    teachers = Paginator(teachers, 15)
    page_number = request.GET.get('page')
    page_obj = teachers.get_page(page_number)
    context = {
        'teachers': teachers,
        'page_obj': page_obj,
        'student_category': student_category,
        'learn_type_to_show': learn_type_to_show,
        'student_price_range': student_price_range,
        'student_syllabus': student_syllabus,
        'city_to_show': city_to_show,
    }
    return render(request, 'teachme/teacher_list.html', context)

@login_required
def teacher_detail(request, teacher_id):
    student_user_id = request.user.id
    teacher_selected = Teacher.objects.get(pk=teacher_id)

    context = {
        'teacher_selected': teacher_selected,
        'student_user_id': student_user_id,
    }
    return render(request, 'teachme/teacher_detail.html', context)


def teacher_request(request):
    clerk_phone = '09361164819'
    teacher_id = request.POST.get('teacher_selected_id')
    teacher_requested = Teacher.objects.get(id=teacher_id)
    teacher_requested_user_id = getattr(teacher_requested,'user_id')
    teacher_requested_user_params = MyUser.objects.get(id=teacher_requested_user_id)
    teacher_phone = teacher_requested_user_params.phone_number
    student_user_id = request.POST.get('student_user_id')
    student = Student.objects.get(user_id=student_user_id)
    student_user_params = MyUser.objects.get(id=student_user_id)
    student_phone = student_user_params.phone_number
    clerk_sms_token = 'id:{},uid{}'.format(teacher_id, teacher_requested_user_id)
    clerk_sms_token2 = teacher_phone
    clerk_sms_token3 = 'id{},{}'.format(student.id,student_phone)
    send_sms_stu(student_phone,teacher_requested.last_name)
    send_sms_clerk(clerk_phone,clerk_sms_token,clerk_sms_token2,clerk_sms_token3)

    # send_mail(
    #     'test from django',
    #     'Here is the message.',
    #     settings.EMAIL_HOST_USER,
    #     ['aliamiri@gmail.com'],
    #     # fail_silently=False,
    # )

    return HttpResponseRedirect(reverse('teachme:message_viewer',args=['درخواست شما ثبت شد بزودی جهت هماهنگی با شما تماس می گیریم'] ))

    # response = send_otp(mobile_number)
def message_viewer(request,message_get):
    message = message_get
    return render(request, 'teachme/message_viewer.html', {'message':message})