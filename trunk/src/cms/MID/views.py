from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login

def loginPage(request):
    return render_to_response('MID/loginPage.html', { 'repeat' : False }, 
                              context_instance=RequestContext(request))

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('MID/switchboard.html', {'user': user})
        else:
            return HttpResponse("Disabled account")
    else:
        return render_to_response('MID/loginPage.html', { 'repeat' : True }, 
                              context_instance=RequestContext(request))