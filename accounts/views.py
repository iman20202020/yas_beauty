from itertools import chain
from django.contrib import messages
from django.shortcuts import redirect
from accounts import phone_vrify
from accounts.otp import *
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from accounts.models import Teacher, MyUser, ClassRequest
from blog.models import Blog


def index_accounts(request):
    teachers_count = Teacher.objects.filter(is_confirmed=True).count()
    teacher_bests = Teacher.objects.all().order_by('-points')[:9]
    total_class_count = ClassRequest.objects.filter(is_confirmed=True).count()

    context = {
        'teacher_bests': teacher_bests,
        'teachers_count': teachers_count,
        'total_class_count': total_class_count,
    }

    return render(request, 'accounts/index.html', context)


def contact_us(request):
    return render(request, 'accounts/contact_us.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index_accounts'))


@login_required
def profile_edit(request):
    return HttpResponseRedirect(reverse('accounts:teacher_edit'))



def search_view(request):
    results = []
    results_teachers = []
    search_message = None
    if request.method == "GET":
        search_query = request.GET.get('search_text', None)
        if search_query:
            result1_teachers = Teacher.objects.filter(syllabus__syllabus_name__contains=search_query, is_confirmed=True)
            result3_teachers = Teacher.objects.filter(
                Q(last_name__contains=search_query, is_confirmed=True) | Q(first_name__contains=search_query,
                                                                           is_confirmed=True) | Q(
                    qualification__contains=search_query, is_confirmed=True))
            result4_teachers = Teacher.objects.filter(
                Q(city__city__contains=search_query, is_confirmed=True) | Q(first_name__contains=search_query,
                                                                            is_confirmed=True) | Q(
                    qualification__contains=search_query, is_confirmed=True))
            results_teachers = list(chain(result1_teachers, result3_teachers, result4_teachers, ))
            if results_teachers:
                search_message = str(len(results_teachers)) + "استاد پیدا شد"
            else:
                search_message = "موردی یافت نشد"

        return render(request, 'accounts/index.html',
                      {'results': results, 'search_message': search_message, 'results_teachers': results_teachers})


def user_verify(request):
    return redirect(reverse('accounts:login_view'))


def login_view(request):
    response = {}
    logout(request)
    if request.method == 'POST':
        user_verified = None
        otp_code = None
        mobile_number = None

        if 'input_mobile' in request.POST:
            mobile_number = request.POST.get('input_mobile')
            if len(mobile_number) == 10:
                mobile_number = '0' + mobile_number
            response = fake_send_otp(mobile_number)
            # response = send_otp(mobile_number)
            if response[0]['status'] == 5:
                user_verified = 'code_sent'
                otp_code = response[1]
            else:
                user_verified = 'code_not_sent'
                otp_code = None
        if 'veri_code_input' in request.POST and 'mobile_number' in request.POST:
            otp_code = request.POST.get('otp_code_generated')
            veri_code_input = request.POST.get('veri_code_input')
            mobile_number = request.POST.get('mobile_number')
            if len(mobile_number) == 10:
                mobile_number = '0' + mobile_number
            if otp_code == veri_code_input:
                user_verified = 'code_checked'
                user_exists = MyUser.objects.filter(username=mobile_number).exists()

                if user_exists:
                    user = MyUser.objects.get(username=mobile_number)
                    user.set_password(otp_code)
                    user.save()
                else:
                    user = MyUser.objects.create(username=mobile_number, password=otp_code, )
                login(request, user)
                context = {
                    'user_verified': user_verified,
                    'mobile_number': mobile_number,
                }
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return render(request, 'accounts/index.html', context)
            else:
                user_verified = 'code_check_error'
    else:
        user_verified = None
        otp_code = None
        mobile_number = None
        my_next = None

    context = {
        'mobile_number': mobile_number,
        'user_verified': user_verified,
        'response': response,
        'otp_code': otp_code,
    }
    return render(request, 'accounts/user_verify.html', context)


def site_laws(request):
    return render(request, 'accounts/sit_laws.html', {})


def how_use(request):
    return render(request, 'accounts/how_use.html', {})


def how_use2(request):
    return render(request, 'accounts/how_use2.html', {})


def teacher_laws(request):
    return render(request, 'accounts/teacher_laws.html', {})


def consult_view(request):
    clerk_phone = '09361164819'
    if request.method == 'POST':
        if 'input_mobile' in request.POST:
            mobile_number = request.POST.get('input_mobile')
        elif 'mobile_number' in request.POST:
            mobile_number = request.POST.get('mobile_number')
        else:
            mobile_number = None

        if 'veri_code_input' in request.POST and 'otp_code_generated' in request.POST:
            veri_code_input = request.POST.get('veri_code_input')
            otp_code = request.POST.get('otp_code_generated')
            if phone_vrify.code_otp_check(otp_code, veri_code_input):
                token = str(mobile_number)
                token2 = 'مشاوره'
                send_sms(clerk_phone, token, token2)
                messages.success(request, 'درخواست شما ثبت شد بزودی جهت مشاوره با شما تماس می گیریم', 'success')
                return redirect('accounts:index_accounts')
            else:
                otp_code = None
                user_verified = None
        else:
            otp_code = phone_vrify.code_send(mobile_number)
            user_verified = 'code_sent'
    else:
        user_verified = None
        otp_code = None
        mobile_number = None
    context = {
        'mobile_number': mobile_number,
        'user_verified': user_verified,
        'otp_code': otp_code,
    }
    return render(request, 'accounts/user_verify.html', context)


# comment for redirect to teacher_detail_view
# @login_required
# def comment_view(request, teacher_id):
#     return redirect('teachme:teacher_detail', args=[teacher_id])
