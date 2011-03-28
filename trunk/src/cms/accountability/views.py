#accountability views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet
from accountability.models import Event
from accountability.models import Attendance

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from datetime import date
from datetime import timedelta

import re

@login_required(redirect_field_name='/')
def createEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    cPlatoon = cMid.platoon
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagFSGT = False
    for p in lBillets :
        if p.billet == "FSGT" and p.current :
            flagFSGT = True

    if not flagFSGT :
        return HttpResponseRedirect('/')
    #End of second check
    
    return render_to_response('accountability/enterAttendance.html', {'cMid':cMid,
                                                                      }, 
                                                                      context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def saveEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    cPlatoon = cMid.platoon
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagFSGT = False
    for p in lBillets :
        if p.billet == "FSGT" and p.current :
            flagFSGT = True

    if not flagFSGT :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company = cCompany).filter(platoon = cPlatoon)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cEvent = Event(dateTime = request.POST['dateTime'],
                   type = request.POST['type'],
                   location = request.POST['location']
                   )
    cEvent.save()
    
    return HttpResponseRedirect('mid:switchboard')

@login_required(redirect_field_name='/')
def enterAttendance(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    cPlatoon = cMid.platoon
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagPLTS = False
    for p in lBillets :
        if p.billet == "PLTS" and p.current :
            flagPLTS = True

    if not flagPLTS :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company = cCompany).filter(platoon = cPlatoon)
    
    if cPlatoon == "1":
        lEvents = Event.objects.filter(company = cCompany).filter(not platoonOneSubmitted)
    elif cPlatoon == "2":
        lEvents = Event.objects.filter(company = cCompany).filter(not platoonTwoSubmitted)
    elif cPlatoon == "3":
        lEvents = Event.objects.filter(company = cCompany).filter(not platoonThreeSubmitted)
    elif cPlatoon == "4":
        lEvents = Event.objects.filter(company = cCompany).filter(not platoonFourSubmitted)
    
    return render_to_response('accountability/enterAttendance.html', {'cMid' : cMid, 
                                                                      'lMids' : lMids,
                                                                      'lEvents' : lEvents,
                                                                      }, 
                                                                      context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def saveAttendance(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    cPlatoon = cMid.platoon
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagPLTS = False
    for p in lBillets :
        if p.billet == "PLTS" and p.current :
            flagPLTS = True

    if not flagPLTS :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company = cCompany).filter(platoon = cPlatoon)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cEvent = Event.objects.get(id = request.POST['event'])
    
    for p in lMids :
        cAttendance = Attendance(mid = p,
                                 event = cEvent,
                                 tempStatus = request.POST[p.alpha+'A']                                
                                 )
        cAttendance.save()
        
    if cPlatoon == "1":
        cEvent.platoonOneSubmitted = True
    elif cPlatoon == "2":
        cEvent.platoonTwoSubmitted = True
    elif cPlatoon == "3":
        cEvent.platoonThreeSubmitted = True
    elif cPlatoon == "4":
        cEvent.platoonFourSubmitted = True
    
    if cEvent.platoonOneSubmitted and cEvent.platoonTwoSubmitted and cEvent.platoonThreeSubmitted and cEvent.platoonFourSubmitted :
        cEvent.companyComplete = True
    
    cEvent.save()

    return HttpResponseRedirect('mid:switchboard')
    
    