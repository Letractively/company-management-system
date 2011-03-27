#medchits veiws.py
#Author: Dimitri Hatley

from mid.models import Mid

from form1.models import Form1

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date

@login_required(redirect_field_name='/')
def formOne(request):
    #Basic user view for Form-1s
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #lWeekends - list of user's medical chits
    lForms = Form1.objects.filter(mid=cMid).order_by('-formDate')
    
    return render_to_response('form1/formOne.html', {'cMid' : cMid,  
                                                     'lFormOnes' : lForms,
                                                    }, 
                                                    context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def formOneView(request):
    #Basic view for review of a Form-1
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cForm = Form1.objects.get(id=request.POST['id'])
    
    return render_to_response('form1/formOneView.html', {'cMid' : cMid,  
                                                         'cForm' : cForm,
                                                        }, 
                                                        context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def formOneSelect(request):
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    lMids = Mid.objects.filter(company = cCompany).order_by('alpha')
    
    return render_to_response('form1/formOneSelect.html', {'cMid' : cMid,  
                                                                  'lMids' : lMids,
                                                                  }, 
                                                                  context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def formOneSubmit(request):
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cInspectee = Mid.objects.get(alpha=request.POST['mid'])
    
    return render_to_response('form1/formOneSubmit.html', {'cMid' : cMid,  
                                                           'cInspectee' : cInspectee,
                                                           }, 
                                                           context_instance=RequestContext(request))

@login_required(redirect_field_name='/')    
def formOneSave(request) :
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cInspectee = Mid.objects.get(alpha=request.POST['alpha'])
    
    cForm = Form1(mid = cInspectee,
                  formType = request.POST['type'],
                  formDate = date.today(),
                  counseledBy = cMid,
                  reason = request.POST['reason'],
                  comment = request.POST['comment'],
                  resolution = "P"
                  )
    
    cForm.save()
    
    return HttpResponseRedirect(reverse('form1:formOneSelect'))