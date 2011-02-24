#mid views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import re
#import render_to_response

def loginPage(request):
    return render_to_response('mid/loginPage.html', { 'repeat' : False, 'noUser' : False }, 
                              context_instance=RequestContext(request))

def logIn(request):
    #Safety feature, makes sure we POST data to this view
    #if request.method != "POST" :
        #return HttpResponse("NO POST")
        #return HttpResponseRedirect('/cms/')
    
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        
        if user.is_active:
            login(request, user)
            
            if user.username == 'co' :
                 return render_to_response('mid/co.html', { })
            
            else :
            
                if re.match("m", username) is not None : 
                
                    alpha = username.split('m')
                    alpha = alpha[1]
        
                    if Mid.objects.filter(alpha=alpha) :
                        
                        cMid = Mid.objects.filter(alpha=alpha)
                        cMid = cMid[0]
                                            
                        return render_to_response('mid/switchboard.html', { 'mid' : cMid })
                    
                    #Alpha does not exist in the database, redirect to login with 'noUser' flag TRUE.
                    else :
                        return render_to_response('mid/loginPage.html', { 'repeat' : False,  'noUser' : True }, 
                                                  context_instance=RequestContext(request))
                
                #Non 'mXXXXXX' login entered, redirect to login with with the 'noUser' flag TRUE.
                else :
                    return render_to_response('mid/loginPage.html', { 'repeat' : False,  'noUser' : True }, 
                                              context_instance=RequestContext(request))
        
        #Disabled account: should not happen, but here just in case
        else:
            return HttpResponse("Disabled account.")
        
    #Wrong password, redirect redirect to login with the 'repeat' flag TRUE    
    else:
        return render_to_response('mid/loginPage.html', { 'repeat' : True, 'noUser' : False }, 
                                  context_instance=RequestContext(request))

def passwordRecovery(request):
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/cms/')
    
    username = request.POST['username']
    #sendmail goes here. =)
    
    return HttpResponseRedirect('/cms/')

@login_required(redirect_field_name='/')
def logOut(request):
    logout(request)
    return HttpResponseRedirect('/cms/')
