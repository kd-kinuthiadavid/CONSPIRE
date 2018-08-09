from django import forms

from my_conspire.models import Profile, Feed, Article, Question, Answer


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

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'profile']


class NewAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['comment']