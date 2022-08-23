from itertools import chain

from django.contrib import messages
from django.shortcuts import redirect

from accounts import phone_vrify
from accounts.otp import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from accounts.forms import MyUserCreate, TeacherEditForm, CommentForm
from accounts.models import LearnCategory, Syllabus, PriceRange, Teacher, City, MyUser, State, Comment, Student


def base_view(request):
    return render(request, 'accounts/_base.html', {})



def index_accounts(request):
    teacher_university_count = Teacher.objects.filter(category='دانشگاهی',is_confirmed=True).count()
    teacher_high_school_count = Teacher.objects.filter(category='متوسطه دوم',is_confirmed=True).count()
    teacher_mid_school_count = Teacher.objects.filter(category='متوسطه اول',is_confirmed=True).count()
    teacher_primary_school_count = Teacher.objects.filter(category='دبستان',is_confirmed=True).count()
    teacher_computer_count = Teacher.objects.filter(category='کامپیوتر',is_confirmed=True).count()
    teacher_music_count = Teacher.objects.filter(category='موسیقی',is_confirmed=True).count()
    teacher_art_count = Teacher.objects.filter(category='هنرهای تجسمی',is_confirmed=True).count()
    teacher_sport_count = Teacher.objects.filter(category='ورزش و بدنسازی',is_confirmed=True).count()
    teacher_cinema_count = Teacher.objects.filter(category='سینما و بازیگری',is_confirmed=True).count()
    teacher_tech_count = Teacher.objects.filter(category='کارهای فنی',is_confirmed=True).count()
    teacher_cooking_count = Teacher.objects.filter(category='آشپزی',is_confirmed=True).count()
    teacher_makeup_count = Teacher.objects.filter(category='آرایش و زیبایی',is_confirmed=True).count()
    teacher_language_count = Teacher.objects.filter(category='زبان های خارجی',is_confirmed=True).count()
    teacher_bests = Teacher.objects.all().order_by('-points')[:10]
    teachers = teacher_bests

    context = {
        'teacher_university_count': teacher_university_count,
        'teacher_high_school_count': teacher_high_school_count,
        'teacher_mid_school_count': teacher_mid_school_count,
        'teacher_sport_count': teacher_sport_count,
        'teacher_music_count': teacher_music_count,
        'teacher_art_count': teacher_art_count,
        'teacher_computer_count': teacher_computer_count,
        'teacher_primary_school_count': teacher_primary_school_count,
        'teacher_cinema_count': teacher_cinema_count,
        'teacher_tech_count': teacher_tech_count,
        'teacher_cooking_count': teacher_cooking_count,
        'teacher_makeup_count': teacher_makeup_count,
        'teacher_language_count': teacher_language_count,
        'teachers': teachers,
    }
    return render(request, 'accounts/index.html', context)


def beauty_trainings(request):
    teacher_counts = []
    teachers = Teacher.objects.filter(category='آرایش و زیبایی', is_confirmed=True).order_by('-points')[:15]
    syllabuses_makeup = Syllabus.objects.filter(learn_category='آرایش و زیبایی')
    for syllabus in syllabuses_makeup:
        teacher_count = Teacher.objects.filter(category='آرایش و زیبایی', syllabus_id=syllabus, is_confirmed=True).count()
        if teacher_count is not 0:
            teacher_counts.append([syllabus,teacher_count])
    context = {
        'syllabuses_makeup': syllabuses_makeup,
        'teacher_counts': teacher_counts,
        'teachers': teachers,
    }
    return render(request, 'accounts/beauty-trainings.html', context)


def high_school_trainings(request):
    teacher_counts = []
    teachers = Teacher.objects.filter(category='متوسطه دوم', is_confirmed=True ).order_by('-points')[:15]
    syllabuses_high_school = Syllabus.objects.filter(learn_category_id='متوسطه دوم')
    for syllabus in syllabuses_high_school:
        teacher_count = Teacher.objects.filter(category='متوسطه دوم', syllabus_id=syllabus, is_confirmed=True).count()
        if teacher_count is not 0:
            teacher_counts.append([syllabus,teacher_count])
    context = {
        'syllabuses_high_school': syllabuses_high_school,
        'teacher_counts': teacher_counts,
        'teachers': teachers,
    }
    return render(request, 'accounts/high_school_trainings.html', context)


