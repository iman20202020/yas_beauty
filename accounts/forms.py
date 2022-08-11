from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Teacher, MyUser, Comment


class MyUserCreate(UserCreationForm):
    # email = forms.EmailField(required=True, label='ایمیل')
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ("phone_number", "username",)

    def __init__(self, *args, **kwargs):
        super(MyUserCreate, self).__init__(*args, **kwargs)
        # super().__init__(*args, **kwargs)
        # for fieldname in ['username',]:
        #     self.fields[fieldname].help_text = None

    password1 = forms.CharField(
        label="گذر واژه",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=None,
    )
    password2 = forms.CharField(
        label="تکرار گذر واژه",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', }),
        strip=False,
        help_text=None,
    )

    phone_number = forms.CharField(required=True, label="شماره همراه", widget=forms.TextInput(attrs={'readonly':'readonly'}) )


class TeacherEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['user', 'email']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="",required=False, widget=forms.Textarea(
    attrs ={
        'class': 'form-control',
        'placeholder': ' دیدگاه خود را بنویسید',
        'rows': 4,
        'cols': 50,

    }))

    class Meta:
        model = Comment
        fields = ['suggest','content', ]
