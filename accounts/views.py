from itertools import chain
from accounts.otp import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from accounts.forms import MyUserCreate, StudentEditForm, TeacherEditForm
from accounts.models import LearnCategory, Syllabus, PriceRange, Student, Teacher, City, MyUser


def base_view(request):
    return render(request, 'accounts/_base.html', {})


def index_accounts(request):
#slect syllabuses for each category on index
    syllabuses_university = Syllabus.objects.filter(learn_category='دانشگاهی')
    teacher_university = Teacher.objects.filter(category='دانشگاهی',is_confirmed=True)
    syllabuses_high_school = Syllabus.objects.filter(learn_category='متوسطه دوم')
    teacher_high_school = Teacher.objects.filter(category='متوسطه دوم',is_confirmed=True)
    syllabuses_mid_school = Syllabus.objects.filter(learn_category='متوسطه اول')
    teacher_mid_school = Teacher.objects.filter(category='متوسطه اول',is_confirmed=True)
    syllabuses_primary_school = Syllabus.objects.filter(learn_category='دبستان')
    teacher_primary_school = Teacher.objects.filter(category='دبستان',is_confirmed=True)
    syllabuses_computer = Syllabus.objects.filter(learn_category='کامپیوتر')
    teacher_computer = Teacher.objects.filter(category='کامپیوتر',is_confirmed=True)
    syllabuses_music = Syllabus.objects.filter(learn_category='موسیقی')
    teacher_music = Teacher.objects.filter(category='موسیقی',is_confirmed=True)
    syllabuses_art = Syllabus.objects.filter(learn_category='هنرهای تجسمی')
    teacher_art = Teacher.objects.filter(category='هنرهای تجسمی',is_confirmed=True)
    syllabuses_sport = Syllabus.objects.filter(learn_category='ورزش')
    teacher_sport = Teacher.objects.filter(category='ورزش',is_confirmed=True)
    syllabuses_cinema = Syllabus.objects.filter(learn_category='سینما و بازیگری')
    teacher_cinema = Teacher.objects.filter(category='سینما و بازیگری',is_confirmed=True)
    syllabuses_tech = Syllabus.objects.filter(learn_category='کارهای فنی')
    teacher_tech = Teacher.objects.filter(category='کارهای فنی',is_confirmed=True)
    syllabuses_cooking = Syllabus.objects.filter(learn_category='آشپزی')
    teacher_cooking = Teacher.objects.filter(category='آشپزی',is_confirmed=True)
    syllabuses_makeup = Syllabus.objects.filter(learn_category='آرایش و زیبایی')
    teacher_makeup = Teacher.objects.filter(category='آرایش و زیبایی',is_confirmed=True)
    syllabuses_language = Syllabus.objects.filter(learn_category='زبان های خارجی')
    teacher_language = Teacher.objects.filter(category='زبان های خارجی',is_confirmed=True)

    context = {
        'syllabuses_university': syllabuses_university,
        'teacher_university': teacher_university,
        'syllabuses_high_school': syllabuses_high_school,
        'teacher_high_school': teacher_high_school,
        'syllabuses_mid_school': syllabuses_mid_school,
        'teacher_mid_school': teacher_mid_school,
        'syllabuses_sport': syllabuses_sport,
        'teacher_sport': teacher_sport,
        'syllabuses_music': syllabuses_music,
        'teacher_music': teacher_music,
        'syllabuses_art': syllabuses_art,
        'teacher_art': teacher_art,
        'syllabuses_computer': syllabuses_computer,
        'teacher_computer': teacher_computer,
        'syllabuses_primary_school': syllabuses_primary_school,
        'teacher_primary_school': teacher_primary_school,
        'syllabuses_cinema': syllabuses_cinema,
        'teacher_cinema': teacher_cinema,
        'syllabuses_tech': syllabuses_tech,
        'teacher_tech': teacher_tech,
        'syllabuses_cooking': syllabuses_cooking,
        'teacher_cooking': teacher_cooking,
        'syllabuses_makeup': syllabuses_makeup,
        'teacher_makeup': teacher_makeup,
        'syllabuses_language': syllabuses_language,
        'teacher_language': teacher_language,
    }
    return render(request, 'accounts/index.html', context)


def contact_us(request):
    return render(request, 'accounts/contact_us.html', {})


