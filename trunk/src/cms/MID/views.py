from cms.MID.models import Mid
from cms.MID.models import Billets
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
            
            alpha = username.split('m')
            alpha = alpha[1]

            if Mid.objects.filter(Alpha=alpha) :
                
                cMid = Mid.objects.filter(Alpha=alpha)
                cBillets = Billets.objects.all()
                
                return render_to_response('MID/switchboard.html', { 'mid' : cMid, 'b' : cBillets })
            
            #Non 'mXXXXXX' login entered, redirect back to the same page with the 'noUser' flag TRUE.
            else :
                return render_to_response('MID/loginPage.html', { 'repeat' : False,  'noUser' : True }, 
                              context_instance=RequestContext(request))
        
        #Disabled account: should not happen, but here just in case
        else:
            return HttpResponse("Disabled account")
        
    #Wrong password, redirect back to the same page with the 'repeat' flag TRUE    
    else:
        return render_to_response('MID/loginPage.html', { 'repeat' : True }, 
                              context_instance=RequestContext(request))