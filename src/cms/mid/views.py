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
    if user.is_authenticated:
        return HttpResponseRedirect('switchboard')
    else:
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
    
    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha = alpha)
                        
    lBillets = Billet.objects.filter(mid = cMid)
    
    
    
    flagFirstie = False
    if cMid.rank == "1" :
        flagFirstie = True
    
    #Here we assign permissions based on billets.
    flagAdmin = False;
    for p in lBillets :
        if p.billet == "ADM" and p.current :
            flagAdmin = True
        if p.billet == "ADMC" and p.current :
            flagAdmin == True
            
    flagPMO = False;
    for p in lBillets :
        if p.billet == "PMO" and p.current :
            flagPMO = True
    
    flagApt = False;
    for p in lBillets :
        if p.billet == "APT" and p.current :
            flagApt = True
            
    flagAdj = False;
    for p in lBillets :
        if p.billet == "ADJ" and p.current :
            flagAdj = True
            
    flagCC = False;
    for p in lBillets :
        if p.billet == "CC" and p.current :
            flagCC = True
    
    return render_to_response('mid/switchboard.html', { 'mid' : cMid,
                                                        'firstie' : flagFirstie,
                                                        'PMO' : flagPMO,
                                                        'admin' : flagAdmin,
                                                        'Aptitude' : flagApt,
                                                        'CC' : flagCC,
                                                        'ADJ' : flagAdj
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
                                                                   'lRoom' : lRooms
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
    
    cXO = None
    for p in lBillet:
        if p.billet == "XO" and p.current:
            cXO = p
    
    cHA = None
    for p in lBillet:
        if p.billet == "HA" and p.current:
            cHA = p
    
    cOPS = None
    for p in lBillet:
        if p.billet == "OPS" and p.current:
            cOPS = p
    
    cADJ = None
    for p in lBillet:
        if p.billet == "ADJ" and p.current:
            cADJ = p
    
    cPMO = None
    for p in lBillet:
        if p.billet == "PMO" and p.current:
            cPMO = p
    
    cAC = None
    for p in lBillet:
        if p.billet == "AC" and p.current:
            cAC = p
    
    cSAF = None
    for p in lBillet:
        if p.billet == "SAF" and p.current:
            cSAF = p
    
    cAPT = None
    for p in lBillet:
        if p.billet == "APT" and p.current:
            cAPT = p
    
    cADEO = None
    for p in lBillet:
        if p.billet == "ADEO" and p.current:
            cADEO = p
    
    cATFP = None
    for p in lBillet:
        if p.billet == "ATFP" and p.current:
            cATFP = p
    
    cTRN = None
    for p in lBillet:
        if p.billet == "TRN" and p.current:
            cTRN = p
    
    c1LT = None
    for p in lBillet:
        if p.billet == "1LT" and p.current:
            c1LT = p
    
    cADM = None
    for p in lBillet:
        if p.billet == "ADM" and p.current:
            cADM = p
    
    cPRO = None
    for p in lBillet:
        if p.billet == "PRO" and p.current:
            cPRO = p
    
    cWRD = None
    for p in lBillet:
        if p.billet == "WRD" and p.current:
            cWRD = p
    
    cDRL = None
    for p in lBillet:
        if p.billet == "DRL" and p.current:
            cDRL = p
    
    cSAVI = None
    for p in lBillet:
        if p.billet == "SAVI" and p.current:
            cSAVI = p
    
    cCMEO = None
    for p in lBillet:
        if p.billet == "CMEO" and p.current:
            cCMEO = p
    
    cFIN = None
    for p in lBillet:
        if p.billet == "FIN" and p.current:
            cFIN = p
    
    c1SGT = None
    for p in lBillet:
        if p.billet == "1SGT" and p.current:
            c1SGT = p
    
    cTRS1 = None
    for p in lBillet:
        if p.billet == "TRNS" and p.current:
            cTRS1 = p
    
    cTRS2 = None
    for p in lBillet:
        if p.billet == "TRNS" and p.current and p.evaluation == "2" :
            cTRS2 = p
    
    cDRLS = None
    for p in lBillet:
        if p.billet == "DRLS" and p.current:
            cDRLS = p
    
    cADMC = None
    for p in lBillet:
        if p.billet == "ADMC" and p.current:
            cADMC = p
    
    cMISLO = None
    for p in lBillet:
        if p.billet == "MISLO" and p.current:
            cMISLO = p

    lMidsOne = Mid.objects.filter(company=cCompany).filter(rank = "1").order_by('alpha')
    lMidsTwo = Mid.objects.filter(company=cCompany).filter(rank = "2").order_by('alpha')
                                                                                                        
    return render_to_response('mid/assignBillets.html', {'lMidsOne' : lMidsOne, 
                                                         'lMidsTwo' : lMidsTwo,
                                                         'XO'  : cXO,
                                                         'HA'  : cHA,
                                                         'OPS' : cOPS,
                                                         'ADJ' : cADJ,
                                                         'PMO' : cPMO,
                                                         'AC'  : cAC,
                                                         'SAF' : cSAF,
                                                         'APT' : cAPT,
                                                         'ADEO': cADEO,
                                                         'ATFP': cATFP,
                                                         'TRN' : cTRN,
                                                         '1LT' : c1LT,
                                                         'ADM' : cADM,
                                                         'PRO' : cPRO,
                                                         'WRD' : cWRD,
                                                         'DRL' : cDRL,
                                                         'SAVI': cSAVI,
                                                         'CMEO': cCMEO,
                                                         'FIN' : cFIN,
                                                         '1SGT': c1SGT,
                                                         'TRS1': cTRS1,
                                                         'TRS2': cTRS1,
                                                         'DRLS': cDRLS,
                                                         'ADMC': cADMC,
                                                         'MISLO': cMISLO,
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
    
    cPLS1 = None
    for p in lBillet:
        if p.billet == "PLTS" and p.current and p.mid.platoon == "1" :
            cPLS1 = p
    
    cPLS2 = None
    for p in lBillet:
        if p.billet == "PLTS" and p.current and p.mid.platoon == "2" :
            cPLS2 = p
    
    cPLS3 = None
    for p in lBillet:
        if p.billet == "PLTS" and p.current and p.mid.platoon == "3" :
            cPLS3 = p
    
    cPLS4 = None
    for p in lBillet:
        if p.billet == "PLTS" and p.current and p.mid.platoon == "4" :
            cPLS4 = p 
    
    cSL1 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "1" and p.mid.squad == "1" :
            cSL1 = p
    
    cSL2 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "1" and p.mid.squad == "2" :
            cSL2 = p
    
    cSL3 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "1" and p.mid.squad == "3" :
            cSL3 = p
    
    cSL4 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "2" and p.mid.squad == "1" :
            cSL4 = p
    
    cSL5 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "2" and p.mid.squad == "2" :
            cSL5 = p
    
    cSL6 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "2" and p.mid.squad == "3" :
            cSL6 = p
    
    cSL7 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "3" and p.mid.squad == "1" :
            cSL7 = p
    
    cSL8 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "3" and p.mid.squad == "2" :
            cSL8 = p
    
    cSL9 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "3" and p.mid.squad == "3" :
            cSL9 = p
    
    cSL10 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "4" and p.mid.squad == "1" :
            cSL10 = p
    
    cSL11 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "4" and p.mid.squad == "2" :
            cSL11 = p
    
    cSL12 = None
    for p in lBillet:
        if p.billet == "SL" and p.current and p.mid.platoon == "4" and p.mid.squad == "3" :
            cSL12 = p

    lMidsOne = Mid.objects.filter(company=cCompany).filter(rank = "1").order_by('alpha')
    lMidsTwo = Mid.objects.filter(company=cCompany).filter(rank = "2").order_by('alpha')
                                                                                                        
    return render_to_response('mid/assignCOC.html', {'lMidsOne' : lMidsOne, 
                                                     'lMidsTwo' : lMidsTwo,
                                                     'PC1' : cPC1,
                                                     'PC2' : cPC2,
                                                     'PC3' : cPC3,
                                                     'PC4' : cPC4,
                                                     'PLS1': cPLS1,
                                                     'PLS2': cPLS2,
                                                     'PLS3': cPLS3,
                                                     'PLS4': cPLS4,
                                                     'SL1' : cSL1,
                                                     'SL2' : cSL2,
                                                     'SL3' : cSL3,
                                                     'SL4' : cSL4,
                                                     'SL5' : cSL5,
                                                     'SL6' : cSL6,
                                                     'SL7' : cSL7,
                                                     'SL8' : cSL8,
                                                     'SL9' : cSL9,
                                                     'SL10': cSL10,
                                                     'SL11': cSL11,
                                                     'SL12': cSL12,
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
    
    L = ['XO', 'HA', 'OPS', 'ADJ', 'PMO', 'AC', 'SAF', 'APT', 'ADEO', 'ATFP', 'TRN', '1LT', 'ADM', 'PRO',
         'WRD', 'DRL', 'SAVI', 'CMEO', 'FIN', '1SGT', 'DRLS', 'ADMC', 'MISLO']

    for x in L:
        alpha = request.POST[x]
        if alpha != "000000" :    
            for p in lBillet:
                if p.billet == x and p.current :
                    p.endDate = cDate
                    p.current = False
                    p.save()
            cMid = Mid.objects.get(alpha = alpha)
            cBillet = Billet(mid = cMid,
                             billet = x,
                             startDate = cDate,
                             current = True
                            )
            cBillet.save()
                                                                                                        
    return HttpResponseRedirect(reverse('mid:assignBillets')) 

@login_required(redirect_field_name='/')
def saveAssignCOC(request):
    
    return HttpResponseRedirect(reverse('mid:assignCOC')) 

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