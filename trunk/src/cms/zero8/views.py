#Zero8 views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet
from zero8.models import Zero8
from zero8.models import SignificantEvents

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
    
    cReport = Zero8.objects.get(reportDate = date.today())
    cDate = cReport.reportDate
    
    lSigEventsA = SignificantEvents.objects.filter(zero8 = cReport).filter(section = "A")
    cSigEventsA = lSigEventsC.count()
    lSigEventsB = SignificantEvents.objects.filter(zero8 = cReport).filter(section = "B")
    cSigEventsB = lSigEventsB.count()
    lSigEventsC = SignificantEvents.objects.filter(zero8 = cReport).filter(section = "C")
    cSigEventsB = lSigEventsC.count()
    
    return render_to_response('zero8/viewReport.html', {'cMid':cMid,
                                                        'cReport' : cReport,
                                                        'cDate' : cDate,
                                                        'lSigEventsA' : lSigEventsA,
                                                        'cSigEventsA' : cSigEventsA,
                                                        'lSigEventsB' : lSigEventsB,
                                                        'cSigEventsB' : cSigEventsB,
                                                        'lSigEventsC' : lSigEventsC,
                                                        'cSigEventsB' : cSigEventsC,
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
    
    cReport = Zero8.objects.get(reportDate = date.today())
    
    cEvent = SignificantEvents(zero8 = cReport,
                               section = request.POST['section'],
                               name = Mid.objects.get(alpha = request.POST['alpha']),
                               description = request.POST['description'],
                               adminNote = request.POST['adminNote']
                               )
    cEvent.save()
    
    return HttpResponseRedirect(reverse('zero8:createSignificantEvent'))
