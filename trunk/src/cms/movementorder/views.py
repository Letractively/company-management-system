#ACHTUNG!!! A bit of testing in the very last function: lPart query

#MOs veiws.py
# Author: Dimitri Hatley

from mid.models import Mid

from movementorder.models import MovementOrder
from movementorder.models import MOParticipant

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
def MO(request):
    #Basic user view for MO-s
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #lChits - list of user's MO-s
    lMO = MovementOrder.objects.filter(moparticipant__participant = cMid).exclude(returnDate = "3000-01-01").order_by('-departDate')
    lAllMO = MovementOrder.objects.filter(returnDate = "3000-01-01").order_by('-departDate')
    
    temp = MovementOrder.objects.filter(moparticipant__participant = cMid).filter(returnDate = "3000-01-01")
    
    #Current date 
    cDate = date.today()
    
    #Check if the user is currently on MO
    cMO = None
    for p in temp :
        cMO = p
    
    return render_to_response('movementorder/MO.html', {'cMid' : cMid, 
                                                        'cMO' : cMO, 
                                                        'lMO' : lMO,
                                                        'lAllMO' : lAllMO,
                                                        }, 
                                                        context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def checkOutMO(request):
    #MO check-out and possible creation
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    code = request.POST['code']
    cDate = date(request.POST['returnDateProjected'])
    cTime = time(request.POST['returnTimeProjected'])
    returnDateProjected = datetime(date, cTime.hour(), cTime.minute(), cTime.second())
    
    #New MO
    if code == "0000000" :
        cMO = MovementOrder(organization = request.POST['organization'],
                            movementOrderCode = request.POST['movementOrderCode'],
                            departDate = datetime.now(),
                            returnDateProjected = returnDateProjected,
                            returnDate = "3000-01-01",
                            adminNote = request.POST['adminNotes'],
                            )
        cMO.save()
    else :
        cMO = MovementOrder.objects.get(movementOrderCode = code)
    
    cPart = MOParticipant(MO = cMO,
                          participant = cMid
                          )
    cPart.save()
    
    return HttpResponseRedirect(reverse('movementorder:MO'))

@login_required(redirect_field_name='/')
def checkInMO(request):
    #MO Check-in
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    code = request.POST['code']
    cMO = MovementOrder.objects.get(movementOrderCode = code)
    cMO.returnDate = date.today()
    cMO.save()
    
    return HttpResponseRedirect(reverse('movementorder:MO'))

@login_required(redirect_field_name='/')
def viewMOListCompany(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    lMO = MovementOrder.objects.filter(moparticipant__participant__company = cCompany).filter(returnDate = "3000-01-01").order_by('-departDate').distinct()
    lMids = Mid.objects.filter(company = cCompany).filter(moparticipant__MO__returnDate = "3000-01-01").order_by('alpha')
    
    return render_to_response('movementorder/viewMOListCompany.html', {'lMO' : lMO,
                                                                       'cCompany' : cCompany,
                                                                       'lPart' : lMids
                                                                       }, 
                                                                       context_instance=RequestContext(request))