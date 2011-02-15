#weekends views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from cms.mid.models import Mid
from cms.mid.models import Billets
from cms.mid.models import Discipline
from cms.mid.models import Probation

from cms.weekends.models import Weekend

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from datetime import date
from datetime import timedelta

@login_required(redirect_field_name='')
def index(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    cBillets = Billets.objects.filter(mid=cMid)
    
    #cWeekends - list of currently taken weekends
    cWeekends = Weekend.objects.filter(mid=cMid).order_by('-startDate')
    cDiscipline = Discipline.objects.filter(mid=cMid)
    cProbation = Probation.objects.filter(mid=cMid)
    
    cDate = date.today()
    
    late = True
    
    if cDate.isoweekday() < 4 :
        cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
        cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
        late = False
    
    onRestriction = False
    onProbation = False
    
    for p in cDiscipline :
       if p.startDate < cDate and p.startDate + timedelta(days=p.daysAwarded) < cDate :
            onRestriction = True
            
    for p in cProbation :
        if p.startDate < cDate and p.startDate + timedelta(days=p.daysAwarded) < cDate :
            onProbation = True
    
    #WT - Weekends Taken
    WT = len(cWeekends)
    
    #WL - Weekends Left
    WL = cMid.weekends - WT
    
    #WE - Weekend Eligible
    if cMid.Weekends > 0 and cMid.AcSAT and cMid.PRTSAT and not onRestriction and not onProbation:
        WE = True 

    return render_to_response('weekends/weekend.html', { 'mid' : cMid, 'cWeekend' : cWeekends, 
                                                        'WT' : WT, 'WL' : WL, 'WE' : WE, 
                                                        'today' : cDate, 'late' : late,
                                                        'NWB' : cNextWeekendBeg, 'NWE' : cNextWeekendEnd }, 
                                                        context_instance=RequestContext(request))

@login_required(redirect_field_name='')
def reqWeekend(request):
    return render_to_response('weekends/reqWeekend.html', {})