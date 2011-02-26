# Author: Dimitri Hatley

from mid.models import Mid

from medchits.models import Chit

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date
from datetime import timedelta

@login_required(redirect_field_name='/')
def index(request):
    #Basic user view for medical chits
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #lWeekends - list of user's medical chits
    lChits = Chit.objects.filter(mid=cMid).order_by('-endDate')
    
    #Current date 
    cDate = date.today()
    
    #Check if the user is currently on chit
    cChit = None
    endDate = cDate
    for p in lChits :
        if p.endDate > cDate :
            if p.endDate < endDate :
                cChit = p
                endDate = p.endDate
    
    return render_to_response('weekends/weekend.html', {'cMid' : cMid, 
                                                        'cChit' : cChit, 
                                                        'lChits' : lChits,
                                                        }, 
                                                        context_instance=RequestContext(request))
