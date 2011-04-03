#Zero8 views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet
from units.models import Units
from units.models import UnitLeaders
from zero8.models import Zero8
from zero8.models import SignificantEvents
from accountability.models import Event
from accountability.models import Attendance
from weekends.models import Weekend
from movementorder.models import MovementOrder
from movementorder.models import MOParticipant
from discipline.models import Separation

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
def viewReport(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    #Get date for the 0800 review
    #reportDate = request.POST['date']
    reportDate = date.today()
    cReport = Zero8.objects.get(reportDate = reportDate)
    
    lSigEventsA = SignificantEvents.objects.filter(zero8 = cReport).filter(section = "A")
    cSigEventsA = lSigEventsA.count()
    lSigEventsB = SignificantEvents.objects.filter(zero8 = cReport).filter(section = "B")
    cSigEventsB = lSigEventsB.count()
    lSigEventsC = SignificantEvents.objects.filter(zero8 = cReport).filter(section = "C")
    cSigEventsC = lSigEventsC.count()
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cDT = datetime.combine(cReport.reportDate, time(23, 55, 00))
    
    cEvent = Event.objects.filter(company = cCompany).filter(type = "TAP").filter(dateTime = cDT)
    cEvent = cEvent[0]
    
    lMidsOnMO = Mid.objects.filter(company = cCompany).filter(moparticipant__MO__returnDate = "3000-01-01")
    
    for p in lMidsOnMO:
        tAttendance = Attendance.objects.get(mid = p, event = cEvent)
        tAttendance.status = "M"
        tAttendance.save()
    
    cTAPS1P = Attendance.objects.filter(event = cEvent).filter(status = "P").filter(mid__rank = 1).count()
    cTAPS2P = Attendance.objects.filter(event = cEvent).filter(status = "P").filter(mid__rank = 2).count()
    cTAPS3P = Attendance.objects.filter(event = cEvent).filter(status = "P").filter(mid__rank = 3).count()
    cTAPS4P = Attendance.objects.filter(event = cEvent).filter(status = "P").filter(mid__rank = 4).count()
    
    cTAPS1A = Attendance.objects.filter(event = cEvent).filter(status = "A").filter(mid__rank = 1).count()
    cTAPS2A = Attendance.objects.filter(event = cEvent).filter(status = "A").filter(mid__rank = 2).count()
    cTAPS3A = Attendance.objects.filter(event = cEvent).filter(status = "A").filter(mid__rank = 3).count()
    cTAPS4A = Attendance.objects.filter(event = cEvent).filter(status = "A").filter(mid__rank = 4).count()
    
    cTAPS1U = Attendance.objects.filter(event = cEvent).filter(status = "U").filter(mid__rank = 1).count()
    cTAPS2U = Attendance.objects.filter(event = cEvent).filter(status = "U").filter(mid__rank = 2).count()
    cTAPS3U = Attendance.objects.filter(event = cEvent).filter(status = "U").filter(mid__rank = 3).count()
    cTAPS4U = Attendance.objects.filter(event = cEvent).filter(status = "U").filter(mid__rank = 4).count()
    
    cTAPS1W = Attendance.objects.filter(event = cEvent).filter(status = "W").filter(mid__rank = 1).count()
    cTAPS2W = Attendance.objects.filter(event = cEvent).filter(status = "W").filter(mid__rank = 2).count()
    cTAPS3W = Attendance.objects.filter(event = cEvent).filter(status = "W").filter(mid__rank = 3).count()
    cTAPS4W = Attendance.objects.filter(event = cEvent).filter(status = "W").filter(mid__rank = 4).count()
    
    cTAPS1M = Attendance.objects.filter(event = cEvent).filter(status = "M").filter(mid__rank = 1).count()
    cTAPS2M = Attendance.objects.filter(event = cEvent).filter(status = "M").filter(mid__rank = 2).count()
    cTAPS3M = Attendance.objects.filter(event = cEvent).filter(status = "M").filter(mid__rank = 3).count()
    cTAPS4M = Attendance.objects.filter(event = cEvent).filter(status = "M").filter(mid__rank = 4).count()
     
    cTotalP = cTAPS1P + cTAPS2P + cTAPS3P + cTAPS4P
    cTotalA = cTAPS1A + cTAPS2A + cTAPS3A + cTAPS4A
    cTotalU = cTAPS1U + cTAPS2U + cTAPS3U + cTAPS4U
    cTotalW = cTAPS1W + cTAPS2W + cTAPS3W + cTAPS4W
    cTotalM = cTAPS1M + cTAPS2M + cTAPS3M + cTAPS4M
    
    lA = Attendance.objects.filter(event = cEvent).filter(status = "A").order_by('mid')
    lU = Attendance.objects.filter(event = cEvent).filter(status = "U").order_by('mid')
    lW = Attendance.objects.filter(event = cEvent).filter(status = "W").order_by('mid')
    lM = MovementOrder.objects.filter(moparticipant__participant__company = cCompany).filter(returnDate = "3000-01-01").order_by('-departDate').distinct()
    lPS = Separation.objects.filter(zero8 = cReport).filter(pending = True)
    lFS = Separation.objects.filter(zero8 = cReport).filter(pending = False)
    
    lR = 
    lT = 
    
    return render_to_response('zero8/viewReport.html', {#'cMid':cMid,
                                                        'cReport' : cReport,
                                                        'cDate' : cDate,
                                                        'cCompany' : cCompany, 
                                                        'lSigEventsA' : lSigEventsA,
                                                        'cSigEventsA' : cSigEventsA,
                                                        'lSigEventsB' : lSigEventsB,
                                                        'cSigEventsB' : cSigEventsB,
                                                        'lSigEventsC' : lSigEventsC,
                                                        'cSigEventsC' : cSigEventsC,
                                                        'cTAPS1P' : cTAPS1P,
                                                        'cTAPS2P' : cTAPS2P,
                                                        'cTAPS3P' : cTAPS3P,
                                                        'cTAPS4P' : cTAPS4P,
                                                        'cTAPS1A' : cTAPS1A,
                                                        'cTAPS2A' : cTAPS2A,
                                                        'cTAPS3A' : cTAPS3A,
                                                        'cTAPS4A' : cTAPS4A,
                                                        'cTAPS1U' : cTAPS1U,
                                                        'cTAPS2U' : cTAPS2U,
                                                        'cTAPS3U' : cTAPS3U,
                                                        'cTAPS4U' : cTAPS4U,
                                                        'cTAPS1W' : cTAPS1W,
                                                        'cTAPS2W' : cTAPS2W,
                                                        'cTAPS3W' : cTAPS3W,
                                                        'cTAPS4W' : cTAPS4W,
                                                        'cTAPS1M' : cTAPS1M,
                                                        'cTAPS2M' : cTAPS2M,
                                                        'cTAPS3M' : cTAPS3M,
                                                        'cTAPS4M' : cTAPS4M,
                                                        'cTotalP' : cTotalP,
                                                        'cTotalA' : cTotalA,
                                                        'cTotalU' : cTotalU,
                                                        'cTotalW' : cTotalW,
                                                        'cTotalM' : cTotalM,
                                                        'lU' : lU,
                                                        'lA' : lA,
                                                        'lW' : lW,
                                                        'lM' : lM,
                                                        'lPS' : lPS,
                                                        'lFS' : lFS,
                                                        
                                                       }, 
                                                       context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def createSignificantEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    lMids = Mid.objects.filter(company = cCompany)
    
    return render_to_response('zero8/createSignificantEvent.html', {'cMid':cMid,
                                                                    'lMids' : lMids,
                                                                    }, 
                                                                    context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def saveSignificantEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
                cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
        
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    cEvent = SignificantEvents(zero8 = cReport,
                               section = request.POST['section'],
                               name = Mid.objects.get(alpha = request.POST['alpha']),
                               description = request.POST['description'],
                               adminNote = request.POST['adminNote']
                               )
    cEvent.save()
    
    return HttpResponseRedirect(reverse('zero8:createSignificantEvent'))
