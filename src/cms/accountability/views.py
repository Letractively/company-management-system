#accountability views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet
from accountability.models import Event
from accountability.models import Attendance
from zero8.models import Zero8

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
from datetime import time
from datetime import datetime
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
    
    return render_to_response('accountability/createEvent.html', {'cMid':cMid,
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
                   location = request.POST['location'],
                   platoonOneSubmitted = False,
                   platoonTwoSubmitted = False,
                   platoonThreeSubmitted = False,
                   platoonFourSubmitted = False,
                   companyComplete = False,
                   company = cCompany
                   )
    cEvent.save()
    
    return HttpResponseRedirect(reverse('accountability:createEvent'))

@login_required(redirect_field_name='/')
def makeDay(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company  
    
    cEvent = Event(dateTime = datetime.combine(date.today(), time(07, 00, 00)),
                   type = "MMF",
                   location = "Company Area",
                   platoonOneSubmitted = False,
                   platoonTwoSubmitted = False,
                   platoonThreeSubmitted = False,
                   platoonFourSubmitted = False,
                   companyComplete = False,
                   company = cCompany
                   )
    cEvent.save()
    
    cEvent = Event(dateTime = datetime.combine(date.today(), time(12, 05, 00)),
                   type = "NMF",
                   location = "Tecumseh Court",
                   platoonOneSubmitted = False,
                   platoonTwoSubmitted = False,
                   platoonThreeSubmitted = False,
                   platoonFourSubmitted = False,
                   companyComplete = False,
                   company = cCompany
                   )
    cEvent.save()
    
    cEvent = Event(dateTime = datetime.combine(date.today(), time(18, 30, 00)),
                   type = "EMF",
                   location = "Company Area",
                   platoonOneSubmitted = False,
                   platoonTwoSubmitted = False,
                   platoonThreeSubmitted = False,
                   platoonFourSubmitted = False,
                   companyComplete = False,
                   company = cCompany
                   )
    cEvent.save()
    
    cEvent = Event(dateTime = datetime.combine(date.today(), time(23, 55, 00)),
                   type = "TAP",
                   location = "Company Area",
                   platoonOneSubmitted = True,
                   platoonTwoSubmitted = True,
                   platoonThreeSubmitted = True,
                   platoonFourSubmitted = True,
                   companyComplete = False,
                   company = cCompany
                   )
    cEvent.save()
    
    cReport = Zero8(offgoingCDO = cMid,
                    oncomingCDO = cMid,
                    reportDate = date.today(),
                    forceProtectionCondition = "A",
                    workOrderActive = 0,
                    workOrderClosed = 0,
                    workOrderOverdue = 0
                    )
    cReport.save()
    
    return HttpResponseRedirect(reverse('switchboard'))

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
        lEvents = Event.objects.filter(company = cCompany).filter(platoonOneSubmitted = False)
    elif cPlatoon == "2":
        lEvents = Event.objects.filter(company = cCompany).filter(platoonTwoSubmitted = False)
    elif cPlatoon == "3":
        lEvents = Event.objects.filter(company = cCompany).filter(platoonThreeSubmitted = False)
    elif cPlatoon == "4":
        lEvents = Event.objects.filter(company = cCompany).filter(platoonFourSubmitted  = False)
    
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
                                 status = request.POST[p.alpha+'A']                                
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

    return HttpResponseRedirect(reverse('accountability:enterAttendance'))
    
@login_required(redirect_field_name='/')
def selectEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    FSGT = False
    for p in lBillets :
        if p.billet == "FSGT" and p.current :
            FSGT = True

    if not FSGT :
        return HttpResponseRedirect('/')
    #End of second check
    
    lEvents = Event.objects.filter(company = cCompany).filter(companyComplete = True).order_by('dateTime')[0:20]
    lInProgEvents = Event.objects.filter(company = cCompany).filter(companyComplete = False).order_by('dateTime')
    
    return render_to_response('accountability/selectEvent.html', {'cMid' : cMid, 
                                                                  'lEvents' : lEvents,
                                                                  'lInProgEvents' : lInProgEvents
                                                                  }, 
                                                                  context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def cancelEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    CC = False
    for p in lBillets :
        if p.billet == "CC" and p.current :
            CC = True

    if not CC :
        return HttpResponseRedirect('/')
    #End of second check
    
    lEvents = Event.objects.filter(company = cCompany).filter(companyComplete = False).order_by('dateTime')[0:40]
    
    return render_to_response('accountability/cancelEvent.html', {'cMid' : cMid, 
                                                                  'lEvents' : lEvents,
                                                                  }, 
                                                                  context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveCancelEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    CC = False
    for p in lBillets :
        if p.billet == "CC" and p.current :
            CC = True

    if not CC :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cEvent = Event.objects.get(id = request.POST['event'])
    
    lAttendance = Attendance.objects.filter(event = cEvent)
    
    for p in lAttendance :
        p.delete()
        
    cEvent.delete()
    
    return HttpResponseRedirect(reverse('accountability:cancelEvent'))
    
@login_required(redirect_field_name='/')
def reviewAttendance(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    FSGT = False
    for p in lBillets :
        if p.billet == "FSGT" and p.current :
            FSGT = True

    if not FSGT :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cEvent = Event.objects.get(id = request.POST['event'])
    lAttendance = Attendance.objects.filter(event = cEvent)
    
    return render_to_response('accountability/reviewAttendance.html', {'cMid' : cMid, 
                                                                       'cEvent' : cEvent,
                                                                       'lAttendance' : lAttendance
                                                                       }, 
                                                                       context_instance=RequestContext(request))