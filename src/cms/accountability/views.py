#accountability views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet

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
    
    return render_to_response('accountability/enterAttendance.html', {'cMid' : cMid, 
                                                                      'lMids' : lMids,
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
    
    cEvent = Event(dateTime = request.POST['dateTime'],
                   type = request.POST['type'],
                   location = request.POST['location']
                   )
    cEvent.save()
    
    for p in lMids :
        cAttendance = Attendance(mid = p,
                                 
                                 )
         
        event = models.ForeignKey(Event) 
    mid = models.ForeignKey("mid.Mid")
    status = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES,null=True)
    comment = models.TextField(null=True)
    tempStatus = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES,null=True)
    def __unicode__(self):
        return self.mid.LName + " - " + self.event 
    
    return HttpResponseRedirect('mid:switchboard')
    
    