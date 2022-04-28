from django.core.paginator import Paginator
from django.shortcuts import render
from accounts.models import Teacher, MyUser, ClassRequest, Student, State
from accounts.otp import send_otp
from teachme.send_sms import *


def teacher_list(request):
    states = State.objects.all()
    category_id = request.GET.get('cat')
    syllabus_id = request.GET.get('syl')
    teachers = Teacher.objects.filter(category=category_id,syllabus=syllabus_id,is_confirmed=True).reverse().order_by('points')
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)

    context = {
        'teachers': teachers,
        'category_id': category_id,
        'syllabus_id': syllabus_id,
        'states': states,
        'state_filter': state_filter,

    }
    return render(request, 'teachme/teacher_list.html', context)


def teacher_detail(request, teacher_id):

    teacher_selected = Teacher.objects.get(pk=teacher_id)
    teacher_cat = teacher_selected.category_id
    context = {
        'teacher_selected': teacher_selected,
        'teacher_cat': teacher_cat,
    }
    return render(request, 'teachme/teacher_detail.html', context)


def teacher_requst_send(request, teacher_id):
    return render(request, 'teachme/request_user_verify.html', {'teacher_id': teacher_id})


def request_user_verify(request, teacher_id):
    clerk_phone = '09361164819'
    response = {}
    if 'teacher_selected_id' in request.POST:
        teacher_id = request.POST.get('teacher_selected_id')

    if request.method == 'POST':
        user_verified = None
        otp_code = None
        mobile_number = None

        if 'input_mobile' in request.POST:
            mobile_number = request.POST.get('input_mobile')
            if len(mobile_number) == 10:
                mobile_number = '0'+mobile_number

            response = send_otp(mobile_number)
            if response[0]['status'] == 5:
                user_verified = 'code_sent'
                otp_code = response[1]
            else:
                user_verified = 'code_not_sent'
                otp_code = None
        if 'veri_code_input' in request.POST and 'mobile_number'in request.POST:
            otp_code = request.POST.get('otp_code_generated')
            veri_code_input = request.POST.get('veri_code_input')
            mobile_number = request.POST.get('mobile_number')
            if len(mobile_number) == 10:
                mobile_number = '0'+mobile_number
            if otp_code == veri_code_input:
                teacher_requested = Teacher.objects.get(id=teacher_id)
                student_object = Student.objects.create(student_phone=mobile_number,
                                                        student_email='')
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

                teacher_requested_user_id = getattr(teacher_requested, 'user_id')
                teacher_requested_user_params = MyUser.objects.get(id=teacher_requested_user_id)
                teacher_phone = teacher_requested_user_params.phone_number

                student_phone = mobile_number
                clerk_sms_token = '{},uid{}'.format(teacher_requested.last_name, teacher_requested_user_id)
                clerk_sms_token2 = teacher_phone
                clerk_sms_token3 = student_phone
                send_sms_stu(student_phone, teacher_requested.last_name)
                send_sms_clerk(clerk_phone, clerk_sms_token, clerk_sms_token2, clerk_sms_token3)
                message = 'درخواست شما ثبت شد بزودی جهت هماهنگی با شما تماس می گیریم'

                return render(request, 'teachme/message_viewer.html', {'message': message})

            else:
                user_verified = 'code_check_error'
    else:
        user_verified = None
        otp_code = None
        mobile_number = None
    context = {
     'mobile_number': mobile_number,
     'user_verified': user_verified,
     'response': response,
     'otp_code': otp_code,
     'teacher_id': teacher_id,
     }
    return render(request, 'teachme/request_user_verify.html', context )



def nakhon_list(request):
    teachers = Teacher.objects.filter(syllabus='خدمات ناخن',is_confirmed=True).reverse().order_by('points')
    state_filter = request.GET.get('st')

    context = {
        'teachers': teachers,
        'state_filter': state_filter,
    }
    return render(request, 'teachme/nakhon_list.html', context)
