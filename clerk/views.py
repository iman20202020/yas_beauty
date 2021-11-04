from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import TeacherEditForm
from accounts.models import LearnCategory, Syllabus, City, PriceRange, Teacher

def index_clerk(request):
    return HttpResponse('welcome')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff == True:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
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
            syllabuses = None
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
                        # if os.path.isfile(teacher_profile.sample_video.path) :
                        #     os.remove(teacher_profile.sample_video.path)
                        # if os.path.isfile(teacher_profile.image.path) :
                        #     os.remove(teacher_profile.image.path)
                        # if os.path.isfile(teacher_profile.degree_image.path):
                        #     os.remove(teacher_profile.degree_image.path)
                        # if os.path.isfile(teacher_profile.national_card_image.path) :
                        #     os.remove(teacher_profile.national_card_image.path)
                        teacher.save()
                        error = "مشخصات شما با موفقیت تغییر کرد. نتیجه بررسی از طریق پیامک به اطلاع شما خواهد رسید"

                    else :
                         error = " خطا !  لطفا ورودی ها را کنترل کنید و دوباره سعی کنید"
            elif hasattr(request.user, 'student'):
                return HttpResponse("مشخصات شما به عنوان دانش آموز ثبت شده لطفا با نام کاربری دیگری به عنوان معلم ثبت نام کنید ")
            if request.method == 'POST' and hasattr(request.user, 'teacher') == False:
                try:
                    teacher_edit_form = TeacherEditForm(request.POST, request.FILES)
                    if teacher_edit_form.is_valid():
                        teacher = teacher_edit_form.save(commit=False)
                        teacher.user = request.user
                        teacher.save()
                        error = "مشخصات شما ثبت شد. نتیجه بررسی از طریق پیامک به اطلاع شما خواهد رسید"
                        teacher_profile = request.user
                    else:
                        error = 'ورودی ها دقیق نیست لطفا دوباره سعی کنید'
                except:
                    teacher_profile = request.POST
                    error = "لطفا اطلاعات وارد شده را بررسی کنید"
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



