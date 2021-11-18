from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import TeacherEditForm
from accounts.models import LearnCategory, Syllabus, City, PriceRange, Teacher

#

def show_blog(request, blog_num):
    blog_template = 'blog'+ str(blog_num)+'.html'
    return render(request, blog_template, {})

