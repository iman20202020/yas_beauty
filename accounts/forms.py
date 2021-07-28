from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _


from accounts.models import Student, Teacher
from yas7 import settings


class MyUserCreate(UserCreationForm):
    email = forms.EmailField(required=True, label='ایمیل')

    def __init__(self, *args, **kwargs):
        super(MyUserCreate, self).__init__(*args, **kwargs)

        super().__init__(*args, **kwargs)
        for fieldname in ['username',]:
            self.fields[fieldname].help_text = None
    # error_messages = {
    #      'رمز عبور ها یکسان نیست',
    # }
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
    phone_number = forms.CharField(label="شماره همراه ")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","email","phone_number")
        field_classes = {'username': UsernameField}

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user','email']

        field_classes = {'username': UsernameField}


class TeacherEditForm(UserChangeForm):



    class Meta(UserChangeForm.Meta):
        model = Teacher

        exclude = ['user','email']




    # def clean_content(self):
    #     content = self.cleaned_data['content']
    #     content_type = content.content_type.split('/')[0]
    #     if content_type in settings.CONTENT_TYPES:
    #         if content._size > settings.MAX_UPLOAD_SIZE:
    #             raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
    #                 filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
    #     else:
    #         raise forms.ValidationError(_('File type is not supported'))
    #     return content
