#medchits veiws.py
#Author: Dimitri Hatley

from mid.models import Mid
from mid.models import Billet

from form1.models import Form1

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date

@login_required(redirect_field_name='/')
def form1(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    firstie = False
    if cMid.rank == "1" :
        firstie = True
    
    lMids = Mid.objects.filter(company = cCompany).exclude(alpha = cMid.alpha)
    lForms = Form1.objects.filter(mid=cMid).order_by('-formDate')
    
    return render_to_response('form1/formOne.html', {'cMid' : cMid, 
                                                     'lBillets' : lBillets,
                                                     'firstie' : firstie, 
                                                     'lMids' : lMids,
                                                     'lFormOnes' : lForms,
                                                    }, 
                                                    context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')    
def form1Save(request) :
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cForm = Form1(mid = Mid.objects.get(alpha=request.POST['mid']),
                  formType = request.POST['type'],
                  formDate = date.today(),
                  counseledBy = cMid,
                  reason = request.POST['reason'],
                  comment = request.POST['comment'],
                  resolution = "P"
                  )
    
    cForm.save()
    
    return HttpResponseRedirect(reverse('form1:form1'))

@login_required(redirect_field_name='/')
def form1View(request):
    #Basic view for review of a Form-1
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    lBillets = Billet.objects.filter(mid = cMid).filter(current = True)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cForm = Form1.objects.get(id=request.POST['id'])
    
    return render_to_response('form1/formOneView.html', {'cMid' : cMid,
                                                         'lBillet' : lBillet, 
                                                         'cForm' : cForm,
                                                        }, 
                                                        context_instance=RequestContext(request))

