from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from accounts.models import Teacher, MyUser, ClassRequest, Student
from teachme.send_sms import *



def teacher_detail(request):
    teacher_id = request.GET.get('teacher_id')
    student_category = request.GET.get('student_category')
    teacher_selected = Teacher.objects.get(pk=teacher_id)


    context = {
        'teacher_selected': teacher_selected,
        'student_category': student_category,
    }
    return render(request, 'teachme/teacher_detail.html', context)


@login_required
def teacher_request(request,teacher_id):
    clerk_phone = '09361164819'

    teacher_requested = Teacher.objects.get(id=teacher_id)
    student = MyUser.objects.get(pk=request.user.id)
    student_object = Student.objects.create(student_phone=student.phone_number, student_email=student.username)
    student_object.save()

    class_request = ClassRequest.objects.create(
        teacher=teacher_requested,
        student=student_object,
        teacher_email=teacher_requested.user.username,
        student_email=student_object.student_email,
        teacher_phone=teacher_requested.user.phone_number,
        student_phone=student_object.student_phone,
        teacher_last_name=teacher_requested.last_name,
        price=teacher_requested.price_range,
        workshop_price=teacher_requested.workshop_price,
        category=teacher_requested.category,
        syllabus=teacher_requested.syllabus,
        city=teacher_requested.city,
        )
    class_request.save()

    teacher_requested_user_id = getattr(teacher_requested,'user_id')
    teacher_requested_user_params = MyUser.objects.get(id=teacher_requested_user_id)
    teacher_phone = teacher_requested_user_params.phone_number

    student_phone = student.phone_number
    clerk_sms_token = 'id:{},uid{}'.format(teacher_id, teacher_requested_user_id)
    clerk_sms_token2 = teacher_phone
    clerk_sms_token3 = 'uid{},{}'.format(student.id,student_phone)
    send_sms_stu(student_phone,teacher_requested.last_name)
    send_sms_clerk(clerk_phone,clerk_sms_token,clerk_sms_token2,clerk_sms_token3)
    message = 'درخواست شما ثبت شد بزودی جهت هماهنگی با شما تماس می گیریم'

    return render(request,'teachme/message_viewer.html', {'message': message})


def teacher_list(request):
    category_selected = request.GET.get('cat')
    syllabus_selected = request.GET.get('syl')

    teachers = Teacher.objects.filter(category=category_selected,syllabus=syllabus_selected,is_confirmed=True).order_by('_points')
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

