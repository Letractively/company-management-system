# Author: Dimitri Hatley
# Editor: Michael Laws
#ALERT!!! Pre-production change in index; change upon test completion
#ALERT!!! Pre-production change in admin; change upon test completion

from mid.models import Mid
from mid.models import Billet
from mid.models import Discipline
from mid.models import Probation

from weekends.models import Weekend

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.core.context_processors import csrf

#from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from datetime import date
from datetime import timedelta

@login_required(redirect_field_name='/')
def index(request):
    #Basic user view for weekend requests
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #lWeekends - list of currently requested weekends
    lWeekends = Weekend.objects.filter(mid=cMid).order_by('-startDate')
    
    #lDiscipline - list of Discipline objects
    lDiscipline = Discipline.objects.filter(mid=cMid).order_by('-startDate')
    
    #lProbation - list of Probation objects
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

    #ALERT!!! ('late' : False); switch back to ('late' : late) for production
    return render_to_response('weekends/weekend.html', { 'mid' : cMid, 'lWeekends' : lWeekends, 'cWeekend' : cWeekend,
                                                         'WT' : WT, 'WL' : WL, 'WE' : WE, 
                                                         'today' : cDate, 'late' : False,
                                                         'NWB' : cNextWeekendBeg, 'NWE' : cNextWeekendEnd,
                                                        }, 
                                                        context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def reqWeekend(request):
    #Requests a weekend
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cLocation = request.POST['location']
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
        
    cWeekend = Weekend(mid=cMid, 
                       startDate=cNextWeekendBeg, 
                       endDate=cNextWeekendEnd,
                       status = 'P', 
                       location = cLocation, 
                       contactNumber = cMid.phoneNumber)
    
    cWeekend.save()

    return HttpResponseRedirect('/weekends/')
    
@login_required(redirect_field_name='/')
def cancelReqWeekend(request):
    #Cancels a weekend request
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    
    #Find and kill specified weekend    
    cWeekend = Weekend.objects.filter(mid = cMid).filter(startDate = cNextWeekendBeg)
    cWeekend.delete()

    return HttpResponseRedirect('/weekends/')

@login_required(redirect_field_name='/')
def viewList(request):
    #Called on /weekends/view -> generates a current weekend list, no additional functionality
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
    #list of current approved weekends
    lWeekends = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(status = 'A').order_by('-mid')
      
    return render_to_response('/weekends/list.html', { 'lWeekends' : lWeekends }, 
                              context_instance=RequestContext(request))

#Following functions deal with the Admin Officer functionality
@login_required(redirect_field_name='/')
def admin(request):
    #Called on /weekends/admin -> generates an editable list of weekend counts and comments for the company
    
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
    
    #ALERT! In the corresponding view second input text size is 50 due to the database limit. 
    #Change required to allow for at least 120 symbols. 
    return render_to_response('/weekends/admin.html', { 'lMids' : lMids },
                              context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveWeekendCount(request):
    #Saves updated weekend counts and comments
    
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
        return HttpResponseRedirect("/")
    
    lMids = Mid.objects.order_by('alpha')
    
    for p in lMids :
        p.weekends = request.POST[p.alpha+'C']
        p.weekendsComment = request.POST[p.alpha+'Comm']
        p.save()
        
    return HttpResponseRedirect('/weekends/admin')

#Following functions deal with CO's functionality - approval and disapproval of weekend requests
@login_required(redirect_field_name='/')
def coApproval(request):
    #Called on /weekends/co -> generates a list of weekends to be approved
    
    #Second check - make sure the user is CO
    name = request.user.username    
    if name != 'CO' :
        return HttpResponseRedirect('/')
    #End of second check
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
    #list of current non-approved weekends
    lWeekends = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(status='P').order_by('-mid')
                                                                                                        
    return render_to_response('weekends/co.html', { 'lWeekends' : lWeekends }, 
                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')    
def approveWeekend(request):
    #Approves a specific weekend, redirects back to CO's approval page
    
    #Second check - make sure the user is CO
    name = request.user.username    
    if name != 'CO' :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['mid'] 
    cMid = Mid.objects.filter(alpha=alpha)
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
    cWeekend = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(mid=cMid)
    for p in cWeekend :
        p.status = "A"
        p.save()
    
    return HttpResponseRedirect('/weekends/co')
    
@login_required(redirect_field_name='/')
def denyWeekend(request): 
    #Denies a specific weekend, redirects back to CO's approval page
    
    #Second check - make sure the user is CO
    name = request.user.username    
    if name != 'CO' :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['mid'] 
    cMid = Mid.objects.filter(alpha=alpha)
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
    cWeekend = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(mid=cMid)
    for p in cWeekend :
        p.status = "D"
        p.save()
    
    return HttpResponseRedirect('/weekends/co')

@login_required(redirect_field_name='/')
def approveAllWeekends(request):
    #Automatically approves all weekends in the CO's list
    
    #Second check - make sure the user is CO
    name = request.user.username    
    if name != 'CO' :
        return HttpResponseRedirect('/')
    #End of second check
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
    #list of current non-approved weekends
    lWeekends = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(status='P').order_by('-mid')
    
    for p in lWeekends :
        p.status = "A"
        p.save()
                                                                                                        
    return HttpResponseRedirect('/weekends/co')