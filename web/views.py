from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from web.models import *
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from web.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    category_list = Category.objects.all()
    article_list = Article.objects.all()
    return render(request,'index.html',locals())


def article(request):
    category_list = Category.objects.all()
    id = request.GET.get('id', None)
    article = Article.objects.get(pk=id)
    return render(request,'article.html',locals())

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密__码',widget=forms.PasswordInput())


def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            user = User.objects.filter(username__exact=username, password__exact=password)
            return render_to_response('index_success.html', {'username': username},RequestContext(request))
        else:
            userform = UserForm()
    else:
        userform = UserForm()
    return render_to_response('login.html', {'userform': userform},RequestContext(request))

def sign(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            User.objects.create(username=username, password=password)
            return render_to_response('index_success.html', {'username': username},RequestContext(request))
        else:
            userform = UserForm()
    else:
        userform = UserForm()
    return render_to_response('sign.html',{'userform': userform},RequestContext(request))

def forgot(request):
    return render_to_response(request,'forgot.html',locals())