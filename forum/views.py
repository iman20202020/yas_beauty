from itertools import chain
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, DetailView
from hitcount.views import HitCountDetailView
from seo.mixins.views import ViewSeoMixin, ModelInstanceViewSeoMixin

from accounts.models import Syllabus, Teacher
from forum.forms import PostCreateForm, CommentForm, SearchForm
from forum.models import Post, Comment, CommentContact, Blog


def post_list(request, tag_syllabus=None):
    posts = Post.published.all()
    syllabus = None

    if tag_syllabus:
        posts = posts.filter(syllabus=tag_syllabus)
        syllabus = get_object_or_404(Syllabus, syllabus=tag_syllabus)

    return render(request, 'forum/post/list.html', {'syllabus': syllabus, 'posts': posts})



class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'forum/post/detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        post_syllabus = self.object.syllabus
        similar_posts = self.model.published.filter(syllabus=post_syllabus).exclude(id=self.object.id)
        data['similar_posts'] = similar_posts
        author = self.object.author
        if hasattr(author,'teacher'):
            teacher = get_object_or_404(Teacher, user=author)
            data['teacher'] = teacher
        data['comments'] = self.object.comments.filter(active=True)

        return data


@login_required
def post_create(request):

    if request.method == 'POST':
        post_form = PostCreateForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.slug = slugify(post.title)
            post.author = request.user
            post.save()
            # tags_list = request.POST['tags']
            # post.tags.add(tags_list)
            messages.success(request, 'پست شما ثبت شد . پس از بررسی منتشر خواهد شد ', 'text-center alert-success')


            return render(request, 'forum/post/detail.html', {'post': post})
    else:
        post_form = PostCreateForm()
    return render(request, 'forum/post/create.html', {'post_form': post_form})


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        query = request.GET.get('query')
        search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
        search_query = SearchQuery(query)
        results_title_body = Post.published.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)
                                          ).filter(rank__gte=0.3).order_by('-rank')
        results_name = Post.objects.filter(Q(author_name=query))
        results = list(chain(results_title_body,results_name))
    return render(request, 'forum/base.html', {'form': form, 'query': query, 'results': results})


@require_POST
@login_required
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        post = get_object_or_404(Post, id=post_id)
        if action == 'like':
            post.users_like.add(request.user)
        else:
            post.users_like.remove(request.user)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


@login_required
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    now_commented = False
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            now_commented = True
    else:
        comment_form = CommentForm()

    return render(request, 'forum/base.html', {'comment_form': comment_form, 'now_commented': now_commented, 'post': post, })


@login_required
def comment_comment(request, post_id, comment_id):
    comment_from = get_object_or_404(Comment, id=comment_id, active=True)
    post = get_object_or_404(Post, id=post_id)
    now_commented = False
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_to = comment_form.save(commit=False)
            comment_to.post = post
            comment_to.user = request.user
            comment_to.save()
            CommentContact.objects.get_or_create(comment_from=comment_from, comment_to=comment_to)
            now_commented = True
    else:
        comment_form = CommentForm()

    return render(request, 'forum/base.html', {'comment_form': comment_form, 'now_commented': now_commented, 'post': post, })


class BlogIndexView(ViewSeoMixin, TemplateView):
    seo_view = 'index'
    template_name = 'forum/blog/index.html'

    def get_context_data(self, **kwargs) :
        data = super().get_context_data(**kwargs)
        blogs = Blog.objects.filter(published=True)
        data['blogs'] = blogs

        return data


class BlogDetailView(ModelInstanceViewSeoMixin, DetailView):
    template_name = 'forum/blog/detail.html'
    model = Blog
    pk_url_kwarg = 'id'