def mid_school_trainings(request):
    teacher_counts = []
    teachers = Teacher.objects.filter(category='متوسطه اول', is_confirmed=True ).order_by('-points')[:15]
    syllabuses_mid_school = Syllabus.objects.filter(learn_category_id='متوسطه اول')
    for syllabus in syllabuses_mid_school:
        teacher_count = Teacher.objects.filter(category='متوسطه اول', syllabus_id=syllabus, is_confirmed=True).count()
        if teacher_count is not 0:
            teacher_counts.append([syllabus,teacher_count])
    context = {
        'syllabuses_mid_school': syllabuses_mid_school,
        'teacher_counts': teacher_counts,
        'teachers': teachers,
    }
    return render(request, 'accounts/mid_school_trainings.html', context)



def music_trainings(request):
    teacher_counts = []
    teachers = Teacher.objects.filter(category='موسیقی', is_confirmed=True ).order_by('-points')[:15]
    syllabuses_music = Syllabus.objects.filter(learn_category_id='موسیقی')
    for syllabus in syllabuses_music:
        teacher_count = Teacher.objects.filter(category='موسیقی', syllabus_id=syllabus, is_confirmed=True).count()
        if teacher_count is not 0:
            teacher_counts.append([syllabus,teacher_count])
    context = {
        'syllabuses_music': syllabuses_music,
        'teacher_counts': teacher_counts,
        'teachers': teachers,
    }
    return render(request, 'accounts/music-trainings.html', context)


def language_trainings(request):
    teacher_counts = []
    teachers = Teacher.objects.filter(category='زبان های خارجی', is_confirmed=True ).order_by('-points')[:15]
    syllabuses_language = Syllabus.objects.filter(learn_category_id='زبان های خارجی')
    for syllabus in syllabuses_language:
        teacher_count = Teacher.objects.filter(category='زبان های خارجی', syllabus_id=syllabus, is_confirmed=True).count()
        if teacher_count is not 0:
            teacher_counts.append([syllabus,teacher_count])
    context = {
        'syllabuses_language': syllabuses_language,
        'teacher_counts': teacher_counts,
        'teachers': teachers,
    }
    return render(request, 'accounts/language-trainings.html', context)


def contact_us(request):
    return render(request, 'accounts/contact_us.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index_accounts'))


@login_required
def profile_edit(request):
    if hasattr(request.user, 'teacher'):
        return HttpResponseRedirect(reverse('accounts:teacher_edit'))
    else:
        return HttpResponseRedirect(reverse('accounts:index_accounts'))




