from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _


from accounts.models import Student, Teacher, MyUser
from accounts.validators import mobile_validate
from yas7 import settings


class MyUserCreate(UserCreationForm):
    # email = forms.EmailField(required=True, label='ایمیل')
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ("phone_number","username",)
        # field_classes = {'email': UsernameField}

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
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',}),
        strip=False,
        help_text=None,
    )

    phone_number = forms.CharField(required=True,label="شماره همراه", widget=forms.TextInput(attrs={'readonly':'readonly'}) )
    # phone_number.__setattr__('readonly','readonly')


class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user','email']



class TeacherEditForm(UserChangeForm):



    class Meta(UserChangeForm.Meta):
        model = Teacher

        exclude = ['user','email']



