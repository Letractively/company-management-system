#ACHTUNG: Line 258

#mid views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet
from mid.models import Room
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

import re

def loginPage(request):
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

                return render_to_response('mid/co.html', { 'cCompany' : cCompany },
                                            context_instance=RequestContext(request))
            
            if re.match("SEL", username) is not None :
                username = username.split('_')
                cCompany = username[1]
                
                return render_to_response('mid/sel.html', { 'cCompany' : cCompany },
                                            context_instance=RequestContext(request))
            
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
            
    flagPMO = False;
    for p in lBillets :
        if p.billet == "PMO" and p.current :
            flagPMO = True
    
    flagApt = False;
    for p in lBillets :
        if p.billet == "A/C" and p.current :
            flagApt = True
    
    return render_to_response('mid/switchboard.html', { 'mid' : cMid,
                                                        'firstie' : flagFirstie,
                                                        'PMO' : flagPMO,
                                                        'admin' : flagAdmin,
                                                        'Aptitude' : flagApt
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
    
    return HttpResponseRedirect(reverse('switchboard'))

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
                   #acSAT = True,
                   #PRTSat = True,
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
      
    return HttpResponseRedirect('selectUser')

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
    
    return HttpResponseRedirect('selectPassReset')

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
    
    lMids = Mid.objects.filter(company=cCompany).order_by('alpha')
    
    return render_to_response('mid/PRTSat.html', { 'cCompany' : cCompany, 
                                                   'lMids' : lMids },
                              context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def savePRTSat(request):
    #Save updated [hysical status

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
        p.PRTSat = request.POST[p.alpha+'P']
        p.save()

    return HttpResponseRedirect(reverse('PRTSat')) 

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
        if p.billet == "A/C" and p.current :
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
        if p.billet == "A/C" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    alpha = request.POST['alpha']
    honor = request.POST['honor']
    dateOffense = request.POST['dateOffence']
    startDate = request.POST['startDate']
    daysAwarded = request.POST['daysAwarded']
    toursAwarded = request.POST['toursAwarded']
    adminNotes = request.POST['adminNotes']

    cDisc = Discipline(mid = Mid.objects.get(alpha = alpha),
                       conductHonor = honor,
                       dateOffence = dateOffence,
                       startDate = startDate,
                       daysAwarded = daysAwarded,
                       daysRemaining = daysAwarded,
                       toursAwarded = toursAwarded,
                       toursRemaining = toursAwarded,
                       adminNotes = adminNotes,
                       checked = date.today - timedelta(days=1),
                       )
    
    cDisc.save()
    
    return HttpResponseRedirect(reverse('enterDiscipline')) 

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
        if p.billet == "A/C" and p.current :
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
        if p.billet == "A/C" and p.current :
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
    
    return HttpResponseRedirect(reverse('enterProbation')) 

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
        if p.billet == "A/C" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    lDisc = Discipline.objects.filter(daysRemaining > 0 or toursRemaining > 0).filter(Mid__company = cCompany).order_by('-alpha')
    
    return render_to_response('mid/assessDiscipline.html', { 'cCompany' : cCompany, 
                                                            'lMids' : lMids },
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
        if p.billet == "A/C" and p.current :
            flagApt = True

    if not flagApt :
        return HttpResponseRedirect('/')
    #End of second check
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect("/")
    
    lDisc = Discipline.objects.filter(daysRemaining > 0 or toursRemaining > 0
                                      ).filter(Mid__company = cCompany).order_by('-alpha')
                                      
    for p in lDisc :
        if daysRemaining > 0 and request.POST['mod'] == "1":
            daysRemaining = daysRemaining - 1
            
        if toursRemaining > 0 and request.POST['mod'] == "1":
            toursRemaining = toursRemaining - 1
    
    return HttpResponseRedirect(reverse('assessDiscipline')) 