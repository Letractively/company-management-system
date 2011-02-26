#mid views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet
from mid.models import Room

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.models import User
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
                        
                        return HttpResponseRedirect('switchboard')
                                            
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
def renderSwitchboard(request) :
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha = alpha)
    cMid = cMid[0]
                        
    lBillets = Billet.objects.filter(mid = cMid)
                        
    #Here we assign permissions based on billets.
    flagAdmin = False;
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True
    
    return render_to_response('mid/switchboard.html', { 'mid' : cMid,
                                                        'admin' : flagAdmin },
                                                        context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def logOut(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(redirect_field_name='/')
def selectPassChange(request):
    
    return render_to_response('mid/selectPassChange.html', { },
                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')    
def passChange(request) :
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    password = request.POST['password']
    
    cUser = request.user    
    cUser.set_password(password)
    cUser.save()
    
    return HttpResponseRedirect('selectPassChange')

#Following functions deal with the Admin Officer functionality
@login_required(redirect_field_name='/')
def selectUser(request):
    #Called on /mid/addUser -> polls data, adds both Mid and User objects to the database
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.order_by('alpha')
    
    return render_to_response('mid/selectUser.html', { 'lMids' : lMids },
                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def modifyUser(request):
    #Called on /mid/modifyUser -> creates a form for edit/addition of the new user
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    alpha = request.POST['alpha']
    
    if alpha == '000000' :
        cMid = None
    else :
        cMid = Mid.objects.filter(alpha = alpha)
        cMid = cMid[0]
        
    lRooms = Room.objects.order_by('roomNumber')
    
    return render_to_response('mid/modifyUser.html', { 'cMid' : cMid, 'lRooms' : lRooms, },
                              context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')    
def saveUser(request) :
    #Saves a new user/Edits a preexisting user
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    newUser = request.POST['newUser']
    roomNumber = request.POST['roomNumber']
    roomNumber = Room.objects.filter(roomNumber = roomNumber)
    roomNumber = roomNumber[0]
    
    #Making sure user with this alpha does not exist
    lMids = Mid.objects.all()
    
    alphaExists = False
    for p in lMids :
        if p.alpha == alpha :
            alphaExists = True
    
    if newUser == "false" :
        cMid = Mid.objects.filter(alpha = alpha)
        cMid = cMid[0]
        
        cMid.LName=request.POST['lName'] 
        cMid.mName=request.POST['mName']
        cMid.fName = request.POST['fName']
        cMid.roomNumber = roomNumber
        cMid.phoneNumber = request.POST['phoneNumber']
        cMid.weekends = request.POST['weekends']
        cMid.save()
               
    if newUser == "true" and not alphaExists:
        cMid = Mid(alpha=request.POST['alpha'],
                   LName=request.POST['lName'],
                   mName=request.POST['mName'],
                   fName = request.POST['fName'],
                   roomNumber = roomNumber,
                   phoneNumber = request.POST['phoneNumber'],
                   weekends = request.POST['weekends'], 
                   #acSAT = True,
                   #PRTSat = True,
                   CQPR = "0.00",
                   SQPR = "0.00",
                   performanceGrade = "N",
                   conductGrade = "N",
                   PRT = "00.0")
        cMid.save()
        
        cUser = User.objects.create_user('m'+alpha, 'm'+alpha+'@usna.edu', alpha)
        cUser.first_name = fName
        cUser.last_name = lName
        cUser.is_staff = False
        cUser.save()
        
    return HttpResponseRedirect('selectUser')

@login_required(redirect_field_name='/')
def selectPassReset(request):
    #Called on /mid/selectPassReset
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.order_by('alpha')
    
    return render_to_response('mid/selectPassReset.html', { 'lMids' : lMids },
                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')    
def passReset(request) :
    #Resets user's password to his alpha
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    alpha = request.POST['alpha']
    
    cUser = User.objects.filter(username='m'+alpha)
    cUser = cUser[0]
    cUser.set_password(alpha)
    cUser.save()
    
    return HttpResponseRedirect('selectPassReset')
