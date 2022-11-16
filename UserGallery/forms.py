from allauth.account.forms import SignupForm
from django import forms
from .models import Video

class SimpleSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    demo = forms.CharField(max_length=100, label='test')

    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.demo = self.cleaned_data['demo']
        user.save()
        return user

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class AddvideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']


class SearchvideoForm(forms.Form):
    search_term = forms.CharField(max_length=255, label="Search for videos")
