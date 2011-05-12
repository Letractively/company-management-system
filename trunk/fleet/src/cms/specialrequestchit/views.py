#SpecialRequests veiws.py
# Author: Dimitri Hatley

from mid.models import Mid
from mid.models import Billet

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
    
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    lChits = SpecialRequestChit.objects.filter(mid=cMid).order_by('-date')
    
    return render_to_response('specialrequestchit/specReq.html', {'cMid' : cMid, 
                                                                  'lBillets' : lBillets,
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
        approvalLevel = 4
    
    if request.POST['to'] == "CSEL" :
        approvalLevel = 5
    
    if request.POST['to'] == "CO" :
        approvalLevel = 6    
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    cChit = SpecialRequestChit(mid = cMid,
                               date = date.today(),
                               toLine = request.POST['to'],
                               fromLine = cMid.fName + " " + cMid.mName + " " + cMid.LName,
                               viaLine = "Chain of Command",
                               requestType = request.POST['type'],
                               otherRequestType = request.POST['otherType'],
                               justification = request.POST['justification'],
                               approvalLevel = approvalLevel,
                               approvalStatus = 1,
                               slComment = "",
                               pcComment = "",
                               ccComment = "",
                               selComment = "",
                               coComment = ""
                               )
    cChit.save()
    
    if cMid.squad == "O" or cMid.squad == "S" :
         cChit.approvalStatus = 2
         cChit.slApproval = True
         cChit.slComment = "DEFAULT"
         cChit.save()
         
    if cMid.platoon == "O" or cMid.platoon == "S" :
         cChit.approvalStatus = 4
         cChit.pcApproval = True
         cChit.pcComment = "DEFAULT"
         cChit.save()
    
    for p in lBillets :
        if p.billet == "CC" and p.current :
            cChit.approvalStatus = 5
            cChit.slApproval = True
            cChit.slComment = "DEFAULT"
            cChit.pcApproval = True
            cChit.pcComment = "DEFAULT"
            cChit.ccApproval = True
            cChit.ccComment = "DEFAULT"
            
        if p.billet == "XO" and p.current :
            cChit.approvalStatus = 4
            cChit.slApproval = True
            cChit.slComment = "DEFAULT"
            cChit.pcApproval = True
            cChit.pcComment = "DEFAULT"
            
        if p.billet == "OPS" and p.current :
            cChit.approvalStatus = 4
            cChit.slApproval = True
            cChit.slComment = "DEFAULT"
            cChit.pcApproval = True
            cChit.pcComment = "DEFAULT"
            
        if p.billet == "FSGT" and p.current :
            cChit.approvalStatus = 4
            cChit.slApproval = True
            cChit.slComment = "DEFAULT"
            cChit.pcApproval = True
            cChit.pcComment = "DEFAULT"
        
        if p.billet == "PC" and p.current :
            cChit.approvalStatus = 4
            cChit.slApproval = True
            cChit.slComment = "DEFAULT"
            cChit.pcApproval = True
            cChit.pcComment = "DEFAULT"
            
        if p.billet == "PLTS" and p.current :
            cChit.approvalStatus = 2
            cChit.slApproval = True
            cChit.slComment = "DEFAULT"
        
        if p.billet == "SL" and p.current :
            cChit.approvalStatus = 2
            cChit.slApproval = True
            cChit.slComment = "DEFAULT"
            
    cChit.save()
    
    if cChit.approvalLevel < cChit.approvalStatus :
        cChit.approvalStatus = 10
    
    cChit.save()
    
    return HttpResponseRedirect(reverse('specialrequestchit:specReq'))

@login_required(redirect_field_name='/')
def specReqView(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    cChit = SpecialRequestChit.objects.get(id=request.POST['id'])
    
    return render_to_response('specialrequestchit/specReqView.html', {'cMid' : cMid, 
                                                                      'lBillets' : lBillets,
                                                                      'cChit' : cChit,
                                                                      }, 
                                                                      context_instance=RequestContext(request))