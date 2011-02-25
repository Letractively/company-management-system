#mid views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

import re

def loginPage(request):
    return render_to_response('mid/loginPage.html', {}, 
                              context_instance=RequestContext(request))

def logIn(request):
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        
        if user.is_active:
            login(request, user)
            
            if user.username == 'CO' :
                 return render_to_response('mid/co.html', { })
            
            else :
            
                if re.match("m", username) is not None : 
                
                    alpha = username.split('m')
                    alpha = alpha[1]
        
                    if Mid.objects.filter(alpha = alpha) :
                        
                        cMid = Mid.objects.filter(alpha = alpha)
                        cMid = cMid[0]
                        
                        lBillets = Billet.objects.filter(mid = cMid)
                        
                        #Here we assign permissions based on billets.
                        flagAdmin = False;
                        for p in lBillets :
                            if p.billet == "ADM" and p.current :
                                flagAdmin = True
                                            
                        return render_to_response('mid/switchboard.html', { 'mid' : cMid,
                                                                            'admin' : flagAdmin })
                    
                    #Alpha does not exist in the database, redirect to login with 'noUser' flag TRUE.
                    else :
                        return render_to_response('mid/loginPage.html', { 'noUser' : True }, 
                                                  context_instance=RequestContext(request))
                
                #Non 'mXXXXXX' login entered, redirect to login with with the 'noUser' flag TRUE.
                else :
                    return render_to_response('mid/loginPage.html', {'noUser' : True }, 
                                              context_instance=RequestContext(request))
        
        #Disabled account: should not happen, but here just in case
        else:
            return HttpResponseRedirect('/')
        
    #Wrong password, redirect redirect to login with the 'repeat' flag TRUE    
    else:
        return render_to_response('mid/loginPage.html', { 'repeat' : True,}, 
                                  context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def logOut(request):
    logout(request)
    return HttpResponseRedirect('/')
