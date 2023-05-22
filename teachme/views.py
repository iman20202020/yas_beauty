from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
from hitcount.views import HitCountDetailView
from seo.mixins.views import ViewSeoMixin

from accounts.models import Teacher, ClassRequest, Comment, Syllabus
from teachme.page_titles import set_page_title
from teachme.send_sms import *


class TeacherDetailView(ViewSeoMixin, HitCountDetailView):
    seo_view = 'teacher_detail'
    model = Teacher
    template_name = 'teachme/teacher_detail.html'
    context_object_name = 'teacher'
    slug_field = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        teacher_id = data['object'].id
        teacher_classes = ClassRequest.objects.filter(teacher_id=teacher_id, is_confirmed=True).count()
        teacher_for_comments = Comment.objects.filter(teacher_id=teacher_id, is_confirmed=True)
        data['teacher_selected'] = data['object']
        data['teacher_for_comments'] = teacher_for_comments
        data['teacher_class_count'] = teacher_classes
        return data


@login_required
def comment(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        comment_text = request.POST.get('comment')
        try:
            comment = Comment(teacher=teacher, user_commenter=request.user, name=name, content=comment_text)
            if comment:
                comment.save()
        except:
            ValidationError('')

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


class TeacherList(ViewSeoMixin,TemplateView):
    model = Teacher
    seo_view = 'teacher_list'
    template_name = 'teachme/teachers_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        syllabus = get_object_or_404(Syllabus, syllabus=self.kwargs["syllabus"])
        teachers = Teacher.objects.filter(syllabus=syllabus)
        context["teachers_1"] = teachers[:1]
        context["teachers_2"] = teachers[1:]

        return context





# def teachers_list(request, teachers_syllabus):
#     teachers_1 = Teacher.objects.filter(syllabus=teachers_syllabus, is_confirmed=True).reverse().order_by('points')[:1]
#     teachers_2 = Teacher.objects.filter(syllabus=teachers_syllabus, is_confirmed=True).reverse().order_by('points')[1:]
#     syllabus = get_object_or_404(Syllabus, syllabus=teachers_syllabus)
#     title = set_page_title(teachers_syllabus)
#
#     context = {
#         'teachers_1': teachers_1,
#         'teachers_2': teachers_2,
#         'syllabus': syllabus,
#         'title': title,
#     }
#     return render(request, 'teachme/teachers_list.html', context)


