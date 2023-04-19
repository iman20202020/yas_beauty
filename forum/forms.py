from django import forms
from accounts.models import Syllabus
from forum.models import Post, Comment


class PostCreateForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'عنوان پست', 'dir': 'rtl', 'class': 'form-control'}), label='',)
    author_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام خود را وارد کنید', 'dir': 'rtl', 'class': 'form-control'}), label='',)
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'شرح پست', 'dir': 'rtl', 'class': 'form-control'}), label='',)
    # image = forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'form-control'}), label='اضافه کردن تصویر',)
    syllabus = forms.ModelChoiceField(queryset=Syllabus.objects.all(), widget=forms.Select(attrs={ 'class': 'form-select text-center'}), label='موضوع',)


    class Meta:
        model = Post
        fields = ['author_name', 'title', 'syllabus', 'body', 'post_image', ]


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'نام خود را وارد کنید', 'dir': 'rtl', 'class': 'form-control'}), label='', )
    body = forms.CharField( widget=forms.Textarea(
        attrs={'placeholder': 'شرح', 'dir': 'rtl', 'class': 'form-control'}), label='', )

    class Meta:
        model = Comment
        fields = ['name', 'body']


class SearchForm(forms.Form):
    query = forms.CharField()

