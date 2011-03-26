#companywatch veiws.py
# Author: Michael Harrison

from mid.models import Mid
from companywatch import AcYear
from companywatch import AcWatch
from companywatch import WatchBill
from companywatch import Watch
from companywatch import LogBook
from companywatch import LogEntry

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date


@login_required(redirect_field_name='/')
def AcYear(request):
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
    
    
    
    
    
    
