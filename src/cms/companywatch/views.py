#companywatch veiws.py
# Author: Michael Harrison

from mid.models import Mid
from mid.models import Billet
from companywatch.models import AcYear
from companywatch.models import AcWatch
from companywatch.models import WatchBill
from companywatch.models import Watch
from companywatch.models import LogBook
from companywatch.models import LogEntry

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date


@login_required(redirect_field_name='/')
def AcYearView(request):
    #check to make sure the reqester is the Company Adj.
    #get requesting username and alpha
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    
    #get the MIDN object and set the company variable
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
  
    #get list of MIDN current billets
    cBillets = Billet.objects.filter(mid=cMid)
  
    isAdj = False
    #go through list of MIDN billets and check for ADJ and if it is current
    for i in cBillets:
        if i.billet == 'ADJ' and i.current:
            isAdj = True
    # if either of these statements are false then redirect back to /
    if not isAdj:
        return HttpResponseRedirect('/')
    
    year = date.today().strftime("%y")
    acYear = AcYear.objects.get(acYear=year)
    return render_to_response('companywatch/AcYearView.html', { 'acYear': acYear },context_instance=RequestContext(request))

def AcYearEdit(request):
    #check to make sure the reqester is the Company Adj.
    #get requesting username and alpha
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    
    #get the MIDN object and set the company variable
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
  
    #get list of MIDN current billets
    cBillets = Billet.objects.filter(mid=cMid)
  
    isAdj = False
    #go through list of MIDN billets and check for ADJ and if it is current
    for i in cBillets:
        if i.billet == 'ADJ' and i.current:
            isAdj = True
    # if either of these statements are false then redirect back to /
    if not isAdj:
        return HttpResponseRedirect('/')
    year = date.today().strftime("%y")
    acYear = AcYear.objects.get(acYear=year)
    
    return render_to_response('companywatch/AcYearEdit.html',{'acYear':acYear},context_instance=RequestContext(request))

def AcYearSubmit(request):
    #check to make sure the reqester is the Company Adj.
    #get requesting username and alpha
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    
    #get the MIDN object and set the company variable
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
  
    #get list of MIDN current billets
    cBillets = Billet.objects.filter(mid=cMid)
  
    isAdj = False
    #go through list of MIDN billets and check for ADJ and if it is current
    for i in cBillets:
        if i.billet == 'ADJ' and i.current:
            isAdj = True
    # if either of these statements are false then redirect back to /
    if not isAdj:
        return HttpResponseRedirect('/')

    year = date.today().strftime("%y")
    acYear = AcYear.objects.get(acYear=year)
    
    acYear.isInit =  request.POST['isInit']
    acYear.fallStart =  request.POST['fallStart']
    acYear.fallGoldWeekStart =  request.POST['fallGoldWeekStart']
    acYear.fall6Weeks =  request.POST['fall6Weeks']
    acYear.fall12Weeks =  request.POST['fall12Weeks']
    acYear.thanksgivingStart =  request.POST['thanksgivingStart']
    acYear.thanksgivingEnd =  request.POST['thanksgivingEnd']
    acYear.fallXWeekStart =  request.POST['fallXWeekStart']
    acYear.fallXWeekEnd =  request.POST['fallXWeekEnd']
    acYear.christmasStart =  request.POST['christmasStart']
    acYear.christmasEnd =  request.POST['christmasEnd']
    acYear.christmasIntersessionalStart =  request.POST['christmasIntersessionalStart']
    acYear.christmasIntersessionalEnd =  request.POST['christmasIntersessionalEnd']
    acYear.laborDay =  request.POST['laborDay']
    acYear.columbusDay =  request.POST['columbusDay']
    acYear.veteransDay =  request.POST['veteransDay']
    acYear.fallEnd =  request.POST['fallEnd']
    acYear.startSpring =  request.POST['startSpring']
    acYear.spring6Weeks =  request.POST['spring6Weeks']
    acYear.spring12Weeks =  request.POST['spring12Weeks']
    acYear.springXWeekStart =  request.POST['springXWeekStart']
    acYear.springXWeekEnd =  request.POST['springXWeekEnd']
    acYear.springBreakStart =  request.POST['springBreakStart']
    acYear.springBreakEnd =  request.POST['springBreakEnd']
    acYear.mlkDay =  request.POST['mlkDay']
    acYear.washingtonBirthday =  request.POST['washingtonBirthday']
    acYear.springEnd =  request.POST['springEnd']
    acYear.springIntersessionalStart =  request.POST['springIntersessionalStart']
    acYear.springIntersessionalEnd =  request.POST['springIntersessionalEnd']
    acYear.summerStart =  request.POST['summerStart']
    
    acYear.save()        
            
    return HttpResponseRedirect(reverse('companywatch:AcYearView'))
    
    
    
    
    
