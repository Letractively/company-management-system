# Author: Dimitri Hatley
# Editor: Michael Laws
#ALERT!!! Pre-production change in index; change upon test completion
#ALERT!!! Pre-production change in admin; change upon test completion

from mid.models import Mid
from mid.models import Billet
from discipline.models import Restriction

from weekends.models import Weekend

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.core.context_processors import csrf

#from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from datetime import date
from datetime import timedelta
from django.db.models import Q

import re

@login_required(redirect_field_name='/')
def index(request):
    #Basic user view for weekend requests
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    #lWeekends - list of currently requested weekends
    lWeekends = Weekend.objects.filter(mid=cMid).order_by('-startDate')
    
    #lDiscipline - list of Discipline objects
    lRestriction = Restriction.objects.filter(mid=cMid).order_by('-startDate')
    
    #Current date 
    cDate = date.today()
    
    #Check if today is a day before Thursday
    late = True
    if cDate.isoweekday() < 4 :
        late = False
    
    #Assign next weekend's beginning and end
    cNextWeekendBeg = None
    cNextWeekendEnd = None
    
    if cMid.rank == "3" or cMid.rank == "4" :
        cNextWeekendBeg = date.today() + timedelta(days=(6 - cDate.isoweekday()));
        cNextWeekendEnd = cNextWeekendBeg + timedelta(days=1);
    else :
        cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
        cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
    #Check if the user is currently on restriction
    onRestriction = False
    for p in lRestriction :
       if p.startDate < cDate and p.daysRemaining > 0 :
            onRestriction = True
            
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
    if WL > 0 and cMid.acSAT and cMid.PRTSat and not onRestriction:
        WE = True

    #ALERT!!! ('late' : False); switch back to ('late' : late) for production
    # Laws - 4-5-2011 : i just changed the above switch for production.
    return render_to_response('weekends/weekend.html', { 'cMid' : cMid, 'lWeekends' : lWeekends, 'cWeekend' : cWeekend,
                                                         'WT' : WT, 'WL' : WL, 'WE' : WE, 
                                                         'today' : cDate, 'late' : late,
                                                         'NWB' : cNextWeekendBeg, 'NWE' : cNextWeekendEnd,
                                                         'lBillets' : lBillets
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
    cMid = Mid.objects.get(alpha=alpha)
    
    cDate = date.today()
    cNextWeekendBeg = None
    cNextWeekendEnd = None
    
    if cMid.rank == "3" or cMid.rank == "4" :
        cNextWeekendBeg = date.today() + timedelta(days=(6 - cDate.isoweekday()));
        cNextWeekendEnd = cNextWeekendBeg + timedelta(days=1);
    else :
        cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
        cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
        
    cWeekend = Weekend(mid=cMid, 
                       startDate=cNextWeekendBeg, 
                       endDate=cNextWeekendEnd,
                       status = 'P', 
                       location = cLocation, 
                       contactNumber = cMid.phoneNumber)
    
    cWeekend.save()

    return HttpResponseRedirect(reverse('weekends:weekendIndex'))
    #return HttpResponseRedirect('/weekends/')
    
@login_required(redirect_field_name='/')
def cancelReqWeekend(request):
    #Cancels a weekend request
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    cDate = date.today()
    cNextWeekendBeg = None
    cNextWeekendEnd = None
    
    if cMid.rank == "3" or cMid.rank == "4" :
        cNextWeekendBeg = date.today() + timedelta(days=(6 - cDate.isoweekday()));
    else :
        cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    
    #Find and kill specified weekend    
    cWeekend = Weekend.objects.filter(mid = cMid).filter(startDate = cNextWeekendBeg)
    cWeekend.delete()

    return HttpResponseRedirect(reverse('weekends:weekendIndex'))
    #return HttpResponseRedirect('/weekends/')

@login_required(redirect_field_name='/')
def viewList(request):
    #Called on /weekends/view -> generates a current weekend list, no additional functionality
    username = request.user.username
    
    CO = False
    SEL = False
    lBillets = []
    
    if re.match("CO", username) is not None :
        username = username.split('_')
        cCompany = username[1]
        CO = True
        
    elif re.match("SEL", username) is not None :
        username = username.split('_')
        cCompany = username[1]
        SEL = True
    
    else :
        alpha = username.split('m')
        alpha = alpha[1]
        cMid = Mid.objects.get(alpha=alpha)
        cCompany = cMid.company
        lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendBegAlt = date.today() + timedelta(days=(6 - cDate.isoweekday()));
    
    lWeekends1 = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(mid__company = cCompany).filter(status='A').order_by('-mid')
    lWeekends2 = Weekend.objects.filter(startDate = cNextWeekendBegAlt).filter(mid__company = cCompany).filter(status='A').order_by('-mid')
    lWeekends = lWeekends1 | lWeekends2

    #list of current approved weekends
    lWeekends = Weekend.objects.filter(mid__company=cCompany).filter( Q(startDate = cNextWeekendBeg) | Q(startDate = cNextWeekendBegAlt)).filter(status = 'A').order_by('-mid')
      
    return render_to_response('weekends/list.html', { 'CO' : True,
                                                      'SEL' : True,
                                                      'cMid' : cMid,
                                                      'lBillets' : lBillets,
                                                      'cCompany' : cCompany,
                                                      'lWeekends' : lWeekends }, 
                                                      context_instance=RequestContext(request))

#Following functions deal with the Admin Officer functionality
@login_required(redirect_field_name='/')
def admin(request):
    #Called on /weekends/admin -> generates an editable list of weekend counts and comments for the company
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    flagAdmin = False
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')
    
    return render_to_response('weekends/admin.html', { 'cMid' : cMid,
                                                       'lBillets' : lBillets,
                                                       'cCompany' : cCompany, 
                                                       'lMids' : lMids },
                              context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveWeekendCount(request):
    #Saves updated weekend counts and comments
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagAdmin = False
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')
    
    for p in lMids :
        p.weekends = request.POST[p.alpha+'C']
        p.weekendsComment = request.POST[p.alpha+'Comm']
        p.save()

    return HttpResponseRedirect(reverse('weekends:weekendAdmin')) 
    #return HttpResponseRedirect('/weekends/admin')

#Following functions deal with CO's functionality - approval and disapproval of weekend requests
@login_required(redirect_field_name='/')
def coApproval(request):
    #Called on /weekends/co -> generates a list of weekends to be approved
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendBegAlt = date.today() + timedelta(days=(6 - cDate.isoweekday()));
    
    #list of current non-approved weekends
    lWeekends1 = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(mid__company = cCompany).filter(status='P').order_by('-mid')
    lWeekends2 = Weekend.objects.filter(startDate = cNextWeekendBegAlt).filter(mid__company = cCompany).filter(status='P').order_by('-mid')
    lWeekends = lWeekends1 | lWeekends2
    
    
    return render_to_response('weekends/co.html', {'CO' : True, 
                                                   'lWeekends' : lWeekends,
                                                   }, 
                                                   context_instance=RequestContext(request))

@login_required(redirect_field_name='/')    
def approveWeekend(request):
    #Approves a specific weekend, redirects back to CO's approval page
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['mid'] 
    cMid = Mid.objects.get(alpha=alpha)
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = None
    cNextWeekendEnd = None
    
    if cMid.rank == "3" or cMid.rank == "4" :
        cNextWeekendBeg = date.today() + timedelta(days=(6 - cDate.isoweekday()));
    else :
        cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    
    cWeekend = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(mid=cMid)
    for p in cWeekend :
        p.status = "A"
        p.save()
    
    return HttpResponseRedirect(reverse('weekends:coApproval'))
    
@login_required(redirect_field_name='/')
def denyWeekend(request): 
    #Denies a specific weekend, redirects back to CO's approval page
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['mid'] 
    cMid = Mid.objects.get(alpha=alpha)
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = None
    cNextWeekendEnd = None
    
    if cMid.rank == "3" or cMid.rank == "4" :
        cNextWeekendBeg = date.today() + timedelta(days=(6 - cDate.isoweekday()));
    else :
        cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    
    cWeekend = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(mid=cMid)
    for p in cWeekend :
        p.status = "D"
        p.save()
    
    return HttpResponseRedirect(reverse('weekends:coApproval'))

@login_required(redirect_field_name='/')
def approveAllWeekends(request):
    #Automatically approves all weekends in the CO's list
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendBegAlt = date.today() + timedelta(days=(6 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
    #list of current non-approved weekends
    lWeekends1 = Weekend.objects.filter(startDate = cNextWeekendBeg).filter(mid__company = cCompany).filter(status='P').order_by('-mid')
    lWeekends2 = Weekend.objects.filter(startDate = cNextWeekendBegAlt).filter(mid__company = cCompany).filter(status='P').order_by('-mid')
    lWeekends = lWeekends1 | lWeekends2
    
    for p in lWeekends :
        p.status = "A"
        p.save()
        
    return HttpResponseRedirect(reverse('weekends:coApproval'))

@login_required(redirect_field_name='/')
def grantWeekends(request):
    #Shows the menu for forcing a weekend
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    cDate = date.today()
    cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
    cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
    #lMidsOnWeekend = Mid.objects.filter(weekend__startDate = cNextWeekendBeg)
    lMids = Mid.objects.filter(company = cCompany).exclude(weekend__startDate = cNextWeekendBeg).order_by('alpha')
                                                                                                        
    return render_to_response('weekends/grantWeekends.html', {  'CO' : True,
                                                                'NWB' : cNextWeekendBeg,
                                                                'NWE' : cNextWeekendEnd,
                                                                'lMids' : lMids }, 
                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def commitWeekendGrant(request):
    #Allows the CO to grant a weekend to a person who would not be eligible for one
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    #date assignment block
    cDate = date.today()
    cNextWeekendBeg = None
    cNextWeekendEnd = None
    
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    alpha = request.POST['alpha']
    cLocation = request.POST['location']
    
    if alpha != "null" :
        cMid = Mid.objects.get(alpha=alpha)
    
        if cMid.rank == "3" or cMid.rank == "4" :
            cNextWeekendBeg = date.today() + timedelta(days=(6 - cDate.isoweekday()));
            cNextWeekendEnd = cNextWeekendBeg + timedelta(days=1);
        else :
            cNextWeekendBeg = date.today() + timedelta(days=(5 - cDate.isoweekday()));
            cNextWeekendEnd = cNextWeekendBeg + timedelta(days=2);
    
        cWeekend = Weekend(mid=cMid, 
                           startDate=cNextWeekendBeg, 
                           endDate=cNextWeekendEnd,
                           status = 'A', 
                           location = cLocation, 
                           contactNumber = cMid.phoneNumber)
        
        cWeekend.save()
        
    return HttpResponseRedirect(reverse('weekends:grantWeekends'))