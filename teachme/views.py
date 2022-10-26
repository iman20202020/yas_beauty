from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.models import Teacher, MyUser, ClassRequest, Student, State, Comment

from teachme.send_sms import *
from accounts import phone_vrify


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


def teacher_detail(request, teacher_id, slug):

    teacher_selected = Teacher.objects.get(pk=teacher_id)

    # teacher_likes = teacher_selected.likes
    # teacher_dislikes = teacher_selected.dislikes
    teacher_for_comments = Comment.objects.filter(teacher_id=teacher_id, is_confirmed=True)

    teacher_cat = teacher_selected.category_id
    context = {
        'teacher_selected': teacher_selected,
        'teacher_cat': teacher_cat,
        # 'teacher_likes': teacher_likes,
        # 'teacher_dislikes': teacher_dislikes,
        'teacher_for_comments': teacher_for_comments,
    }
    return render(request, 'teachme/teacher_detail.html', context)



def teacher_requst_send(request, teacher_id):
    context = {'teacher_id': teacher_id,}
    return render(request, 'teachme/request_user_verify.html', context)


def request_user_verify(request, teacher_id):

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
                teacher_requested = Teacher.objects.get(id=teacher_id)
                student_object = Student.objects.create(student_phone=mobile_number,)
                student_object.save()
                class_request = ClassRequest.objects.create(
                    teacher=teacher_requested,
                    student=student_object,
                    # teacher_email=teacher_requested.user.username,
                    # student_email=student_object.student_email,
                    teacher_phone=teacher_requested.user.username,
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
                teacher_phone = teacher_requested_user_params.username

                student_phone = mobile_number
                clerk_sms_token = '{},uid{}'.format(teacher_requested.last_name, teacher_requested_user_id)
                clerk_sms_token2 = teacher_phone
                clerk_sms_token3 = student_phone
                send_sms_stu(student_phone, teacher_requested.last_name)
                send_sms_clerk(clerk_phone, clerk_sms_token, clerk_sms_token2, clerk_sms_token3)
                messages.success(request, 'درخواست شما ثبت شد بزودی جهت هماهنگی با شما تماس می گیریم', 'success')
                user_verified = 'code_sent'
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
     'teacher_id': teacher_id,
     }
    return render(request, 'teachme/request_user_verify.html', context )


# create pages for direct search
def nail_implants(request):
    teachers = Teacher.objects.filter(syllabus='کاشت ناخن',is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/nail_implants.html', context)


def eyebrow_microblading_training(request):
    teachers = Teacher.objects.filter(syllabus='آرایش دائم ابرو چشم و لب',is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/eyebrow-microblading-training.html', context)


def eyebrow_lift_training(request):
    teachers = Teacher.objects.filter(syllabus='آرایش دائم ابرو چشم و لب',is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/eyebrow-lift-training.html', context)


def eyebrow_permanent_makeup_training(request):
    teachers = Teacher.objects.filter(syllabus='آرایش دائم ابرو چشم و لب',is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/permanent-makeup-training.html', context)


def haircut_training(request):
    teachers = Teacher.objects.filter(syllabus='کوتاهی موی بانوان',is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/haircut-training.html', context)

def hair_coloring_training(request):
    teachers = Teacher.objects.filter(syllabus='آموزش رنگ و مش مو',is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/hair-coloring-training.html', context)

def face_balancing_training(request):
    teachers = Teacher.objects.filter(syllabus='میکاپ',is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/face-balancing-training.html', context)

def extension_training_for_eylashes(request):
    teachers = Teacher.objects.filter(syllabus='کاشت مژه',is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/extension-training-for-eyelashes.html', context)

def face_cleaning_training(request):
    teachers = Teacher.objects.filter(syllabus='پاکسازی پوست',is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/face-cleaning-training.html', context)


def hair_dress_training(request):
    teachers = Teacher.objects.filter(syllabus='شینیون و بافت مو', is_confirmed=True).reverse().order_by('points')
    states = State.objects.all()
    state_filter = request.GET.get('st')
    if state_filter:
        teachers = teachers.filter(state=state_filter)
    context = {
        'teachers': teachers,
        'state_filter': state_filter,
        'states': states,
    }
    return render(request, 'teachme/hair-dress-training.html', context)




def like_view(request):


    if request.is_ajax():
        teacher_id = request.GET.get('id')
        teacher = Teacher.objects.get(id=teacher_id)
        action = request.GET.get('action')
        if teacher_id and action:
            try:
                # teacher = Teacher.objects.get(id=teacher_id)
                if action == 'like':
                    teacher.users_like.add(request.user)
                    teacher.users_dislike.remove(request.user)
                    status = 'like_ok'
                elif action == 'unlike':
                    teacher.users_like.remove(request.user)
                    status = 'like_ok'
                elif action == 'dislike':
                    teacher.users_dislike.add(request.user)
                    teacher.users_like.remove(request.user)
                    status = 'dislike_ok'
                elif action == 'no_dislike':
                    teacher.users_dislike.remove(request.user)
                    status = 'dislike_ok'
                else:
                    status = 'error'
                likes_count = teacher.users_like.count()
                dislikes_count = teacher.users_dislike.count()
                teacher_point = teacher.points+((likes_count-dislikes_count)/100)
                teacher_point = round(teacher_point, 2)
                if teacher_point < 5.0:
                    teacher.points = teacher_point
                else:
                    teacher.points = 5.0
                teacher.save()

                return JsonResponse({'status': status})
            except:
                pass
        return JsonResponse({'status': 'error'})
    else:
        pass


