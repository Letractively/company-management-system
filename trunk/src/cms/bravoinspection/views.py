from mid.models import Mid
from mid.models import Room

from bravoinspection.models import BravoInspection

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date

@login_required(redirect_field_name='/')
def bIns(request):
    #Basic user view for Form-1s
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cRoom = cMid.roomNumber
    
    #lWeekends - list of user's medical chits
    lbIns = BravoInspection.objects.filter(room=cRoom).order_by('-inspectionDate')
    
    return render_to_response('bravoinspection/bIns.html', {'cMid' : cMid,
                                                            'lbIns' : lbIns,
                                                            }, 
                                                            context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def bInsView(request):
    #Basic view for review of a Form-1
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cbIns = BravoInspection.objects.get(id=request.POST['id'])
    
    return render_to_response('bravoinspection/bInsView.html', {'cMid' : cMid,  
                                                                'cbIns' : cbIns,
                                                                }, 
                                                                context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def bInsSelect(request):
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    lRooms = Room.objects.filter(company = cCompany).order_by('roomNumber')
    
    return render_to_response('bravoinspection/bInsSelect.html', {'cMid' : cMid,  
                                                                  'lRooms' : lRooms,
                                                                  }, 
                                                                  context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def bInsSubmit(request):
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cRoom = Room.objects.get(roomNumber=request.POST['room'])
    
    return render_to_response('bravoinspection/bInsSubmit.html', {'cMid' : cMid,  
                                                                  'cRoom' : cRoom,
                                                                  }, 
                                                                  context_instance=RequestContext(request))

@login_required(redirect_field_name='/')    
def bInsSave(request) :
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cRoom = Room.objects.get(roomNumber=request.POST['roomNumber'])
      
    cScore = 0
    
    if request.POST.__contains__ ('deck'):
        cScore = cScore+1
        deck = True
    else :
        deck = False
    
    if request.POST.__contains__ ('laundry'):
        cScore = cScore+1
        laundry = True
    else :
        laundry = False
    
    if request.POST.__contains__ ('mold'):
        cScore = cScore+1
        mold = True
    else :
        mold = False
    
    if request.POST.__contains__ ('door'):
        cScore = cScore+1
        door = True
    else :
        door = False
        
    if request.POST.__contains__ ('electronics'):
        cScore = cScore+1
        electronics = True
    else :
        electronics = False
        
    if request.POST.__contains__ ('dust'):
        cScore = cScore+1
        dust = True
    else :
        dust = False
        
    if request.POST.__contains__ ('bulkheads'):
        cScore = cScore+1
        bulkheads = True
    else :
        bulkheads = False
        
    if request.POST.__contains__ ('racks'):
        cScore = cScore+1
        racks = True
    else :
        racks = False
        
    if request.POST.__contains__ ('furniture'):
        cScore = cScore+1
        furniture = True
    else :
        furniture = False
        
    if request.POST.__contains__ ('felt'):
        cScore = cScore+1
        felt = True
    else :
        felt = False
    
    if request.POST.__contains__ ('gear'):
        cScore = cScore+1
        gear = True
    else :
        gear = False
    
    if request.POST.__contains__ ('conLockers'):
        cScore = cScore+1
        conLockers = True
    else :
        conLockers = False
    
    if request.POST.__contains__ ('blinds'):
        cScore = cScore+1
        blinds = True
    else :
        blinds = False
    
    if request.POST.__contains__ ('boxes'):
        cScore = cScore+1
        boxes = True
    else :
        boxes = False
        
    if request.POST.__contains__ ('corkBoard'):
        cScore = cScore+1
        corkBoard = True
    else :
        corkBoard = False
        
    if request.POST.__contains__ ('computer'):
        cScore = cScore+1
        computer = True
    else :
        computer = False
        
    if request.POST.__contains__ ('rugs'):
        cScore = cScore+1
        rugs = True
    else :
        rugs = False
        
    if request.POST.__contains__ ('midRegs'):
        cScore = cScore+1
        midRegs = True
    else :
        midRegs = False
        
    if request.POST.__contains__ ('shower'):
        cScore = cScore+1
        shower = True
    else :
        shower = False
        
    if request.POST.__contains__ ('medicineCabinets'):
        cScore = cScore+1
        medicineCabinets = True
    else :
        medicineCabinets = False

    if request.POST.__contains__ ('brightWork'):
        cScore = cScore+1
        brightWork = True
    else :
        brightWork = False
        
    if request.POST.__contains__ ('materialDeficiencies'):
        cScore = cScore+1
        materialDeficiencies = True
    else :
        materialDeficiencies = False
        
    if request.POST.__contains__ ('rifles'):
        cScore = cScore+1
        rifles = True
    else :
        rifles = False
   
    if not deck or not laundry or not mold or not door or cScore < 3 :
        cFail = True
    else :
        cFail = False
    
    cbIns = BravoInspection(inspector = cMid,
                            room = cRoom,
                            score = cScore,
                            fail = cFail,
                            inspectionDate = date.today(),
                            deck = deck,
                            laundry = laundry,
                            mold = mold,
                            door = door,
                            electronics = electronics,
                            dust = dust,
                            bulkheads = bulkheads,
                            racks = racks,
                            furniture = furniture,
                            felt = felt,
                            gear = gear,
                            conLockers = conLockers,
                            blinds = blinds,
                            boxes = boxes,
                            corkBoard = corkBoard,
                            computer = computer,
                            rugs = rugs,
                            midRegs = midRegs,
                            shower = shower,
                            medicineCabinets = medicineCabinets,
                            brightWork = brightWork,
                            materialDeficiencies = materialDeficiencies,
                            rifles = rifles,
                            comment=request.POST['comment'])
    
    cbIns.save()

    return HttpResponseRedirect(reverse('bravoinspection:bInsSelect'))