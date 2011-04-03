#ORM veiws.py
# Author: Dimitri Hatley

from mid.models import Mid
from mid.models import Billet

from discipline.models import Restriction
from discipline.models import Tours
from discipline.models import Probation

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

@login_required(redirect_field_name='/')
def enterDiscipline(request):
    #Enter Restriction/Tours
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')
    
    return render_to_response('discipline/enterDiscipline.html', { 'cCompany' : cCompany, 
                                                            'lMids' : lMids },
                                                            context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def saveDiscipline(request):
    #Save entered Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['alpha']
    honor = request.POST['honor']
    dateOffense = request.POST['dateOffense']
    startDate = request.POST['startDate']
    daysAwarded = int(request.POST['daysAwarded'])
    toursAwarded = int(request.POST['toursAwarded'])
    adminNotes = request.POST['adminNotes']
    
    if toursAwarded < daysAwarded :
        toursAwarded = daysAwarded
            
    lDisc = Restriction.objects.filter(mid = Mid.objects.get(alpha = alpha))
    
    cDisc = None
    for p in lDisc :
        if p.startDate < date.today() and p.daysRemaining > 0 :
            cDisc = p
            
    if cDisc is None :
        if daysAwarded > 0 :
            cDisc = Restriction(mid = Mid.objects.get(alpha = alpha),
                                conductHonor = honor,
                                dateOffence = dateOffense,
                                startDate = startDate,
                                daysAwarded = daysAwarded,
                                daysRemaining = daysAwarded,
                                adminNotes = adminNotes,
                                checked = date.today()
                                )
            cDisc.save()
            
        if toursAwarded > 0 :
            cDisc = Tours(mid = Mid.objects.get(alpha = alpha),
                          conductHonor = honor,
                          dateOffence = dateOffense,
                          startDate = startDate,
                          toursAwarded = toursAwarded,
                          toursRemaining = toursAwarded,
                          adminNotes = adminNotes,
                          )
        cDisc.save()
    
    else :
        cDisc.daysRemaining = cDisc.daysRemaining + daysAwarded
        cDisc.daysAwarded = cDisc.daysAwarded+daysAwarded
        cDisc.save()
        cDisc = Tours.objects.get(startDate = cDisc.startDate)
        cDisc.toursRemaining = cDisc.toursRemaining + toursAwarded
        cDisc.toursAwarded = cDisc.toursAwarded+toursAwarded
        cDisc.save()
    
    return HttpResponseRedirect(reverse('discipline:enterDiscipline')) 

@login_required(redirect_field_name='/')
def enterProbation(request):
    #Enter Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')
    
    return render_to_response('discipline/enterProbation.html', { 'cCompany' : cCompany, 
                                                            'lMids' : lMids },
                                                            context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def saveProbation(request):
    #Save entered Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['alpha']
    startDate = request.POST['startDate']
    daysAwarded = request.POST['daysAwarded']
    adminNotes = request.POST['adminNotes']
    
    lProbation = Probation.objects.filter(mid=cMid).order_by('-startDate')
      
    for p in lProbation :
        if p.startDate < date.today() and p.startDate + timedelta(days=p.daysAwarded) < date.today() :
            startDate = p.startDate + timedelta(days= (p.daysAwarded + 1))

    cDisc = Probation(mid = Mid.objects.get(alpha = alpha),
                       startDate = startDate,
                       daysAwarded = daysAwarded,
                       description = adminNotes,
                       )
    
    cDisc.save()
    
    return HttpResponseRedirect(reverse('discipline:enterProbation')) 

@login_required(redirect_field_name='/')
def assessDiscipline(request):
    #Save entered Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    cDate = date.today()
    
    lR = Restriction.objects.filter(mid__company = cCompany).filter(daysRemaining__gt= 0).order_by('startDate')
    lT = Tours.objects.filter(mid__company = cCompany).filter(toursRemaining__gt= 0).order_by('startDate')
    
    lP = Probation.objects.filter(mid__company = cCompany).order_by('startDate')
    
    return render_to_response('discipline/assessDiscipline.html', { 'cCompany' : cCompany, 
                                                                    'lR' : lR,
                                                                    'lT' : lT,
                                                                    'lP' : lP,
                                                                    },
                                                                    context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def updateDiscipline(request):
    #Save entered Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    lR = Restriction.objects.filter(mid__company = cCompany).filter(daysRemaining__gt= 0).order_by('startDate')
    lT = Tours.objects.filter(mid__company = cCompany).filter(toursRemaining__gt= 0).order_by('startDate')                                     
    
    for p in lR :
        if request.POST[p.id+'R'] == "true" :
            p.daysRemaining = p.daysRemaining - 1
            p.save()
    
    for p in lT :
        if request.POST[p.id+'T'] == "true" :
            p.toursRemaining = p.toursRemaining - 1
            p.save()
    
    return HttpResponseRedirect(reverse('discipline:assessDiscipline')) 


