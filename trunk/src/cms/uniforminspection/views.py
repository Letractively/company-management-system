from mid.models import Mid

from uniforminspection.models import UniformInspection

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date

@login_required(redirect_field_name='/')
def uIns(request):
    #Basic user view for Form-1s
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
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
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cuIns = UniformInspection.objects.get(id=request.POST['id'])
    
    return render_to_response('uniforminspection/uInsView.html', {'cMid' : cMid,  
                                                                  'cuIns' : cuIns,
                                                                  }, 
                                                                  context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def uInsSelect(request):
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    lMids = Mid.objects.order_by('alpha')
    
    return render_to_response('uniforminspection/uInsSelect.html', {'cMid' : cMid,  
                                                                    'lMids' : lMids,
                                                                    }, 
                                                                    context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def uInsSubmit(request):
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cInspectee = request.POST['mid']
    cInspectee = Mid.objects.get(alpha=cInspectee)
    
    return render_to_response('uniforminspection/uInsSubmit.html', {'cMid' : cMid,  
                                                                    'cInspectee' : cInspectee,
                                                                    }, 
                                                                    context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def uInsSave(request) :
     
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cInspectee = Mid.objects.get(alpha=request.POST['alpha'])
      
    cScore = 0
    
    if request.POST.__contains__ ('groomingShave'):
        cScore = cScore+1
        groomingShave = True
    else :
        groomingShave = False
    
    if request.POST.__contains__ ('groomingLength'):
        cScore = cScore+1
        groomingLength = True
    else :
        groomingLength = False
    
    if request.POST.__contains__ ('groomingAppearance'):
        cScore = cScore+1
        groomingAppearance = True
    else :
        groomingAppearance = False
    
    if request.POST.__contains__ ('missingItems'):
        cScore = cScore+1
        missingItems = True
    else :
        missingItems = False
        
    if request.POST.__contains__ ('appearance'):
        cScore = cScore+1
        appearance = True
    else :
        appearance = False
        
    if request.POST.__contains__ ('IPs'):
        cScore = cScore+1
        IPs = True
    else :
        IPs = False
        
    if request.POST.__contains__ ('dust'):
        cScore = cScore+1
        dust = True
    else :
        dust = False
        
    if request.POST.__contains__ ('coverDirtRing'):
        cScore = cScore+1
        coverDirtRing = True
    else :
        coverDirtRing = False
        
    if request.POST.__contains__ ('coverCleanBill'):
        cScore = cScore+1
        coverCleanBill = True
    else :
        coverCleanBill = False
        
    if request.POST.__contains__ ('ribbons'):
        cScore = cScore+1
        ribbons = True
    else :
        ribbons = False
    
    if request.POST.__contains__ ('shirtInsigniaPlacement'):
        cScore = cScore+1
        shirtInsigniaPlacement = True
    else :
        shirtInsigniaPlacement = False
    
    if request.POST.__contains__ ('shirtProperTie'):
        cScore = cScore+1
        shirtProperTie = True
    else :
        shirtProperTie = False
    
    if request.POST.__contains__ ('IDProperlyDisplayed'):
        cScore = cScore+1
        IDProperlyDisplayed = True
    else :
        IDProperlyDisplayed = False
    
    if request.POST.__contains__ ('shirtUndershirt'):
        cScore = cScore+1
        shirtUndershirt = True
    else :
        shirtUndershirt = False
        
    if request.POST.__contains__ ('creasesPresent'):
        cScore = cScore+1
        creasesPresent = True
    else :
        creasesPresent = False
        
    if request.POST.__contains__ ('beltBuckleTip'):
        cScore = cScore+1
        beltBuckleTip = True
    else :
        beltBuckleTip = False
        
    if request.POST.__contains__ ('gigLine'):
        cScore = cScore+1
        gigLine = True
    else :
        gigLine = False
        
    if request.POST.__contains__ ('trousersProperLength'):
        cScore = cScore+1
        trousersProperLength = True
    else :
        trousersProperLength = False
        
    if request.POST.__contains__ ('shinedShoes'):
        cScore = cScore+1
        shinedShoes = True
    else :
        shinedShoes = False
   
    if cScore < 15 :
        cFail = True
    else :
        cFail = False
    
    cuIns = UniformInspection(inspector = cMid,
                              mid = cInspectee,
                              inspectionDate = date.today(),
                              score = cScore,
                              groomingShave = groomingShave,
                              groomingLength = groomingLength,
                              groomingAppearance = groomingAppearance, 
                              missingItems = missingItems,
                              appearance = appearance,
                              IPs = IPs,
                              dust = dust,
                              coverDirtRing = coverDirtRing,
                              coverCleanBill = coverCleanBill,
                              ribbons = ribbons,
                              shirtInsigniaPlacement = shirtInsigniaPlacement,
                              shirtProperTie = shirtProperTie,
                              IDProperlyDisplayed = IDProperlyDisplayed,
                              shirtUndershirt = shirtUndershirt,
                              creasesPresent = creasesPresent,
                              beltBuckleTip = beltBuckleTip,
                              gigLine = gigLine,
                              trousersProperLength = trousersProperLength,
                              shinedShoes = shinedShoes,
                              comment=request.POST['comment'])
    
    cuIns.save()

    return HttpResponseRedirect(reverse('uInsSelect'))