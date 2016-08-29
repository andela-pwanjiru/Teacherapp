from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


class UserModelForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if (not password) or (not username):
            raise forms.ValidationError("All fields are required!")

        return self.cleaned_data

    def save(self):
        user = super(UserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user
