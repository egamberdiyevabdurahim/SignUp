from django import forms

from .models import User


class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username', 'password', 'phone', 'photo']

	def save(self, commit=True):
		user=super().save(commit)
		user.set_password(self.cleaned_data['password'])
		user.save()
		return user


class SigninForm(forms.Form):
	username=forms.CharField(max_length=20)
	password=forms.CharField(max_length=25)