@login_required
@csrf_exempt
def teacher_edit(request):
        if request.is_ajax():
            if 'category' in request.GET :
                category = request.GET.get('category',None)
                category_list = request.GET.get('category_list', None)
                if category_list:
                    category_list = list(LearnCategory.objects.all().values())
                    return JsonResponse(category_list, safe=False)
                syll = list(Syllabus.objects.filter(learn_category=category).values())
                return JsonResponse(syll, safe=False)
            if 'state' in request.GET:
                state = request.GET.get('state', None)
                state_list = request.GET.get('state_list', None)
                if state_list:
                    state_list = list(State.objects.all().values())
                    return JsonResponse(state_list, safe=False)
                city = list(City.objects.filter(state=state).values())
                return JsonResponse(city,safe=False)

        else:
            teacher_edit_form = TeacherEditForm()
            cities = list(City.objects.all().values())
            states = list(State.objects.all().values())
            price_ranges=list(PriceRange.objects.all().values())
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
                    # national_id_entered = teacher_edit_form.data['national_id']
                    # if is_valid_iran_code(national_id_entered):
                    if teacher_edit_form.is_valid():
                        teacher_edit_form.user = request.user
                        teacher_edit_form.pk = teacher_profile.id
                        teacher = teacher_edit_form.save(commit=False)
                        # teacher.slug = f"{teacher.syllabus}-{teacher.last_name}"
                        teacher.save()

                        error = "مشخصات شما با موفقیت تغییر کرد.پس از بررسی در سایت قرار می گیرد"
                        clerk_phone = '09361164819'
                        teacher_user_id = request.user.id
                        teacher_requested = MyUser.objects.get(id=request.user.id)
                        teacher_email = request.user.username
                        teacher_phone = teacher_requested.username
                        sms_token = 'user_id:{},name:{}'.format(teacher_user_id, teacher.last_name)
                        sms_token2 = teacher_phone
                        sms_token3 = teacher_email
                        send_sms_teacher_edit(clerk_phone,sms_token, sms_token2,sms_token3)

                    else :
                         error = "خطا:"
                    # else:
                    #     error = " شماره ملی معتبر نیست"

            if request.method == 'POST' and hasattr(request.user, 'teacher') == False:
                teacher_edit_form = TeacherEditForm(request.POST, request.FILES)
                # national_id_entered = teacher_edit_form.data['national_id']
                # if is_valid_iran_code(national_id_entered):
                if teacher_edit_form.is_valid():
                    teacher = teacher_edit_form.save(commit=False)
                    teacher.user = request.user
                    # teacher.slug = f"{teacher.syllabus}-{teacher.last_name}"
                    teacher.save()
                    error = "مشخصات شما ثبت شد.پس از بررسی در سایت قرار می گیرد"
                    teacher_profile = Teacher.objects.get(user_id=request.user.id)
                    clerk_phone = '09361164819'
                    teacher_user_id = request.user.id
                    teacher_requested = MyUser.objects.get(id=request.user.id)
                    teacher_email = request.user.username
                    teacher_phone = teacher_requested.username
                    sms_token = 'user_id:{},name:{}'.format(teacher_user_id, teacher.last_name)
                    sms_token2 = teacher_phone
                    sms_token3 = teacher_email
                    send_sms_teacher_edit(clerk_phone, sms_token, sms_token2, sms_token3)
                else:
                    error = 'خطای فرم:'


            context = {
                'teacher_profile' : teacher_profile,
                'teacher_edit_form': teacher_edit_form,
                'error': error,
                'cities': cities,
                'states': states,
                'price_ranges' : price_ranges,
                # 'teacher_edited' : teacher_edited,
                'categories' : categories,
                'syllabuses' : syllabuses,
                'first_name' : first_name,
                'last_name' : last_name,
                }
            return render(request, 'accounts/teacher_edit.html', context)


@login_required
def comment_view(request, teacher_id,):
    if request.method == 'POST':
        teacher = Teacher.objects.get(id=teacher_id)
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            content = request.POST.get('content')
            suggest = request.POST.get('suggest')
            if Comment.objects.filter(teacher_id=teacher_id,user_commenter_id=request.user.id).exists():
                messages.error(request,'برای هر استاد فقط یک بار می توانید نظر دهید', 'danger')
                return redirect(reverse('teachme:teacher_detail', None, args=(teacher_id,)))
            else:

                comment = Comment.objects.create(teacher=teacher, content=content, user_commenter=request.user, suggest=suggest)
                # teacher.comment_num += 1
                comment.save()
                if suggest == '1':
                        teacher.likes += 1

                if suggest == '2':
                    teacher.dislikes += 1
                if content or suggest == '1' or suggest == '2':
                    teacher_point = teacher.points+((teacher.likes-teacher.dislikes)/100/(teacher.dislikes+teacher.likes))
                    teacher_point = round(teacher_point, 2)
                    if teacher_point < 5:
                        teacher.points = teacher_point
                teacher.save()
                messages.success(request, 'نظر شما ثبت شد ', 'success')
                return redirect(reverse('teachme:teacher_detail', None, args=(teacher_id, )))
    else:
        cf = CommentForm()

    context = {
        'comment_form': cf,

    }
    return render(request, 'accounts/comment_detail.html', context)


def search_view(request):
    results = []
    results_teachers =[]
    search_message = None
    if request.method == "GET":
        search_query = request.GET.get('search_text',None)
        if search_query:
            result1 = Syllabus.objects.filter(syllabus__contains= search_query)
            result1_teachers = Teacher.objects.filter(syllabus__syllabus_name__contains=search_query,is_confirmed=True)
            result2 = LearnCategory.objects.filter(category_name__contains=search_query)
            result2_teachers = Teacher.objects.filter(category__category__contains=search_query,is_confirmed=True)

            result3_teachers = Teacher.objects.filter(Q(last_name__contains=search_query,is_confirmed=True)|Q(first_name__contains=search_query,is_confirmed=True)|Q(qualification__contains=search_query,is_confirmed=True))
            results = list(chain(result1, result2, ))
            results_teachers = list(chain(result1_teachers,result2_teachers,result3_teachers ))
            if  results_teachers :
                search_message = str(len(results_teachers)) + "استاد پیدا شد"
            else:
                search_message = "موردی یافت نشد"
        return render(request, 'accounts/index.html', {'results': results, 'search_message': search_message,'results_teachers': results_teachers})