def user_create(request):
    if request.method == 'POST':
        logout(request)
        user_create_form = MyUserCreate(request.POST)
        if user_create_form.is_valid:
            try:
                user = user_create_form.save(commit=False)
                # user.is_active = False
                user_saved = user
                user.save()
                login(request, user)
            except:
                user_saved = None
        else:
            user_saved = None
    else:
        user_create_form = MyUserCreate()
        user_saved = None
    context = {
        'user_create_form': user_create_form,
        'user_saved': user_saved,
    }
    return render(request, 'accounts/user_create.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            if hasattr(user, 'teacher'):
                return HttpResponseRedirect(reverse('accounts:teacher_edit'))
            elif hasattr(user, 'student'):
                return HttpResponseRedirect(reverse('accounts:student_edit'))
            else:
                return render(request,'accounts/user_create.html',{'user_saved': 1})
        else:
            context = {
                'username': username,
                'error': "کاربر موجود نیست",
            }
            return render(request, 'accounts/login.html', context)
    else:
        context = {}
        return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index_accounts'))


@login_required
def profile_edit(request):
    if hasattr(request.user, 'teacher'):
        return HttpResponseRedirect(reverse('accounts:teacher_edit'))
    # if hasattr(request.user, 'student'):
    #     return HttpResponseRedirect(reverse('accounts:student_edit'))
    else:
        return HttpResponseRedirect(reverse('accounts:student_edit'))
        # get_user_pk = request.user.pk
        # MyUser.objects.get(pk=get_user_pk).delete()
        # return HttpResponse("لطفا دوباره بصورت معلم یا دانش آموز ثبت نام کنید")


@login_required
@csrf_exempt
def student_edit(request):
    if request.is_ajax():
        category = request.GET.get('category',None)
        category_list = request.GET.get('category_list', None)
        if category_list:
            category_list = list(LearnCategory.objects.all().values())
            return JsonResponse(category_list, safe=False)
        syll = list(Syllabus.objects.filter(learn_category=category).values())
        return JsonResponse(syll, safe=False)
    else:
        student_edit_form = StudentEditForm()
        cities = list(City.objects.all().values())
        price_ranges = list(PriceRange.objects.all().values())
        # languages = list(Language.objects.all().values())
        categories = list(LearnCategory.objects.all().values())
        syllabuses = None
        student_profile = None
        error = None
        if hasattr(request.user, 'student'):
            student_profile = Student.objects.get(user_id=request.user.id)
            student_edit_form = StudentEditForm(instance=student_profile)
            error = str(request.user)+" "+'خوش آمدید'
            if request.method == 'POST':
                try:
                    student_edited = StudentEditForm(request.POST)
                    student_edited = student_edited.save(commit=False)
                    student_edited.user = request.user
                    student_edited.pk = student_profile.id
                    student_edited.save()
                    student_profile = request.user.student
                    error = "مشخصات جستجوی شما با موفقیت تغییر یافت "
                except :
                    error = 'ورودی های خود را کنترل کنید'
                    raise ValidationError( 'ورودی های خود را کنترل کنید')
            if hasattr(request.user, 'teacher'):
                get_user_pk = request.user.pk
                return HttpResponse("شما به عنوان معلم ثبت نام کرده اید نه دانش آموز ")
        if request.method == 'POST' and hasattr(request.user, 'student') is False:
            try:
                student_edit_form = StudentEditForm(request.POST)
                if student_edit_form.is_valid():
                    student = student_edit_form.save(commit=False)
                    student.user = request.user
                    student.save()
                    error = "به عنوان دانش آموز در سیستم ثبت شدید"
                    student_profile = request.user.student
            except:
                student_profile = request.POST
                error = "لطفا ورودی های خود را کنترل کنید"
        context = {
            'student_profile' : student_profile,
            'student_edit_form': student_edit_form,
            'error': error,
            'cities': cities,
            'price_ranges' : price_ranges,
            # 'learn_types' : learn_types,
            'categories' : categories,
            'syllabuses' : syllabuses,
            # 'first_name' : first_name,
            # 'last_name' : last_name,
            }

        return render(request, 'accounts/student_edit.html', context)


@login_required
@csrf_exempt
def teacher_edit(request):
        if request.is_ajax():
            category = request.GET.get('category',None)
            category_list = request.GET.get('category_list', None)
            if category_list:
                category_list = list(LearnCategory.objects.all().values())
                return JsonResponse(category_list, safe=False)
            syll = list(Syllabus.objects.filter(learn_category=category).values())
            return JsonResponse(syll,safe=False)
        else:
            teacher_edit_form = TeacherEditForm()
            cities = list(City.objects.all().values())
            price_ranges=list(PriceRange.objects.all().values())
            # languages=list(Language.objects.all().values())
            categories=list(LearnCategory.objects.all().values())
            syllabuses = list(Syllabus.objects.all().values())
            first_name = None
            last_name = None
            teacher_profile= None
            error = ''
            if hasattr(request.user, 'teacher'):
                teacher_profile = Teacher.objects.get(user_id=request.user.id)
                teacher_edit_form = TeacherEditForm( instance=teacher_profile)
                error = str(request.user)+" "+'خوش آمدید'
                if request.method == 'POST':
                    teacher_edit_form = TeacherEditForm(request.POST, request.FILES,instance=teacher_profile)
                    if teacher_edit_form.is_valid():
                        teacher_edit_form.user = request.user
                        teacher_edit_form.pk = teacher_profile.id
                        teacher = teacher_edit_form.save(commit=False)
                        teacher.is_confirmed = False
                        teacher.save()
                        error = "مشخصات شما با موفقیت تغییر کرد. نتیجه بررسی از طریق پیامک به اطلاع شما خواهد رسید"
                        clerk_phone = '09361164819'
                        teacher_user_id = request.user.id
                        teacher_requested = MyUser.objects.get(id=request.user.id)
                        teacher_email = request.user.username
                        teacher_phone = teacher_requested.phone_number
                        sms_token = 'user_id:{},name:{}'.format(teacher_user_id, teacher.last_name)
                        sms_token2 = teacher_phone
                        sms_token3 = teacher_email
                        send_sms_teacher_edit(clerk_phone,sms_token, sms_token2,sms_token3)
                        # if os.path.isfile(teacher_profile.sample_video.path) :
                        #     os.remove(teacher_profile.sample_video.path)
                        # if os.path.isfile(teacher_profile.image.path) :
                        #     os.remove(teacher_profile.image.path)
                        # if os.path.isfile(teacher_profile.degree_image.path):
                        #     os.remove(teacher_profile.degree_image.path)
                        # if os.path.isfile(teacher_profile.national_card_image.path) :
                        #     os.remove(teacher_profile.national_card_image.path)

                    else :
                         error = " خطا !  لطفا ورودی ها را کنترل کنید و دوباره سعی کنید"
            elif hasattr(request.user, 'student'):
                return HttpResponse("مشخصات شما به عنوان دانش آموز ثبت شده لطفا با نام کاربری دیگری به عنوان معلم ثبت نام کنید ")
            if request.method == 'POST' and hasattr(request.user, 'teacher') == False:

                    teacher_edit_form = TeacherEditForm(request.POST, request.FILES)
                    if teacher_edit_form.is_valid():
                        teacher = teacher_edit_form.save(commit=False)
                        teacher.user = request.user
                        teacher.save()
                        error = "مشخصات شما ثبت شد. نتیجه بررسی از طریق پیامک به اطلاع شما خواهد رسید"
                        teacher_profile = request.user

                        clerk_phone = '09361164819'
                        teacher_user_id = request.user.id
                        teacher_requested = MyUser.objects.get(id=request.user.id)
                        teacher_email = request.user.username
                        teacher_phone = teacher_requested.phone_number
                        sms_token = 'user_id:{},name:{}'.format(teacher_user_id, teacher.last_name)
                        sms_token2 = teacher_phone
                        sms_token3 = teacher_email
                        send_sms_teacher_edit(clerk_phone, sms_token, sms_token2, sms_token3)
                    else:
                        error = 'ورودی ها دقیق نیست لطفا دوباره سعی کنید'

            context = {
                'teacher_profile' : teacher_profile,
                'teacher_edit_form': teacher_edit_form,
                'error': error,
                'cities': cities,
                'price_ranges' : price_ranges,
                # 'teacher_edited' : teacher_edited,
                'categories' : categories,
                'syllabuses' : syllabuses,
                'first_name' : first_name,
                'last_name' : last_name,
                }
            return render(request, 'accounts/teacher_edit.html', context)


def search_view(request):
    results = []
    results_teachers =[]
    search_message = None
    if request.method == "GET":
        search_query = request.GET.get('search_text',None)
        if search_query:
            result1 = Syllabus.objects.filter(syllabus__icontains= search_query)
            result1_teachers = Teacher.objects.filter(syllabus__syllabus_name__contains=search_query,is_confirmed=True)
            result2 = LearnCategory.objects.filter(category_name__icontains=search_query)
            result2_teachers = Teacher.objects.filter(category__category__contains=search_query,is_confirmed=True)

            result3_teachers = Teacher.objects.filter(Q(last_name__icontains=search_query,is_confirmed=True)|Q(first_name__icontains=search_query,is_confirmed=True))
            results = list(chain(result1, result2, ))
            results_teachers = list(chain(result1_teachers,result2_teachers,result3_teachers ))
            if  results_teachers :
                search_message = str(len(results_teachers)) + "استاد پیدا شد"
            else:
                search_message = "موردی یافت نشد"
        return render(request, 'accounts/index.html', {'results': results, 'search_message': search_message,'results_teachers': results_teachers})


def user_verify(request):
    response = {}
    if request.method == 'POST':
        user_verified = None
        otp_code = None
        mobile_number = None
        if 'input_mobile' in request.POST:
            mobile_number = request.POST.get('input_mobile')
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
            if otp_code == veri_code_input:
                mobile_number = request.POST.get('mobile_number')
                user_verified = 'code_checked'
                user_create_form = MyUserCreate()
                user_create_form.fields['phone_number'].initial = mobile_number
                # user_create_form.phone_number = mobile_number
                user_saved = None
                context = {
                    'user_saved':user_saved,
                    'user_create_form':user_create_form,
                    'user_verified':user_verified,
                    'mobile_number': mobile_number,
                }
                return render(request, 'accounts/user_create.html', context)
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
     }
    return render(request, 'accounts/user_verify.html', context )


