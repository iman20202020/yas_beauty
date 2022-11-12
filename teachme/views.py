from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.models import Teacher, MyUser, ClassRequest, State, Comment
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

    teacher_for_comments = Comment.objects.filter(teacher_id=teacher_id, is_confirmed=True)

    teacher_cat = teacher_selected.category_id
    context = {
        'teacher_selected': teacher_selected,
        'teacher_cat': teacher_cat,
        'teacher_for_comments': teacher_for_comments,
    }
    return render(request, 'teachme/teacher_detail.html', context)


@login_required
def teacher_request_send(request, teacher_id):
    clerk_phone = '09361164819'
    teacher_requested = Teacher.objects.get(id=teacher_id)
    student_user = request.user
    ClassRequest.objects.update_or_create(teacher=teacher_requested, student=student_user)
    teacher_phone = teacher_requested.user.username
    student_phone = student_user.username
    clerk_sms_token = '{},id{}'.format(teacher_requested.last_name, teacher_requested.id)
    clerk_sms_token2 = teacher_phone
    clerk_sms_token3 = student_phone
    send_sms_stu(student_phone, teacher_requested.last_name)
    send_sms_clerk(clerk_phone, clerk_sms_token, clerk_sms_token2, clerk_sms_token3)

    messages.success(request, 'درخواست شما ثبت شد بزودی جهت هماهنگی با شما تماس می گیریم', 'success large')

    return redirect(teacher_requested.get_absolute_url())


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
        teacher_points = teacher.points
        action = request.GET.get('action')
        if teacher_id and action:
            try:
                if action == 'like':
                    teacher_points += 0.01
                    teacher.users_like.add(request.user)
                    teacher.users_dislike.remove(request.user)
                    status = 'like_ok'
                elif action == 'unlike':
                    teacher_points -= 0.01
                    teacher.users_like.remove(request.user)
                    status = 'like_ok'
                elif action == 'dislike':
                    teacher_points -= 0.01
                    teacher.users_dislike.add(request.user)
                    teacher.users_like.remove(request.user)
                    status = 'dislike_ok'
                elif action == 'no_dislike':
                    teacher_points += 0.01
                    teacher.users_dislike.remove(request.user)
                    status = 'dislike_ok'
                else:
                    status = 'error'
                if teacher_points > 5.0:
                    teacher.points = 5.0
                else:
                    teacher.points = teacher_points

                    teacher.save()

                return JsonResponse({'status': status})
            except:
                pass
        return JsonResponse({'status': 'error'})
    else:
        pass


