#medchits veiws.py
# Author: Dimitri Hatley

from mid.models import Mid
from mid.models import Billet

from medchits.models import Chit

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date
from datetime import timedelta

@login_required(redirect_field_name='/')
def medchits(request):
    #Basic user view for medical chits
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    #lChits - list of user's medical chits
    lChits = Chit.objects.filter(mid=cMid).order_by('-endDate')
    
    #Current date 
    cDate = date.today()
    
    #Check if the user is currently on chit
    cChit = None
    endDate = cDate+timedelta(days=365);
    for p in lChits :
        if p.endDate > cDate :
            if p.endDate < endDate :
                cChit = p
                endDate = p.endDate
    
    return render_to_response('medchits/medchit.html', {'cMid' : cMid, 
                                                        'lBillets' : lBillets,
                                                        'cChit' : cChit, 
                                                        'lChits' : lChits,
                                                        }, 
                                                        context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def medChitSubmit(request):
    #Medchit submission
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    lChits = Chit.objects.filter(mid=cMid).order_by('-endDate')
    
    #Check for repeated start date; avoid multiple submissions
    startDate = request.POST['startDate']
    
    repeat = False
    for p in lChits :
        if p.startDate == startDate :
            repeat = True
    
    if not repeat :
        cChit = Chit(mid = cMid,
                     diagnosis = request.POST['diagnosis'],
                     startDate = request.POST['startDate'],
                     endDate = request.POST['endDate'],
                     disposition = request.POST['disposition'],
                     adminNotes = request.POST['adminNotes'])
        cChit.save()
    
    return HttpResponseRedirect(reverse('medchits:medchits'))