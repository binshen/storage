import json
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import User

def index(request):
    
    return render_to_response('login.html', context_instance=RequestContext(request))


def login(request):
    
    email = request.POST.get("email")
    password = request.POST.get("password")
    
    user_count = User.objects.filter(email = email, password = password).count()
    if user_count > 0:
        request.session['login_email'] = email
        request.session['login_password'] = password
        return HttpResponseRedirect('/store/index/')
    
    return HttpResponseRedirect('/')
    
    
def logout(request):
    
    if 'login_email' in request.session:
        del request.session['login_email']
        
    return HttpResponseRedirect('/')


def store_index(request):
    
    return render_to_response('store/index.html', context_instance=RequestContext(request))


def store_stock(request):
    
    return render_to_response('store/stock.html', context_instance=RequestContext(request))


def store_history(request):
    
    return render_to_response('store/history.html', context_instance=RequestContext(request))


def store_calculate(request):
    
    return render_to_response('store/calculate.html', context_instance=RequestContext(request))


def store_help(request):
    
    return render_to_response('store/help.html', context_instance=RequestContext(request))


def store_account(request):
    
    return render_to_response('store/account.html', { "message" : "Password" }, context_instance=RequestContext(request))


def store_change_password(request):
    
    oldpassword = request.POST.get("oldpassword")
    password = request.POST.get("password")
    repassword = request.POST.get("repassword")
    
    login_email = request.session['login_email']
    login_password = request.session['login_password']
    if password <> repassword:
        message = "Repassword should be the same with password"
    elif oldpassword == login_password:
        user = User.objects.get(email = login_email, password = login_password)
        user.password = password
        user.save()
        message = "Congratulation!"
    else:
        message = "Password is wrong"
    
    return render_to_response('store/account.html', { "message" : message }, context_instance=RequestContext(request))


def store_change_email(request):
    
    email = request.POST.get("email")
    login_email = request.session['login_email']
    login_password = request.session['login_password']
    user = User.objects.get(email = login_email, password = login_password)
    user.email = email
    user.save()
    
    request.session['login_email'] = email
    
    return render_to_response('store/account.html', context_instance=RequestContext(request))


def store_system(request):
    
    return render_to_response('store/system.html', context_instance=RequestContext(request))


def store_data(request):
    
    payload = {}
    return HttpResponse(json.dumps(payload), content_type = "application/json")