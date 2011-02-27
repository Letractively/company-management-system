from mid.models import Mid

from form1.models import Form1

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='/')
def uIns(request):
    #Basic user view for Form-1s
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #lWeekends - list of user's medical chits
    uIns = UniformInspection.objects.filter(mid=cMid).order_by('-dateTime')
    
    return render_to_response('form1/uIns.html', {'cMid' : cMid,  
                                                  'luIns' : luIns,
                                                 }, 
                                                 context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def uInsView(request):
    #Basic view for review of a Form-1
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cuIns = UniformInspection.objects.filter(id=request.POST['id'])
    cuIns = cuIns[0]
    
    return render_to_response('form1/uInsView.html', {'cMid' : cMid,  
                                                      'cuIns' : cuIns,
                                                     }, 
                                                     context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def uInsSubmit(request):

    return HttpResponseRedirect(reverse('uIns'))