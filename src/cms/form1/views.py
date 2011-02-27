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

@login_required(redirect_field_name='/')
def formOne(request):
    #Basic user view for Form-1s
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #lWeekends - list of user's medical chits
    lForms = Form1.objects.filter(mid=cMid).order_by('-dateTime')
    
    return render_to_response('form1/formOne.html', {'cMid' : cMid,  
                                                     'lForms' : lForms,
                                                    }, 
                                                    context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def viewFormOne(request):
    #Basic view for review of a Form-1
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cForm = Form1.objects.filter(id=request.POST['id'])
    cForm = cForm[0]
    
    return render_to_response('form1/formOne.html', {'cMid' : cMid,  
                                                     'cForm' : cForm,
                                                    }, 
                                                    context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def submit(request):

    return HttpResponseRedirect(reverse('formOne'))