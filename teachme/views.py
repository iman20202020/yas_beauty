from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from accounts.models import  Teacher, MyUser, StudentSubmit
from teachme.send_sms import *


@login_required
def teacher_detail(request, teacher_id):
    teacher_selected = None
    student_user_id = None
    if hasattr(request.user, 'studentsubmit') ==False and  hasattr(request.user, 'teacher') == False:

        return render(request,'accounts/student_submit.html',context={'teacher_id':teacher_id})


    student_user_id = request.user.id
    teacher_selected = Teacher.objects.get(pk=teacher_id)

    #     return HttpResponseRedirect(reverse('teachme:message_viewer',args=['شما به عنوان معلم ثبت شده اید برای درخواست استاد دوباره با شماره تلفن و ایمیل جدید به عنوان دانش آموز ثبت نام کنید']))

    context = {
        'teacher_selected': teacher_selected,
        'student_user_id': student_user_id,
    }
    return render(request, 'teachme/teacher_detail.html', context)

@login_required
def teacher_request(request):
    clerk_phone = '09361164819'
    teacher_id = request.POST.get('teacher_selected_id')
    teacher_requested = Teacher.objects.get(id=teacher_id)
    teacher_requested_user_id = getattr(teacher_requested,'user_id')
    teacher_requested_user_params = MyUser.objects.get(id=teacher_requested_user_id)
    teacher_phone = teacher_requested_user_params.phone_number
    student_user_id = request.POST.get('student_user_id')
    if hasattr(request.user, 'studentsubmit'):
        student = StudentSubmit.objects.get(user_id=student_user_id)
    if hasattr(request.user, 'teacher'):
        student = Teacher.objects.get(user_id=student_user_id)
    student_user_params = MyUser.objects.get(id=student_user_id)
    student_phone = student_user_params.phone_number
    clerk_sms_token = 'id:{},uid{}'.format(teacher_id, teacher_requested_user_id)
    clerk_sms_token2 = teacher_phone
    clerk_sms_token3 = 'id{},{}'.format(student.id,student_phone)
    send_sms_stu(student_phone,teacher_requested.last_name)
    send_sms_clerk(clerk_phone,clerk_sms_token,clerk_sms_token2,clerk_sms_token3)
    message = 'درخواست شما ثبت شد بزودی جهت هماهنگی با شما تماس می گیریم'

    return render(request,'teachme/message_viewer.html', {'message': message})


def teacher_list(request):

    category_selected = request.GET.get('cat')
    syllabus_selected = request.GET.get('syl')


    teachers = Teacher.objects.filter(category=category_selected,syllabus=syllabus_selected,is_confirmed=True)
    teachers = Paginator(teachers, 25)
    page_number = request.GET.get('page')
    page_obj = teachers.get_page(page_number)
    context = {
        'teachers': teachers,
        'page_obj': page_obj,
        'student_category': category_selected,
        'student_syllabus': syllabus_selected,

    }
    return render(request, 'teachme/teacher_list.html', context)

    # response = send_otp(mobile_number)
# def message_viewer(request,message_get):
#     message = message_get
#     return render(request, 'teachme/message_viewer.html', {'message':message})