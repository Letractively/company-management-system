from mid.models import Mid

from bravoinspection.models import BravoInspection

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='/')
def bIns(request):
    #Basic user view for Form-1s
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]    
    cRoom = cMid.roomNumber
    
    #lWeekends - list of user's medical chits
    lbIns = BravoInspection.objects.filter(room=cRoom).order_by('-inspectionDate')
    
    return render_to_response('bravoinspection/bIns.html', {'cMid' : cMid,  
                                                            'lbIns' : lbIns,
                                                            }, 
                                                            context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def bInsView(request):
    #Basic view for review of a Form-1
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cbIns = BravoInspection.objects.filter(id=request.POST['id'])
    cbIns = cbIns[0]
    
    return render_to_response('bravoinspection/bInsView.html', {'cMid' : cMid,  
                                                                'cbIns' : cbIns,
                                                                }, 
                                                                context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def bInsSubmit(request):

    return HttpResponseRedirect(reverse('bIns'))