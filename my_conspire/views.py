from django.shortcuts import render

# Create your views here.

def welcome(request):
    title='welcome'
    return render(request, 'welcome.html', locals())
