#ACHTUNG: Line 258

#mid views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet
from mid.models import Room
from mid.models import PRT
from mid.models import Discipline
from mid.models import Probation

from specialrequestchit.models import SpecialRequestChit
from orm.models import OrmChit

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from datetime import date
from datetime import timedelta

import re

def loginPage(request):
    #if request.user.is_authenticated:
    #    return HttpResponseRedirect('switchboard')
    #else:
        return render_to_response('mid/loginPage.html', {}, 
                                  context_instance=RequestContext(request))

def logIn(request):
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        
        if user.is_active:
            login(request, user)
            
            if re.match("CO", username) is not None :
                username = username.split('_')
                cCompany = username[1]

                return HttpResponseRedirect('switchboard')
            
            if re.match("SEL", username) is not None :
                username = username.split('_')
                cCompany = username[1]
                
                return HttpResponseRedirect('switchboard')
            
            else :
            
                if re.match("m", username) is not None : 
                
                    alpha = username.split('m')
                    alpha = alpha[1]
        
                    if Mid.objects.filter(alpha = alpha) :
                        
                        return HttpResponseRedirect('switchboard')
                                            
                    #Alpha does not exist in the database, redirect to login with 'noUser' flag TRUE.
                    else :
                        return render_to_response('mid/loginPage.html', { 'noUser' : True }, 
                                                  context_instance=RequestContext(request))
                
                #Non 'mXXXXXX' login entered, redirect to login with with the 'noUser' flag TRUE.
                else :
                    return render_to_response('mid/loginPage.html', {'noUser' : True }, 
                                              context_instance=RequestContext(request))
        
        #Disabled account: should not happen, but here just in case
        else:
            return HttpResponseRedirect('/')
        
    #Wrong password, redirect redirect to login with the 'repeat' flag TRUE    
    else:
        return render_to_response('mid/loginPage.html', { 'repeat' : True,}, 
                                  context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def renderSwitchboard(request) :
    if re.match("CO", request.user.username) is not None :
        return render_to_response('mid/switchboard.html', { 'CO' : True
                                                           },
                                                           context_instance=RequestContext(request))
    
    if re.match("SEL", request.user.username) is not None :
        return render_to_response('mid/switchboard.html', { 'SEL' : True
                                                           },
                                                           context_instance=RequestContext(request))
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha = alpha)
                        
    lBillets = Billet.objects.filter(mid = cMid)
    
    CC = False
    XO = False
    HA = False
    OPS = False
    ADJ = False
    PMO = False
    AC = False
    SAF = False
    APT = False
    ADEO = False
    ATFP = False
    TRN = False
    FLT = False
    ADM = False
    PRO = False
    WRD = False
    DRL = False
    SAVI = False
    CMEO = False
    FIN = False
    FSGT = False
    DRLS = False
    ADMC = False
    MISLO = False
    TRNS1 = False
    TRNS2 = False
    PLTS = False
    PC = False
    SL = False

    firstie = False
    if cMid.rank == "1" :
        firstie = True
    
    for p in lBillets :
        if p.billet == 'CC' and p.current :
            CC = True
    
    for p in lBillets :
        if p.billet == 'XO' and p.current :
            XO = True
    
    for p in lBillets :
        if p.billet == 'HA' and p.current :
            HA = True
            
    for p in lBillets :
        if p.billet == 'OPS' and p.current :
            OPS = True
            
    for p in lBillets :
        if p.billet == 'ADJ' and p.current :
            ADJ = True
            
    for p in lBillets :
        if p.billet == 'PMO' and p.current :
            PMO = True
            
    for p in lBillets :
        if p.billet == 'AC' and p.current :
            AC = True
            
    for p in lBillets :
        if p.billet == 'SAF' and p.current :
            SAF = True
            
    for p in lBillets :
        if p.billet == 'APT' and p.current :
            APT = True
            
    for p in lBillets :
        if p.billet == 'ADEO' and p.current :
            ADEO = True
            
    for p in lBillets :
        if p.billet == 'ATFP' and p.current :
            ATFP = True
            
    for p in lBillets :
        if p.billet == 'TRN' and p.current :
            TRN = True
    
    for p in lBillets :
        if p.billet == 'FLT' and p.current :
            FLT = True
            
    for p in lBillets :
        if p.billet == 'ADM' and p.current :
            ADM = True
            
    for p in lBillets :
        if p.billet == 'PRO' and p.current :
            PRO = True
            
    for p in lBillets :
        if p.billet == 'WRD' and p.current :
            WRD = True
            
    for p in lBillets :
        if p.billet == 'DRL' and p.current :
            DRL = True
            
    for p in lBillets :
        if p.billet == 'SAVI' and p.current :
            SAVI = True
            
    for p in lBillets :
        if p.billet == 'CMEO' and p.current :
            CMEO = True
            
    for p in lBillets :
        if p.billet == 'FIN' and p.current :
            FIN = True
            
    for p in lBillets :
        if p.billet == 'FSGT' and p.current :
            FSGT = True
            
    for p in lBillets :
        if p.billet == 'DRLS' and p.current :
            DRLS = True
            
    for p in lBillets :
        if p.billet == 'ADMC' and p.current :
            ADMC = True
            
    for p in lBillets :
        if p.billet == 'MISLO' and p.current :
            MISLO = True
            
    for p in lBillets :
        if p.billet == 'TRNS1' and p.current :
            TRNS1 = True
            
    for p in lBillets :
        if p.billet == 'TRNS2' and p.current :
            TRNS2 = True
            
    for p in lBillets :
        if p.billet == 'PC' and p.current :
            PC = True
    
    for p in lBillets :
        if p.billet == 'PLTS' and p.current :
            PLTS = True
    
    for p in lBillets :
        if p.billet == 'SL' and p.current :
            SL = True
   
    return render_to_response('mid/switchboard.html', { 'mid' : cMid,
                                                        'firstie' : firstie,
                                                        'CC' : CC,
                                                        'XO'  : XO,
                                                        'HA'  : HA,
                                                        'OPS' : OPS,
                                                        'ADJ' : ADJ,
                                                        'PMO' : PMO,
                                                        'AC'  : AC,
                                                        'SAF' : SAF,
                                                        'APT' : APT,
                                                        'ADEO': ADEO,
                                                        'ATFP': ATFP,
                                                        'TRN' : TRN,
                                                        'FLT' : FLT,
                                                        'ADM' : ADM,
                                                        'PRO' : PRO,
                                                        'WRD' : WRD,
                                                        'DRL' : DRL,
                                                        'SAVI': SAVI,
                                                        'CMEO': CMEO,
                                                        'FIN' : FIN,
                                                        'FSGT': FSGT,
                                                        'TRNS1': TRNS1,
                                                        'TRNS2': TRNS2,
                                                        'DRLS': DRLS,
                                                        'ADMC': ADMC,
                                                        'MISLO': MISLO,
                                                        'PLTS' : PLTS,
                                                        'PC' : PC,
                                                        'SL' : SL
                                                        },
                                                        context_instance=RequestContext(request))