def pass_reset(request):
    error = None
    user_verified = None
    otp_code = None
    mobile_number = None
    if request.method == 'POST':
        if 'input_mobile' in request.POST:
            mobile_number = request.POST.get('input_mobile')
            response = send_otp(mobile_number)
            if response[0]['status'] == 5:
                user_verified = 'code_sent'
                otp_code = response[1]
            else:
                user_verified = 'code_not_sent'
                otp_code = None
        if 'veri_code_input' in request.POST and 'mobile_number' in request.POST:
            otp_code = request.POST.get('otp_code_generated')
            veri_code_input = request.POST.get('veri_code_input')
            if otp_code == veri_code_input:
                mobile_number = request.POST.get('mobile_number')
                user =MyUser.objects.filter(phone_number=mobile_number,)
                if not user:
                    error = 'چنین کاربری وجود ندارد لطفا دوباره شماره خود را وارد کنید'
                    return render(request, 'accounts/user_verify.html',{'error':error})
                user_verified = 'code_checked'
                user_create_form = MyUserCreate()
                user_create_form.fields['phone_number'].initial = mobile_number
                # user_create_form.fields['username'].initial = user_email
                reset_pass_request = True
                context = {
                    'user_verified': user_verified,
                    'otp_code': otp_code,
                    'reset_pass_request': reset_pass_request,
                    'mobile_number': mobile_number,
                    'user_create_form': user_create_form,
                }
                return render(request,'accounts/user_create.html',context)
    context = {
        'user_verified':user_verified,
        'otp_code':otp_code,
        'mobile_number':mobile_number,
    }
    return render(request,'accounts/user_verify.html',context)


def pass_reset_confirmed(request):
        mobile_number =request.POST.get('phone_number')
        entered_email =request.POST.get('username')
        user = MyUser.objects.get(phone_number=mobile_number)
        user_email = getattr(user,'username')
        if entered_email == user_email:
            new_password = request.POST.get('password1')
            user.set_password(new_password)
            user.save()
            login(request, user)
        else:
            return HttpResponse('ایمیل وارد شده با شماره همراه مطابق نیست')
        return render(request, 'accounts/pass_reset-confirmed.html',{})

def site_laws(request):
    return render(request,'accounts/sit_laws.html',{})