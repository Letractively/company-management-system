#weekends views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from cms.mid.models import Mid
from cms.mid.models import Billet
from cms.mid.models import Discipline
from cms.mid.models import Probation

from cms.weekends.models import Weekend

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from datetime import date
from datetime import timedelta

@login_required(redirect_field_name='/')
def index(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #List of current mid's billets
    cBillets = Billet.objects.filter(mid=cMid)
    
    #ADD ADMIN OFFICER FUNCTIONALITY BASED ON BILLET!!!
    
    #lWeekends - list of currently requested weekends
    lWeekends = Weekend.objects.filter(mid=cMid).order_by('-startDate')
    
    #cDiscipline - list of Discipline objects
    lDiscipline = Discipline.objects.filter(mid=cMid).order_by('-startDate')
    
    #cProbation - list of Probation objects
    lProbation = Probation.objects.filter(mid=cMid).order_by('-startDate')
    
    #Current date 
    cDate = date.today()
    
    #Check if today is a day before Thursday
    late = True
    if cDate.isoweekday() < 4 :
        late = False
    
    #Assign next weekend's beginning and end
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
    #Check if the user is currently on restriction
    onRestriction = False
    for p in lDiscipline :
       if p.startDate < cDate and p.startDate + timedelta(days=p.daysAwarded) < cDate :
            onRestriction = True
    
    #Check if user is currently on probation
    onProbation = False  
    for p in lProbation :
        if p.startDate < cDate and p.startDate + timedelta(days=p.daysAwarded) < cDate :
            onProbation = True
            
    #Check for the current weekend
    cWeekend = None
    for p in lWeekends :
        if p.startDate == cNextWeekendBeg :
            cWeekend = p;
    
    weekendsComment = cMid.weekendsComment
    
    #List of weekends redone, this time subtracting weekends that were not explicitly approved
    lWeekends = Weekend.objects.filter(mid=cMid).filter(status='A').order_by('-startDate')
    
    #WT - Weekends Taken
    WT = len(lWeekends)
    
    #WL - Weekends Left
    WL = cMid.weekends - WT
    
    #WE - Weekend Eligible
    WE = False
    if WL > 0 and cMid.acSAT and cMid.PRTSat and not onRestriction and not onProbation:
        WE = True

    return render_to_response('weekends/weekend.html', { 'mid' : cMid, 'lWeekends' : lWeekends, 'cWeekend' : cWeekend,
                                                        'WT' : WT, 'WL' : WL, 'WE' : WE, 
                                                        'today' : cDate, 'late' : late,
                                                        'NWB' : cNextWeekendBeg, 'NWE' : cNextWeekendEnd,
                                                        }, 
                                                        context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def reqWeekend(request):
    cLocation = request.POST['location']
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
        
    cWeekend = Weekend(mid=cMid, startDate=cNextWeekendBeg, endDate=cNextWeekendEnd,
                       status = 'P', location = cLocation, contactNumber = cMid.phoneNumber)
    
    cWeekend.save()

    return HttpResponseRedirect('/weekends/')
