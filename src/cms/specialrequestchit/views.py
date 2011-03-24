#medchits veiws.py
# Author: Dimitri Hatley

from mid.models import Mid

from specialrequestchit.models import SpecialRequestChit

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date

@login_required(redirect_field_name='/')
def specReq(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    lChits = SpecialRequestChit.objects.filter(mid=cMid).order_by('-date')
    
    return render_to_response('specialrequestchit/specReq.html', {'cMid' : cMid, 
                                                                  'lChits' : lChits,
                                                                  }, 
                                                                  context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def specReqSubmit(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)

    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    approvalLevel = 0
    
    if request.POST['to'] == "SL" :
        approvalLevel = 1
    
    if request.POST['to'] == "PL" :
        approvalLevel = 2
    
    if request.POST['to'] == "CC" :
        approvalLevel = 3
    
    if request.POST['to'] == "CSEL" :
        approvalLevel = 4
    
    if request.POST['to'] == "CO" :
        approvalLevel = 5    
    
    cChit = SpecialRequestChit(mid = cMid,
                               date = date.today(),
                               toLine = request.POST['to'],
                               fromLine = cMid.fName + " " + cMid.mName + " " + cMid.LName,
                               viaLine = "Chain of Command",
                               requestType = request.POST['type'],
                               otherRequestType = request.POST['otherType'],
                               justification = request.POST['justification'],
                               approvalLevel = approvalLevel,
                               approvalStatus = 1)
    cChit.save()
    
    return HttpResponseRedirect(reverse('specReq'))

@login_required(redirect_field_name='/')
def specReqView(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    cChit = SpecialRequestChit.objects.get(id=request.POST['id'])
    
    return render_to_response('specialrequestchit/specReqView.html', {'cMid' : cMid, 
                                                                      'cChit' : cChit,
                                                                      }, 
                                                                      context_instance=RequestContext(request))