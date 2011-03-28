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
    dateDepart = dateDepart.split('-')
    dateDepart = date(int(dateDepart[0]), int(dateDepart[1]), int(dateDepart[2]))
    
    dateReturn = request.POST['dateReturn']
    dateReturn = dateReturn.split('-')
    dateReturn = date(int(dateReturn[0]), int(dateReturn[1]), int(dateReturn[2]))
    
    daysLeave = dateReturn - dateDepart;
    daysLeave = daysLeave.days;
    daysTravel = request.POST['daysTravel']
    travelRatio = int(daysTravel) / int(daysLeave)

    #ORM Chit not complete
    approvalStatus = -2   
    
    cChit = OrmChit(mid = cMid,
                               date = date.today(),            
                               street1 = request.POST['street1'],
                               street2 = request.POST['street2'],
                               city = request.POST['city'],
                               state = request.POST['state'],
                               zip = request.POST['zip'],
                               dateDepart = dateDepart,
                               dateReturn = dateReturn,
                               daysTravel = daysTravel,
                               daysLeave = daysLeave,
                               travelRatio = travelRatio,
                               approvalLevel = 6,
                               approvalStatus = approvalStatus
                               )
    cChit.save()
    
    lLeisure = LeisureActivites.objects.filter(OrmChit = cChit)
    
    return render_to_response('orm/ormLeisure.html', {'cMid' : cMid, 
                                                      'cChit' : cChit,
                                                      'lLeisure' : lLeisure,
                                                      }, 
                                                      context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveLeisure(request) :
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    lChits = OrmChit.objects.filter(mid=cMid).order_by('-date')
    cChit = OrmChit.objects.get(id=request.POST['id'])
    
    cLeisure = LeisureActivites(OrmChit = cChit,
                                activity = request.POST['activity'],
                                duration = request.POST['duration'],
                                RAC = request.POST['RAC']
                                )
    cLeisure.save()
    
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
    
    lLeisure = LeisureActivites.objects.filter(OrmChit = cChit)
    
    return render_to_response('orm/ormView.html', {'cMid' : cMid, 
                                                   'cChit' : cChit,
                                                   'lLeisure' : lLeisure,
                                                   #'lTravel' : lTravel,
                                                   }, 
                                                  context_instance=RequestContext(request))
