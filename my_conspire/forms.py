from django import forms

from my_conspire.models import Profile, Feed, Article


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class NewFeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        exclude = ['comment']


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['comment']