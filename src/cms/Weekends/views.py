from cms.MID.models import Mid
from cms.MID.models import Billets
from cms.Weekends.models import Weekend
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='')
def index(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]

    cMid = Mid.objects.filter(Alpha=alpha)
    cMid = cMid[0]
    #cBillets = Billets.objects.filter(mid=cMid)
    
    #cWeekend - list of currently taken weekends
    cWeekend = Weekend.objects.filter(mid=cMid).order_by(-Startdate)
    
    #WT - Weekends Taken
    WT = len(cWeekend)
    
    #WL - Weekends Left
    WL = cMid.Weekends - WT
    
    #WE - Weekend Eligible
    if cMid.Weekends > 0 and cMid.AcSAT and cMid.PRTSAT :
        WE = True 

    return render_to_response('Weekends/weekend.html', { 'mid' : cMid, 'cWeekend' : cWeekend, 
                                                        'WT' : WT, 'WL' : WL, 'WE' : WE })