def user_verify(request):
    return redirect(reverse('accounts:login_view'))


def login_view(request):
    teacher_id = None
    response = {}
    logout(request)
    if 'teacher_selected_id' in request.POST:
        teacher_id = request.POST.get('teacher_selected_id')

    if request.method == 'POST':
        user_verified = None
        otp_code = None
        mobile_number = None
        # my_next = request.POST.get('my_next')

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
                user_verified = 'code_checked'
                user_exists = MyUser.objects.filter(username=mobile_number).exists()

                if user_exists:
                    user = MyUser.objects.get(username=mobile_number)
                    user.set_password(otp_code)
                    user.save()

                else:
                    user = MyUser.objects.create(username=mobile_number, password=otp_code, )

                login(request,user)
                # user_create_form = MyUserCreate()
                # user_create_form.fields['phone_number'].initial = mobile_number

                user_saved = None
                # my_next = request.POST.get('my_next2')
                context = {
                    'user_saved':user_saved,
                    # 'user_create_form':user_create_form,
                    'user_verified':user_verified,
                    'mobile_number': mobile_number,
                    'teacher_id': teacher_id,
                    # 'my_next': my_next
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
     'teacher_id': teacher_id,
     # 'my_next': my_next
     }
    return render(request, 'accounts/user_verify.html', context )


def pass_reset(request):
    this_user = None
    if request.method == 'POST':
        if 'pass_1' in request.POST:
            pass_1 = request.POST.get('pass_1')
            pass_2 = request.POST.get('pass_2')
            if pass_1 == pass_2:

                mobile_number = request.POST.get('mobile_number')
                if len(mobile_number) == 10:
                    mobile_number = '0' + mobile_number
                if mobile_number:
                    user = MyUser.objects.get(phone_number=mobile_number)
                    user.set_password(pass_1)
                    user.save()
                    login(request, user)
                    messages.success(request, 'رمزعبور با موفقیت تغییر یافت', 'success')
                    return redirect(reverse('accounts:index_accounts'))
            else:
                messages.error(request, 'رمز عبور با تکرار آن مطابق نیست','danger')
        if 'input_mobile' in request.POST:
            mobile_number = request.POST.get('input_mobile')
        elif 'mobile_number' in request.POST:
            mobile_number = request.POST.get('mobile_number')
        else:
            mobile_number = None
        if len(mobile_number) == 10:
            mobile_number = '0' + mobile_number
        this_user = MyUser.objects.filter(phone_number=mobile_number, )
        if this_user:
            if 'veri_code_input' in request.POST and 'otp_code_generated' in request.POST:
                veri_code_input = request.POST.get('veri_code_input')
                otp_code = request.POST.get('otp_code_generated')
                user_verified = 'code_checked'
                if phone_vrify.code_otp_check(otp_code, veri_code_input):
                    return render(request, 'accounts/pass_reset.html', {'this_user': this_user, 'phone_number': mobile_number})
                else:
                    user_verified = 'code_check_error'
            else:

                otp_code = phone_vrify.code_send(mobile_number)
                user_verified = 'code_sent'

                
            context = {
                'mobile_number': mobile_number,
                'user_verified': user_verified,
                'otp_code': otp_code,
            }
            return render(request,'accounts/user_verify.html',context)
        else:
            messages.error(request, 'کاربری با این شماره همراه موجود نیست', 'danger')


    return render(request, 'accounts/pass_reset.html', {'this_user': this_user})



def site_laws(request):
    return render(request,'accounts/sit_laws.html',{})

def how_use(request):
    return render(request,'accounts/how_use.html',{})


def how_use2(request):
    return render(request,'accounts/how_use2.html',{})


def teacher_laws(request):
    return render(request,'accounts/teacher_laws.html',{})

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
        # 'teacher_id': teacher_id,
    }
    return render(request, 'accounts/user_verify.html',context)