@login_required(redirect_field_name='/')
def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))

@login_required(redirect_field_name='/')
def selectPassChange(request):
    
    return render_to_response('mid/selectPassChange.html', { },
                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')    
def passChange(request) :
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    password = request.POST['password']
    
    cUser = request.user    
    cUser.set_password(password)
    cUser.save()
    
    return HttpResponseRedirect(reverse('mid:switchboard'))

@login_required(redirect_field_name='/')
def editPersonalInformation(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    lRooms = Room.objects.filter(company = cCompany)
    
    return render_to_response('mid/editPersonalInformation.html', {'cMid' : cMid,
                                                                   'lRooms' : lRooms
                                                                   },
                              context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')    
def savePersonalInformation(request) :
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    roomNumber = request.POST['roomNumber']
    roomNumber = Room.objects.get(roomNumber = roomNumber)
    
    cMid.roomNumber = roomNumber
    cMid.phoneNumber = request.POST['phone']
    cMid.CQPR = request.POST['CQPR']
    cMid.SQPR = request.POST['SQPR']
    cMid.performanceGrade = request.POST['perf']
    cMid.conductGrade = request.POST['apt']
    cMid.PRT = request.POST['PRT']
    cMid.save()
    
    return HttpResponseRedirect(reverse('mid:editPersonalInformation'))

@login_required(redirect_field_name='/')
def viewDiscipline(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)

    #lDisc - list of user's errors in judgement
    lDisc = Discipline.objects.filter(mid = cMid)
    lProb = Probation.objects.filter(mid = cMid)
    #Current date 
    cDate = date.today()
    
    #Check if the user is currently on chit
    cDisc = None
    for p in lDisc :
        if p.daysRemaining > 0 :
            cDisc = p
    
    cProb = None
    for p in lProb :
        if p.startDate + timedelta(days = p.daysAwarded) > cDate :
            cProb = p
    
    return render_to_response('mid/viewDiscipline.html', {'cMid' : cMid, 
                                                          'cDisc' : cDisc,
                                                          'lDisc' : lDisc,
                                                          'cProb' : cProb,
                                                          'lProb' : lProb
                                                          },
                                                          context_instance=RequestContext(request))

#Following functions deal with the Admin Officer functionality
@login_required(redirect_field_name='/')
def selectUser(request):
    #Called on /mid/addUser -> polls data, adds both Mid and User objects to the database
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True
        if p.billet == "ADMC" and p.current :
            flagAdmin == True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')
    
    return render_to_response('mid/selectUser.html', { 'lMids' : lMids },
                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def modifyUser(request):
    #Called on /mid/modifyUser -> creates a form for edit/addition of the new user
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True
        if p.billet == "ADMC" and p.current :
            flagAdmin == True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    alpha = request.POST['alpha']
    
    if alpha == '000000' :
        cMid = None
    else :
        cMid = Mid.objects.get(alpha = alpha)
        
    lRooms = Room.objects.filter(company = cCompany).order_by('roomNumber')
    
    return render_to_response('mid/modifyUser.html', { 'cMid' : cMid, 
                                                       'lRooms' : lRooms, },
                              context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')    
def saveUser(request) :
    #Saves a new user/Edits a preexisting user
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True
        if p.billet == "ADMC" and p.current :
            flagAdmin == True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    newUser = request.POST['newUser']
    alpha = request.POST['alpha']
    roomNumber = request.POST['roomNumber']
    roomNumber = Room.objects.get(roomNumber = roomNumber)
    
    #Making sure user with this alpha does not exist
    lMids = Mid.objects.all()
    
    alphaExists = False
    for p in lMids :
        if p.alpha == alpha :
            alphaExists = True
    
    if newUser == "false" :
        cMid = Mid.objects.get(alpha = alpha)
        
        cMid.LName=request.POST['lName'] 
        cMid.mName=request.POST['mName']
        cMid.fName = request.POST['fName']
        cMid.roomNumber = roomNumber
        cMid.phoneNumber = request.POST['phoneNumber']
        cMid.weekends = request.POST['weekends']
        cMid.save()
               
    if newUser == "true" and not alphaExists:
    
    #ACHTUNG: Add dynamic checking based on the current year. 
        if re.match("11", alpha):
            cRank = 1
        elif re.match("12", alpha):
            cRank = 2
        elif re.match("13", alpha):
            cRank = 3
        else:
            cRank = 4
        
        cMid = Mid(alpha=alpha,
                   LName=request.POST['lName'],
                   mName=request.POST['mName'],
                   fName = request.POST['fName'],
                   roomNumber = roomNumber,
                   phoneNumber = request.POST['phoneNumber'],
                   weekends = request.POST['weekends'], 
                   company = cCompany,
                   rank = cRank,
                   acSAT = True,
                   PRTSat = True,
                   CQPR = "0.00",
                   SQPR = "0.00",
                   performanceGrade = "N",
                   conductGrade = "N",
                   PRT = "00.0")
        cMid.save()
        
        cUser = User.objects.create_user('m'+alpha, 'm'+alpha+'@usna.edu', alpha)
        cUser.first_name = request.POST['fName']
        cUser.last_name = request.POST['lName']
        cUser.is_staff = False
        cUser.save()
      
    return HttpResponseRedirect('mid:selectUser')

@login_required(redirect_field_name='/')
def selectPassReset(request):
    #Called on /mid/selectPassReset
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True
        if p.billet == "ADMC" and p.current :
            flagAdmin == True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')
    
    return render_to_response('mid/selectPassReset.html', { 'lMids' : lMids },
                              context_instance=RequestContext(request))

@login_required(redirect_field_name='/')    
def passReset(request) :
    #Resets user's password to his alpha
    
    #Second check - make sure the user is Admin officer
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True
        if p.billet == "ADMC" and p.current :
            flagAdmin == True

    if not flagAdmin :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    alpha = request.POST['alpha']
    
    cUser = User.objects.get(username='m'+alpha)
    cUser.set_password(alpha)
    cUser.save()
    
    return HttpResponseRedirect('mid:selectPassReset')

#Following functions deal with CC's functionality
@login_required(redirect_field_name='/')
def assignBillets(request):
    #Allows CC to appoint company staff
    
    #Saves billet assignment    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagCC = False
    for p in lBillets :
        if p.billet == "CC" and p.current :
            flagCC = True

    if not flagCC :
        return HttpResponseRedirect('/')
    #End of second check
    
    lBillet = Billet.objects.filter(mid__company = cCompany)
    
    L = ['XO', 'HA', 'OPS', 'ADJ', 'PMO', 'AC', 'SAF', 'APT', 'ADEO', 'ATFP', 'TRN', 'FLT', 'ADM', 'PRO',
         'WRD', 'DRL', 'SAVI', 'CMEO', 'FIN', 'FSGT', 'DRLS', 'ADMC', 'MISLO', 'TRNS1', 'TRNS2']
    
    XO = None
    for p in lBillet:
        if p.billet == 'XO' and p.current:
            XO = p
    
    HA = None
    for p in lBillet:
        if p.billet == "HA" and p.current:
            HA = p
    
    OPS = None
    for p in lBillet:
        if p.billet == "OPS" and p.current:
            OPS = p
    
    ADJ = None
    for p in lBillet:
        if p.billet == "ADJ" and p.current:
            ADJ = p
    
    PMO = None
    for p in lBillet:
        if p.billet == "PMO" and p.current:
            PMO = p
    
    AC = None
    for p in lBillet:
        if p.billet == "AC" and p.current:
            AC = p
    
    SAF = None
    for p in lBillet:
        if p.billet == "SAF" and p.current:
            SAF = p
    
    APT = None
    for p in lBillet:
        if p.billet == "APT" and p.current:
            APT = p
    
    ADEO = None
    for p in lBillet:
        if p.billet == "ADEO" and p.current:
            ADEO = p
    
    ATFP = None
    for p in lBillet:
        if p.billet == "ATFP" and p.current:
            ATFP = p
    
    TRN = None
    for p in lBillet:
        if p.billet == "TRN" and p.current:
            TRN = p
    
    FLT = None
    for p in lBillet:
        if p.billet == "FLT" and p.current:
            FLT = p
    
    ADM = None
    for p in lBillet:
        if p.billet == "ADM" and p.current:
            ADM = p
    
    PRO = None
    for p in lBillet:
        if p.billet == "PRO" and p.current:
            PRO = p
    
    WRD = None
    for p in lBillet:
        if p.billet == "WRD" and p.current:
            WRD = p
    
    DRL = None
    for p in lBillet:
        if p.billet == "DRL" and p.current:
            DRL = p
    
    SAVI = None
    for p in lBillet:
        if p.billet == "SAVI" and p.current:
            SAVI = p
    
    CMEO = None
    for p in lBillet:
        if p.billet == "CMEO" and p.current:
            CMEO = p
    
    FIN = None
    for p in lBillet:
        if p.billet == "FIN" and p.current:
            FIN = p
    
    FSGT = None
    for p in lBillet:
        if p.billet == "FSGT" and p.current:
            FSGT = p
    
    TRNS1 = None
    for p in lBillet:
        if p.billet == "TRNS1" and p.current:
            TRNS1 = p
    
    TRNS2 = None
    for p in lBillet:
        if p.billet == "TRNS2" and p.current:
            TRNS2 = p
    
    DRLS = None
    for p in lBillet:
        if p.billet == "DRLS" and p.current:
            DRLS = p
    
    ADMC = None
    for p in lBillet:
        if p.billet == "ADMC" and p.current:
            ADMC = p
    
    MISLO = None
    for p in lBillet:
        if p.billet == "MISLO" and p.current:
            MISLO = p

    lMidsOne = Mid.objects.filter(company=cCompany).filter(rank = "1").order_by('alpha')
    lMidsTwo = Mid.objects.filter(company=cCompany).filter(rank = "2").order_by('alpha')
                                                                                                        
    return render_to_response('mid/assignBillets.html', {'lMidsOne' : lMidsOne, 
                                                         'lMidsTwo' : lMidsTwo,
                                                         'XO'  : XO,
                                                         'HA'  : HA,
                                                         'OPS' : OPS,
                                                         'ADJ' : ADJ,
                                                         'PMO' : PMO,
                                                         'AC'  : AC,
                                                         'SAF' : SAF,
                                                         'APT' : APT,
                                                         'ADEO': ADEO,
                                                         'ATFP': ATFP,
                                                         'TRN' : TRN,
                                                         'FLT' : FLT,
                                                         'ADM' : ADM,
                                                         'PRO' : PRO,
                                                         'WRD' : WRD,
                                                         'DRL' : DRL,
                                                         'SAVI': SAVI,
                                                         'CMEO': CMEO,
                                                         'FIN' : FIN,
                                                         'FSGT': FSGT,
                                                         'TRNS1': TRNS1,
                                                         'TRNS2': TRNS2,
                                                         'DRLS': DRLS,
                                                         'ADMC': ADMC,
                                                         'MISLO': MISLO,
                                                     }, 
                                                     context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def assignCOC(request):
    #Allows CC to appoint company staff
    
    #Saves billet assignment    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagCC = False
    for p in lBillets :
        if p.billet == "CC" and p.current :
            flagCC = True

    if not flagCC :
        return HttpResponseRedirect('/')
    #End of second check
    
    lBillet = Billet.objects.filter(mid__company = cCompany)
    
    cPC1 = None
    for p in lBillet:
        if p.billet == "PC" and p.current and p.mid.platoon == "1" :
            cPC1 = p
            
    cPC2 = None
    for p in lBillet:
        if p.billet == "PC" and p.current and p.mid.platoon == "2" :
            cPC2 = p
            
    cPC3 = None
    for p in lBillet:
        if p.billet == "PC" and p.current and p.mid.platoon == "3" :
            cPC3 = p
            
    cPC4 = None
    for p in lBillet:
        if p.billet == "PC" and p.current and p.mid.platoon == "4" :
            cPC4 = p
    
    cPLTS1 = None
    for p in lBillet:
        if p.billet == "PLTS" and p.current and p.mid.platoon == "1" :
            cPLTS1 = p
    
    cPLTS2 = None
    for p in lBillet:
        if p.billet == "PLTS" and p.current and p.mid.platoon == "2" :
            cPLTS2 = p
    
    cPLTS3 = None
    for p in lBillet:
        if p.billet == "PLTS" and p.current and p.mid.platoon == "3" :
            cPLTS3 = p
    
    cPLTS4 = None
    for p in lBillet:
        if p.billet == "PLTS" and p.current and p.mid.platoon == "4" :
            cPLTS4 = p 
    
    cSL11 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "1" and p.mid.squad == "1" :
            cSL11 = p
    
    cSL12 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "1" and p.mid.squad == "2" :
            cSL12 = p
    
    cSL13 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "1" and p.mid.squad == "3" :
            cSL13 = p
    
    cSL21 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "2" and p.mid.squad == "1" :
            cSL21 = p
    
    cSL22 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "2" and p.mid.squad == "2" :
            cSL22 = p
    
    cSL23 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "2" and p.mid.squad == "3" :
            cSL23 = p
    
    cSL31 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "3" and p.mid.squad == "1" :
            cSL31 = p
    
    cSL32 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "3" and p.mid.squad == "2" :
            cSL32 = p
    
    cSL33 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "3" and p.mid.squad == "3" :
            cSL33 = p
    
    cSL41 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "4" and p.mid.squad == "1" :
            cSL41 = p
    
    cSL42 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "4" and p.mid.squad == "2" :
            cSL42 = p
    
    cSL43 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "4" and p.mid.squad == "3" :
            cSL43 = p

    lMidsOne = Mid.objects.filter(company=cCompany).filter(rank = "1").order_by('alpha')
    lMidsTwo = Mid.objects.filter(company=cCompany).filter(rank = "2").order_by('alpha')
                                                                                                        
    return render_to_response('mid/assignCOC.html', {'lMidsOne' : lMidsOne, 
                                                     'lMidsTwo' : lMidsTwo,
                                                     'PC1' : cPC1,
                                                     'PC2' : cPC2,
                                                     'PC3' : cPC3,
                                                     'PC4' : cPC4,
                                                     'PLTS1': cPLTS1,
                                                     'PLTS2': cPLTS2,
                                                     'PLTS3': cPLTS3,
                                                     'PLTS4': cPLTS4,
                                                     'SL11' : cSL11,
                                                     'SL12' : cSL12,
                                                     'SL13' : cSL13,
                                                     'SL21' : cSL21,
                                                     'SL22' : cSL22,
                                                     'SL23' : cSL23,
                                                     'SL31' : cSL31,
                                                     'SL32' : cSL32,
                                                     'SL33' : cSL33,
                                                     'SL41': cSL41,
                                                     'SL42': cSL42,
                                                     'SL43': cSL43,
                                                     }, 
                                                     context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveAssignBillets(request):
    #Saves billet assignment    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagCC = False
    for p in lBillets :
        if p.billet == "CC" and p.current :
            flagCC = True

    if not flagCC :
        return HttpResponseRedirect('/')
    #End of second check
    
    cDate = date.today()
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    lBillet = Billet.objects.filter(mid__company = cCompany)
    
    L = ['XO', 'HA', 'OPS', 'ADJ', 'PMO', 'AC', 'SAF', 'APT', 'ADEO', 'ATFP', 'TRN', 'FLT', 'ADM', 'PRO',
         'WRD', 'DRL', 'SAVI', 'CMEO', 'FIN', 'FSGT', 'DRLS', 'ADMC', 'MISLO', 'TRNS1', 'TRNS2']

    for x in L:
        alpha = request.POST[x]
        if alpha != "000000" :    
            for p in lBillet:
                if p.billet == x and p.current :
                    p.endDate = cDate
                    p.current = False
                    p.save()
            cMid = Mid.objects.get(alpha = alpha)
            
            if x == "XO" or x == "OPS" or x == "FSGT":
                cMid.squad = "S"
                cMid.platoon = "S"
                cMid.save()
            
            cBillet = Billet(mid = cMid,
                             billet = x,
                             startDate = cDate,
                             current = True
                            )
            cBillet.save()
                                                                                                        
    return HttpResponseRedirect(reverse('mid:assignBillets')) 

@login_required(redirect_field_name='/')
def saveAssignCOC(request):
    #Saves billet assignment    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagCC = False
    for p in lBillets :
        if p.billet == "CC" and p.current :
            flagCC = True

    if not flagCC :
        return HttpResponseRedirect('/')
    #End of second check
    
    cDate = date.today()
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    lBillet = Billet.objects.filter(mid__company = cCompany)

    L = ['1', '2', '3', '4']
    R = ['1', '2', '3']
    
    for x in L :
        alpha = request.POST['PC'+x]
        if alpha != "000000" :    
            for p in lBillet:
                cMid = p.mid
                if p.billet == 'PC' and p.current and cMid.platoon == x :
                    p.endDate = cDate
                    p.current = False
                    p.save()
            
            cMid = Mid.objects.get(alpha = alpha)
            cMid.platoon = x
            cMid.squad = "S"
            cBillet = Billet(mid = cMid,
                             billet = "PC",
                             startDate = cDate,
                             current = True
                            )
            cBillet.save()
            
        alpha = request.POST['PLTS'+x]
        if alpha != "000000" :    
            for p in lBillet:
                cMid = p.mid
                if p.billet == 'PLTS' and p.current and cMid.platoon == x :
                    p.endDate = cDate
                    p.current = False
                    p.save()
            
            cMid = Mid.objects.get(alpha = alpha)
            cMid.platoon = x
            cMid.squad = "S"
            cMid.save()
            cBillet = Billet(mid = cMid,
                             billet = "PLTS",
                             startDate = cDate,
                             current = True
                            )
            cBillet.save()

        for z in R:
            alpha = request.POST['SL'+x+z]
            if alpha != "000000" :    
                for p in lBillet:
                    if p.billet == 'SL' and p.current and p.mid.platoon == x and p.mid.squad == z :
                        p.endDate = cDate
                        p.current = False
                        p.save()
            
                cMid = Mid.objects.get(alpha = alpha)
                cMid.platoon = x
                cMid.squad = z
                cMid.save()
                cBillet = Billet(mid = cMid,
                                 billet = "SL",
                                 startDate = cDate,
                                 current = True
                                )
                cBillet.save()

                                                                                                        
    return HttpResponseRedirect(reverse('mid:assignCOC'))

@login_required(redirect_field_name='/')    
def pendingApproval(request) :
    #Generates a list of Special Request/ORM chits that need to be approved by this person...
    username = request.user.username
    
    if re.match("CO", username) is not None :
        username = username.split('_')
        cCompany = username[1]
        lSRC = SpecialRequestChit.objects.filter(mid__company = cCompany).filter(approvalStatus = "4")
        lORM = OrmChit.objects.filter(mid__company = cCompany).filter(approvalStatus = "4")
        
        return render_to_response('mid/pendingApproval.html', {'CO' : True, 
                                                               'lSRC' : lSRC,
                                                               'lORM' : lORM, 
                                                               },
                                                               context_instance=RequestContext(request))
        
    elif re.match("SEL", username) is not None :
        username = username.split('_')
        cCompany = username[1]
        lSRC = SpecialRequestChit.objects.filter(mid__company = cCompany).filter(approvalStatus = "5")
        lORM = OrmChit.objects.filter(mid__company = cCompany).filter(approvalStatus = "5")
        
        return render_to_response('mid/pendingApproval.html', {'SEL' : True, 
                                                               'lSRC' : lSRC,
                                                               'lORM' : lORM, 
                                                               },
                                                               context_instance=RequestContext(request))
    
    else :
        alpha = username.split('m')
        alpha = alpha[1]
        cMid = Mid.objects.get(alpha=alpha)
        cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    SL = False
    PC = False
    CC = False
    
    for p in lBillets :
        if p.billet == "SL" and p.current :
            cSquad = cMid.squad
            lSRC = SpecialRequestChit.objects.filter(mid__squad = cSquad).filter(approvalStatus = "1")
            lORM = OrmChit.objects.filter(mid__squad = cSquad).filter(approvalStatus = "1")
            SL = True
        elif p.billet == "PC" and p.current :
            cPlatoon = cMid.platoon
            lSRC = SpecialRequestChit.objects.filter(mid__platoon = cPlatoon).filter(approvalStatus = "2")
            lORM = OrmChit.objects.filter(mid__platoon = cPlatoon).filter(approvalStatus = "2")
            PC = True
        if p.billet == "CC" and p.current :
            cCompany = cMid.company
            lSRC = SpecialRequestChit.objects.filter(mid__company = cCompany).filter(approvalStatus = "3")
            lORM = OrmChit.objects.filter(mid__company = cCompany).filter(approvalStatus = "3")
            CC = True
    
    return render_to_response('mid/pendingApproval.html', { 'cMid' : cMid, 
                                                            'lSRC' : lSRC,
                                                            'lORM' : lORM,
                                                            'SL' : SL,
                                                            'PC' : PC,
                                                            'CC' : CC
                                                           },
                                                           context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')    
def specReqView(request) :
    cChit = SpecialRequestChit.objects.get(id=request.POST['id'])
    username = request.user.username
    
    if re.match("CO", username) is not None :
        return render_to_response('specialrequestchit/specReqView.html', {'CO' : True, 
                                                                          'cChit' : cChit,
                                                                          }, 
                                                                          context_instance=RequestContext(request))
        
    elif re.match("SEL", username) is not None :
        return render_to_response('specialrequestchit/specReqView.html', {'SEL' : True, 
                                                                          'cChit' : cChit,
                                                                          }, 
                                                                          context_instance=RequestContext(request))
    
    else :
        alpha = username.split('m')
        alpha = alpha[1]
        cMid = Mid.objects.get(alpha=alpha)

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    SL = False
    PC = False
    CC = False
    
    for p in lBillets :
        if p.billet == "SL" and p.current :
            SL = True
        elif p.billet == "PC" and p.current :
            PC = True
        if p.billet == "CC" and p.current :
            CC = True

    return render_to_response('specialrequestchit/specReqView.html', {'SL' : SL,
                                                                      'PC' : PC,
                                                                      'CC' : CC, 
                                                                      'cChit' : cChit,
                                                                      }, 
                                                                      context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')    
def approveChit(request) :
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    cChit = SpecialRequestChit.objects.get(id=request.POST['id'])
    
    level = request.POST['level']
    action = request.POST['action']
    comment = request.POST['comment']
    
    if level == "1" :
        if action == "1" :
            cChit.squadLeaderApproval = True
            if cChit.approvalLevel == 1 :
                cChit.approvalStatus = 0
            else:
                cChit.approvalStatus = 2
        else:
            cChit.squadLeaderApproval = False
            if cChit.approvalLevel == 1 :
                cChit.approvalStatus = -1
            else:
                cChit.approvalStatus = 2
        
        cChit.slComment = comment
        
    if level == "2" :
        if action == "1" :
            cChit.squadLeaderApproval = True
            if cChit.approvalLevel == 2 :
                cChit.approvalStatus = 0
            else:
                cChit.approvalStatus = 3
        else:
            cChit.squadLeaderApproval = False
            if cChit.approvalLevel == 2 :
                cChit.approvalStatus = -1
            else:
                cChit.approvalStatus = 3
        
        cChit.plComment = comment
    
    if level == "3" :
        if action == "1" :
            cChit.squadLeaderApproval = True
            if cChit.approvalLevel == 3 :
                cChit.approvalStatus = 0
            else:
                cChit.approvalStatus = 4
        else:
            cChit.squadLeaderApproval = False
            if cChit.approvalLevel == 3 :
                cChit.approvalStatus = -1
            else:
                cChit.approvalStatus = 4
        
        cChit.ccComment = comment
    
    if level == "4" :
        if action == "1" :
            cChit.squadLeaderApproval = True
            if cChit.approvalLevel == 4 :
                cChit.approvalStatus = 0
            else:
                cChit.approvalStatus = 5
        else:
            cChit.squadLeaderApproval = False
            if cChit.approvalLevel == 4 :
                cChit.approvalStatus = -1
            else:
                cChit.approvalStatus = 5
        
        cChit.selComment = comment
    
    if level == "5" :
        if action == "1" :
            cChit.squadLeaderApproval = True
            if cChit.approvalLevel == 5 :
                cChit.approvalStatus = 0
            else:
                cChit.approvalStatus = 6
        else:
            cChit.squadLeaderApproval = False
            if cChit.approvalLevel == 5 :
                cChit.approvalStatus = -1
            else:
                cChit.approvalStatus = 6
        
        cChit.coComment = comment    
        
    cChit.save()
    
    return HttpResponseRedirect(reverse('mid:pendingApproval')) 
    
@login_required(redirect_field_name='/')    
def PRTSat(request) :
    #Aggregate list of people's physical status
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagPMO = False
    for p in lBillets :
        if p.billet == "PMO" and p.current :
            flagPMO = True

    if not flagPMO :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company = cCompany).order_by('alpha')
    
    return render_to_response('mid/PRTSat.html', { 'cCompany' : cCompany, 
                                                   'lMids' : lMids },
                                                   context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def savePRT(request):
    #Save updated physical status

    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagPMO = False
    for p in lBillets :
        if p.billet == "PMO" and p.current :
            flagPMO = True

    if not flagPMO :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
       return HttpResponseRedirect("/")
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')

    for p in lMids :
        if request.POST[p.alpha+'P'] == "True" :
            p.PRTSat = True
        else :
            p.PRTSat = False
            
        p.save()
 
    return HttpResponseRedirect(reverse('mid:PRTSat')) 

@login_required(redirect_field_name='/')
def enterDiscipline(request):
    #Enter Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')
    
    return render_to_response('mid/enterDiscipline.html', { 'cCompany' : cCompany, 
                                                            'lMids' : lMids },
                                                            context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def saveDiscipline(request):
    #Save entered Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['alpha']
    honor = request.POST['honor']
    dateOffense = request.POST['dateOffense']
    startDate = request.POST['startDate']
    daysAwarded = request.POST['daysAwarded']
    toursAwarded = request.POST['toursAwarded']
    adminNotes = request.POST['adminNotes']
    
    if toursAwarded < daysAwarded :
            toursAwarded = daysAwarded

    cDisc = Discipline(mid = Mid.objects.get(alpha = alpha),
                       conductHonor = honor,
                       dateOffence = dateOffense,
                       startDate = startDate,
                       daysAwarded = daysAwarded,
                       daysRemaining = daysAwarded,
                       toursAwarded = toursAwarded,
                       toursRemaining = toursAwarded,
                       adminNotes = adminNotes,
                       checked = date.today(),
                       )
    
    cDisc.save()
    
    return HttpResponseRedirect(reverse('mid:enterDiscipline')) 

@login_required(redirect_field_name='/')
def enterProbation(request):
    #Enter Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')
    
    return render_to_response('mid/enterProbation.html', { 'cCompany' : cCompany, 
                                                            'lMids' : lMids },
                                                            context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def saveProbation(request):
    #Save entered Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['alpha']
    startDate = request.POST['startDate']
    daysAwarded = request.POST['daysAwarded']
    adminNotes = request.POST['adminNotes']

    cDisc = Probation(mid = Mid.objects.get(alpha = alpha),
                       startDate = startDate,
                       daysAwarded = daysAwarded,
                       description = adminNotes,
                       )
    
    cDisc.save()
    
    return HttpResponseRedirect(reverse('mid:enterProbation')) 

@login_required(redirect_field_name='/')
def assessDiscipline(request):
    #Save entered Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    lDisc = Discipline.objects.filter(mid__company = cCompany).filter(toursRemaining__gt= 0)
    
    return render_to_response('mid/assessDiscipline.html', { 'cCompany' : cCompany, 
                                                             'lDisc' : lDisc,
                                                             },
                                                            context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def updateDiscipline(request):
    #Save entered Restriction/Tours
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company

    #List of current mid's billets
    lBillets = Billet.objects.filter(mid=cMid)
    
    flagApt = False
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    lDisc = Discipline.objects.filter(mid__company = cCompany).filter(toursRemaining__gt= 0)
                                      
    for p in lDisc :
        if p.daysRemaining > 0 and request.POST[str(p.id)] == "true":
            p.daysRemaining = p.daysRemaining -1
        
        if p.toursRemaining > 0 and request.POST[str(p.id)] == "true":
            p.toursRemaining = p.toursRemaining -1
        
        if p.toursRemaining < p.daysRemaining :
            p.toursRemaining = p.daysRemaining
        
        p.save()
    
    return HttpResponseRedirect(reverse('mid:assessDiscipline')) 

#Following functions deal with CO's functionality
@login_required(redirect_field_name='/')
def appointCC(request):
    #Allows CO to appoint CC
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    lBillet = Billet.objects.filter(mid__company = cCompany)
    
    cBillet = None
    for p in lBillet:
        if p.billet == "CC" and p.current:
            cBillet = p
    
    lMids = Mid.objects.filter(company = cCompany).filter(rank = "1")
                                                                                                        
    return render_to_response('mid/appointCC.html', {'cBillet' : cBillet, 
                                                     'lMids' : lMids 
                                                     }, 
                                                     context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveAppointCC(request):
    #Allows CO to appoint CC
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    cDate = date.today()
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['alpha']
    
    cMid = Mid.objects.get(alpha = alpha)
    cMid.squad = "S"
    cMid.platoon = "S"
    cMid.dutySection = "0"
    cMid.save()
    
    lBillet = Billet.objects.filter(mid__company = cCompany)
    
    for p in lBillet:
        if p.billet == "CC" and p.current:
            p.endDate = cDate
            p.current = False
            p.save()
    
    cBillet = Billet(mid = cMid,
                     billet = "CC",
                     startDate = cDate,
                     endDate = request.POST['endDate'],
                     current = True
                     )
    cBillet.save()
                                                                                                        
    return HttpResponseRedirect(reverse('mid:appointCC')) 

@login_required(redirect_field_name='/')
def changeCompany(request):
    #Allows CO to move MIDN to another company
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    lMids = Mid.objects.filter(company = cCompany)
                                                                                                        
    return render_to_response('mid/changeCompany.html', {'lMids' : lMids 
                                                         }, 
                                                         context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveChangeCompany(request):
    #Allows CO to appoint CC
    
    #Second check - make sure the user is CO
    if re.match("CO", request.user.username) is not None :
        name = request.user.username.split('_')
        cCompany = name[1]  
    else:
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['alpha']
    
    cMid = Mid.objects.get(alpha = alpha)
    
    cMid.company = request.POST['company']
    cMid.save()
                                                                                                        
    return HttpResponseRedirect(reverse('mid:changeCompany')) 