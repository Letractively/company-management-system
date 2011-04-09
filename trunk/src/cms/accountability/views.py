#accountability views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet
from accountability.models import Event
from accountability.models import Attendance
from zero8.models import Zero8
from weekends.models import Weekend
from unit.models import Unit

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
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    flagFSGT = False
    for p in lBillets :
        if p.billet == "FSGT" and p.current :
            flagFSGT = True

    if not flagFSGT :
        return HttpResponseRedirect('/')
    #End of second check
    
    return render_to_response('accountability/createEvent.html', {'cMid':cMid,
                                                                  'lBillets' : lBillets,
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
                    workOrderOverdue = 0,
                    company = Unit.objects.get(company = cMid.company)
                    )
    cReport.save()
    
    lMids = Mid.objects.filter(company = cCompany).order_by('alpha')
    
    for p in lMids :
        cAttendance = Attendance(mid = p,
                                 event = cEvent,
                                 status = "U"                                
                                 )
        cAttendance.save()
    
    cDate = date.today()
    cNextWeekendBeg = cDate + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendBegAlt = cDate + timedelta(days=(6 - cDate.isoweekday()));
    
    lWeekends = []
    
    if date.today().isoweekday() == 5 :
        lWeekends = Weekend.objects.filter(startDate = date.today()).filter(mid__company = cCompany).filter(status='A').order_by('-mid')
 
    if date.today().isoweekday() == 6 :
        lWeekends1 = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(mid__company = cCompany).filter(status='A').order_by('-mid')
        lWeekends2 = Weekend.objects.filter(startDate = cNextWeekendBegAlt).filter(mid__company = cCompany).filter(status='A').order_by('-mid')
        lWeekends = lWeekends1 | lWeekends2

    for p in lWeekends :
        tMid = p.mid
        tAttendance = Attendance.objects.get(mid = tMid, event = cEvent)
        tAttendance.status = "W"
        tAttendance.comment = p.location + " (" + p.contactNumber + ")"
        tAttendance.save()
    
    return HttpResponseRedirect(reverse('switchboard'))

@login_required(redirect_field_name='/')
def enterAttendance(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    cPlatoon = cMid.platoon
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
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
                                                                      'lBillets' : lBillets,
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
def taps(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cDT = datetime.combine(cDate, time(23, 55, 00))
    
    cEvent = Event.objects.filter(company = cCompany).filter(type = "TAP").filter(dateTime = cDT)
    cEvent = cEvent[0]
    
    lAttendance = Attendance.objects.filter(event = cEvent
                                            ).exclude(status = "P"
                                                      ).exclude(status = "W"
                                                                ).exclude(status = "M").order_by('mid')

    return render_to_response('accountability/taps.html', {'cMid' : cMid, 
                                                           'lBillets', lBillets,
                                                           'cEvent' : cEvent,
                                                           'lAttendance' : lAttendance
                                                           }, 
                                                           context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveTAPS(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cDT = datetime.combine(cDate, time(23, 55, 00))
    
    cEvent = Event.objects.filter(company = cCompany).filter(type = "TAP").filter(dateTime = cDT)
    cEvent = cEvent[0]
    
    cMid = Mid.objects.get(alpha = request.POST['alpha'])
    
    cAttendance = Attendance.objects.get(mid = cMid, event = cEvent)
    cAttendance.status = request.POST[cMid.alpha+'A']
    cAttendance.save()

    return HttpResponseRedirect(reverse('accountability:taps'))
    
@login_required(redirect_field_name='/')
def selectEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
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
                                                                  'lBillets', : lBillets,
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
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    CC = False
    for p in lBillets :
        if p.billet == "CC" and p.current :
            CC = True

    if not CC :
        return HttpResponseRedirect('/')
    #End of second check
    
    lEvents = Event.objects.filter(company = cCompany).filter(companyComplete = False).order_by('dateTime')[0:40]
    
    return render_to_response('accountability/cancelEvent.html', {'cMid' : cMid, 
                                                                  'lBillets', lBillets,
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
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
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
                                                                       'lBillets' : lBillets,
                                                                       'cEvent' : cEvent,
                                                                       'lAttendance' : lAttendance
                                                                       }, 
                                                                       context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def viewAttendance(request):
    if request.method != "POST" :
        alpha = request.user.username.split('m')
        alpha = alpha[1]
        cMid = Mid.objects.get(alpha=alpha)
    else :
        cMid = Mid.objects.get(alpha = request.POST['alpha'])
    
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    cCompany = cMid.company
    
    lAttendance = Attendance.objects.filter(mid = cMid).exclude(status = "P")
    
    return render_to_response('accountability/viewAttendance.html', {'cMid' : cMid, 
                                                                     'lBillets' : lBillets,
                                                                     'lAttendance' : lAttendance
                                                                    }, 
                                                                    context_instance=RequestContext(request))