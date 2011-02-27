from mid.models import Mid

from uniforminspection.models import UniformInspection

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
    luIns = UniformInspection.objects.filter(mid=cMid).order_by('-inspectionDate')
    
    return render_to_response('uniforminspection/uIns.html', {'cMid' : cMid,  
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
    
    return render_to_response('uniforminspection/uInsView.html', {'cMid' : cMid,  
                                                                  'cuIns' : cuIns,
                                                                  }, 
                                                                  context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def uInsSelect(request):
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    lMids = Mid.objects.order_by('alpha')
    
    return render_to_response('uniforminspection/uInsSelect.html', {'cMid' : cMid,  
                                                                    'lMids' : lMids,
                                                                    }, 
                                                                    context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def uInsSubmit(request):
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.filter(alpha=alpha)
    cMid = cMid[0]
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cInspectee = request.POST['mid']
    cInspectee = Mid.objects.filter(alpha=cInspectee)
    cInspectee = cInspectee[0]
    
    return render_to_response('uniforminspection/uInsSubmit.html', {'cMid' : cMid,  
                                                                    'cInspectee' : cInspectee,
                                                                    }, 
                                                                    context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def uInsSave(request) :
    
    return HttpResponseRedirect(reverse('uIns'))