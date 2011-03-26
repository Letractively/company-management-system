#ORM veiws.py
# Author: Dimitri Hatley

from mid.models import Mid

from orm.models import OrmChit
from orm.models import LeisureActivites
from orm.models import MethodsOfTravel

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
def orm(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    lChits = OrmChit.objects.filter(mid=cMid).order_by('-date')
    
    return render_to_response('orm/orm.html', {'cMid' : cMid, 
                                               'lChits' : lChits,
                                              }, 
                                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def addLeisure(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)

    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    dateDepart = request.POST['dateDepart']
    dateReturn = request.POST['dateReturn']
    daysLeave = timedelta(dateReturn - dateDepart);
    daysTravel = request.POST['daysTravel']
    travelRatio = daysTravel / daysLeave

    #ORM Chit not complete
    approvalStatus = -2   
    
    cChit = SpecialRequestChit(mid = cMid,
                               date = date.today(),            
                               street1 = request.POST['street1'],
                               street2 = request.POST['street2'],
                               city = request.POST['city'],
                               state = request.POST['state'],
                               zip = request.POST['zip'],
                               altPhone = request.POST['altPhone'],
                               dateDepart = dateDepart,
                               dateReturn = dateReturn,
                               daysTravel = daysTravel,
                               daysLeave = daysLeave,
                               travelRatio = travelRatio,
                               riskMitigationPlan = request.POST['street1'],
                               approvalLevel = 4,
                               approvalStatus = approvalStatus
                               )
    cChit.save()
    
    lLeisure = LeisureActivites.objects.filter(OrmChit = cChit)
    
    return render_to_response('orm/ormLeisure.html', {'cMid' : cMid, 
                                               'lChits' : lChits,
                                               'lLeisure' : lLeisure,
                                              }, 
                                              context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveLeisure(request) :
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    lChits = OrmChit.objects.filter(mid=cMid).order_by('-date')
    cChit = lChits[0]
    
    lLeisure = LeisureActivites.objects.filter(OrmChit = cChit)
    
    return render_to_response('orm/ormLeisure.html', {'cMid' : cMid, 
                                               'cChit' : cChit,
                                               'lChits' : lChits,
                                               'lLeisure' : lLeisure,
                                              }, 
                                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def ormView(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    cChit = OrmChit.objects.get(id=request.POST['id'])
    
    return render_to_response('orm/ormView.html', {'cMid' : cMid, 
                                                   'cChit' : cChit,
                                                   'lLeisure' : lLeisure,
                                                   'lTravel' : lTravel,
                                                   }, 
                                                  context_instance=RequestContext(request))
