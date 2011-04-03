#Zero8 views.py
# Author: Dimitri Hatley
# Editor: Michael Laws

from mid.models import Mid
from mid.models import Billet
from mid.models import Room
from units.models import Units
from units.models import UnitLeaders
from zero8.models import Zero8
from zero8.models import SignificantEvents
from accountability.models import Event
from accountability.models import Attendance
from weekends.models import Weekend
from movementorder.models import MovementOrder
from movementorder.models import MOParticipant
from discipline.models import Separation
from discipline.models import Restriction
from discipline.models import Tours
from discipline.models import Probation
from medchits.models import Chit
from zero8.models import Candidates
from zero8.models import Inspections
from uniforminspection.models import UniformInspection
from bravoinspection.models import BravoInspection

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
from datetime import time
from datetime import datetime
from datetime import timedelta

import re

@login_required(redirect_field_name='/')
def viewReport(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    if request.method != "POST" :
        if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
            reportDate = date.today() - timedelta(days = 1)
        else :
            reportDate = date.today()
    else :
        reportDate = request.POST['date']
    
    cReport = Zero8.objects.get(reportDate = reportDate)
    
    #Sig events
    lSigEventsA = SignificantEvents.objects.filter(zero8 = cReport).filter(section = "A")
    cSigEventsA = lSigEventsA.count()
    lSigEventsB = SignificantEvents.objects.filter(zero8 = cReport).filter(section = "B")
    cSigEventsB = lSigEventsB.count()
    lSigEventsC = SignificantEvents.objects.filter(zero8 = cReport).filter(section = "C")
    cSigEventsC = lSigEventsC.count()
    
    cDT = datetime.combine(cReport.reportDate, time(23, 55, 00))
    
    cEvent = Event.objects.filter(company = cCompany).filter(type = "TAP").filter(dateTime = cDT)
    cEvent = cEvent[0]
    
    lMidsOnMO = Mid.objects.filter(company = cCompany).filter(moparticipant__MO__returnDate = "3000-01-01")
    
    for p in lMidsOnMO:
        tAttendance = Attendance.objects.get(mid = p, event = cEvent)
        tAttendance.status = "M"
        tAttendance.save()
    
    #TAPS
    cTAPS1P = Attendance.objects.filter(event = cEvent).filter(status = "P").filter(mid__rank = 1).count()
    cTAPS2P = Attendance.objects.filter(event = cEvent).filter(status = "P").filter(mid__rank = 2).count()
    cTAPS3P = Attendance.objects.filter(event = cEvent).filter(status = "P").filter(mid__rank = 3).count()
    cTAPS4P = Attendance.objects.filter(event = cEvent).filter(status = "P").filter(mid__rank = 4).count()
    
    cTAPS1A = Attendance.objects.filter(event = cEvent).filter(status = "A").filter(mid__rank = 1).count()
    cTAPS2A = Attendance.objects.filter(event = cEvent).filter(status = "A").filter(mid__rank = 2).count()
    cTAPS3A = Attendance.objects.filter(event = cEvent).filter(status = "A").filter(mid__rank = 3).count()
    cTAPS4A = Attendance.objects.filter(event = cEvent).filter(status = "A").filter(mid__rank = 4).count()
    
    cTAPS1U = Attendance.objects.filter(event = cEvent).filter(status = "U").filter(mid__rank = 1).count()
    cTAPS2U = Attendance.objects.filter(event = cEvent).filter(status = "U").filter(mid__rank = 2).count()
    cTAPS3U = Attendance.objects.filter(event = cEvent).filter(status = "U").filter(mid__rank = 3).count()
    cTAPS4U = Attendance.objects.filter(event = cEvent).filter(status = "U").filter(mid__rank = 4).count()
    
    cTAPS1W = Attendance.objects.filter(event = cEvent).filter(status = "W").filter(mid__rank = 1).count()
    cTAPS2W = Attendance.objects.filter(event = cEvent).filter(status = "W").filter(mid__rank = 2).count()
    cTAPS3W = Attendance.objects.filter(event = cEvent).filter(status = "W").filter(mid__rank = 3).count()
    cTAPS4W = Attendance.objects.filter(event = cEvent).filter(status = "W").filter(mid__rank = 4).count()
    
    cTAPS1M = Attendance.objects.filter(event = cEvent).filter(status = "M").filter(mid__rank = 1).count()
    cTAPS2M = Attendance.objects.filter(event = cEvent).filter(status = "M").filter(mid__rank = 2).count()
    cTAPS3M = Attendance.objects.filter(event = cEvent).filter(status = "M").filter(mid__rank = 3).count()
    cTAPS4M = Attendance.objects.filter(event = cEvent).filter(status = "M").filter(mid__rank = 4).count()
     
    cTotalP = cTAPS1P + cTAPS2P + cTAPS3P + cTAPS4P
    cTotalA = cTAPS1A + cTAPS2A + cTAPS3A + cTAPS4A
    cTotalU = cTAPS1U + cTAPS2U + cTAPS3U + cTAPS4U
    cTotalW = cTAPS1W + cTAPS2W + cTAPS3W + cTAPS4W
    cTotalM = cTAPS1M + cTAPS2M + cTAPS3M + cTAPS4M
    
    #TAPS in detail
    lA = Attendance.objects.filter(event = cEvent).filter(status = "A").order_by('mid')
    lU = Attendance.objects.filter(event = cEvent).filter(status = "U").order_by('mid')
    lW = Attendance.objects.filter(event = cEvent).filter(status = "W").order_by('mid')
    lM = MovementOrder.objects.filter(moparticipant__participant__company = cCompany).filter(returnDate = "3000-01-01").order_by('-departDate').distinct()
    
    cA = lA.count()
    cU = lU.count()
    cW = lW.count()
    cM = lM.count()
    
    #Discipline
    lPS = Separation.objects.filter(zero8 = cReport).filter(pending = True)
    lFS = Separation.objects.filter(zero8 = cReport).filter(pending = False)
    lR = Restriction.objects.filter(mid__company = cCompany).filter(daysRemaining__gt= 0).order_by('mid')
    lT = Tours.objects.filter(mid__company = cCompany).filter(toursRemaining__gt= 0).order_by('mid') 
    lP = Probation.objects.filter(mid__company = cCompany).order_by('mid')
    
    cPS = lPS.count()
    cFS = lFS.count()
    cR = lR.count()
    cT = lT.count()
    cP = lP.count()
    
    #Chits
    lMChit = Chit.objects.filter(mid__company = cCompany).filter(endDate__gt = cReport.reportDate).filter(disposition = "LLD").order_by('mid')
    lSChit = Chit.objects.filter(mid__company = cCompany).filter(endDate__gt = cReport.reportDate).exclude(disposition = "LLD").order_by('mid')
    
    cMChit = lMChit.count()
    cSChit = lSChit.count()
    
    #MIDN 6/C =)
    lCand = Candidates.objects.filter(host__company = cCompany).filter(departDate = "3000-01-01")
    cCand = lCand.count()
    
    #Inspections of all kinds
    lDutySectionMuster = Inspections.objects.filter(zero8 = cReport).filter(type = "W")
    cDutySectionMuster = lDutySectionMuster.count()
    lUniform = UniformInspection.objects.filter(mid__company = cCompany).filter(inspectionDate = cReport.reportDate)
    cUniform = lUniform.count()
    lRoom = BravoInspection.objects.filter(room__company = cCompany).filter(inspectionDate = cReport.reportDate)
    cRoom = lRoom.count()
    lBedCheck = Inspections.objects.filter(zero8 = cReport).filter(type = "B")
    cBedCheck = lBedCheck.count()
    lStudyHour = Inspections.objects.filter(zero8 = cReport).filter(type = "S")
    cStudyHour = lStudyHour.count()
    lRestCheck = Inspections.objects.filter(zero8 = cReport).filter(type = "R")
    cRestCheck = lRestCheck.count()
    lBAC = Inspections.objects.filter(zero8 = cReport).filter(type = "A")
    cBAC = lBAC.count()
    
    return render_to_response('zero8/viewReport.html', {#'cMid':cMid,
                                                        'cReport' : cReport,
                                                        'cDate' : cReport.reportDate,
                                                        'cCompany' : cCompany, 
                                                        'lSigEventsA' : lSigEventsA,
                                                        'cSigEventsA' : cSigEventsA,
                                                        'lSigEventsB' : lSigEventsB,
                                                        'cSigEventsB' : cSigEventsB,
                                                        'lSigEventsC' : lSigEventsC,
                                                        'cSigEventsC' : cSigEventsC,
                                                        'cTAPS1P' : cTAPS1P,
                                                        'cTAPS2P' : cTAPS2P,
                                                        'cTAPS3P' : cTAPS3P,
                                                        'cTAPS4P' : cTAPS4P,
                                                        'cTAPS1A' : cTAPS1A,
                                                        'cTAPS2A' : cTAPS2A,
                                                        'cTAPS3A' : cTAPS3A,
                                                        'cTAPS4A' : cTAPS4A,
                                                        'cTAPS1U' : cTAPS1U,
                                                        'cTAPS2U' : cTAPS2U,
                                                        'cTAPS3U' : cTAPS3U,
                                                        'cTAPS4U' : cTAPS4U,
                                                        'cTAPS1W' : cTAPS1W,
                                                        'cTAPS2W' : cTAPS2W,
                                                        'cTAPS3W' : cTAPS3W,
                                                        'cTAPS4W' : cTAPS4W,
                                                        'cTAPS1M' : cTAPS1M,
                                                        'cTAPS2M' : cTAPS2M,
                                                        'cTAPS3M' : cTAPS3M,
                                                        'cTAPS4M' : cTAPS4M,
                                                        'cTotalP' : cTotalP,
                                                        'cTotalA' : cTotalA,
                                                        'cTotalU' : cTotalU,
                                                        'cTotalW' : cTotalW,
                                                        'cTotalM' : cTotalM,
                                                        'lU' : lU,
                                                        'lA' : lA,
                                                        'lW' : lW,
                                                        'lM' : lM,
                                                        'cU' : cU,
                                                        'cA' : cA,
                                                        'cW' : cW,
                                                        'cM' : cM,
                                                        'lPS' : lPS,
                                                        'lFS' : lFS,
                                                        'lR' : lR,
                                                        'lT' : lT,
                                                        'lP' : lP,
                                                        'cPS' : cPS,
                                                        'cFS' : cFS,
                                                        'cR' : cR,
                                                        'cT' : cT,
                                                        'cP' : cP,
                                                        'lMChit' : lMChit,
                                                        'lSChit' : lSChit,
                                                        'cMChit' : cMChit,
                                                        'cSChit' : cSChit,
                                                        'lCand' : lCand,
                                                        'cCand' : cCand,
                                                        'lDutySectionMuster' : lDutySectionMuster,
                                                        'cDutySectionMuster' : cDutySectionMuster,
                                                        'lUniform' : lUniform,
                                                        'cUniform' : cUniform,
                                                        'lRoom' : lRoom,
                                                        'cRoom' : cRoom,
                                                        'lBedCheck' : lBedCheck,
                                                        'cBedCheck' : cBedCheck,
                                                        'lStudyHour' : lStudyHour,
                                                        'cStudyHour' : cStudyHour,
                                                        'lRestCheck' : lRestCheck, 
                                                        'cRestCheck' : cRestCheck, 
                                                        'lBAC' : lBAC,
                                                        'cBAC' : cBAC,
                                                       }, 
                                                       context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def createSignificantEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    lMids = Mid.objects.filter(company = cCompany)
    
    return render_to_response('zero8/createSignificantEvent.html', {'cMid':cMid,
                                                                    'lMids' : lMids,
                                                                    }, 
                                                                    context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def saveSignificantEvent(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
        
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    cEvent = SignificantEvents(zero8 = cReport,
                               section = request.POST['section'],
                               name = Mid.objects.get(alpha = request.POST['alpha']),
                               description = request.POST['description'],
                               adminNote = request.POST['adminNote']
                               )
    cEvent.save()
    
    return HttpResponseRedirect(reverse('zero8:createSignificantEvent'))

@login_required(redirect_field_name='/')
def candidates(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    lMids = Mid.objects.filter(company = cCompany)
    lCand = Candidates.objects.filter(host__company = cCompany).filter(departDate = "3000-01-01")
    
    return render_to_response('zero8/candidates.html', {'cMid':cMid,
                                                        'lMids' : lMids,
                                                        'lCand' : lCand
                                                        }, 
                                                        context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveCandidate(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cCandidate = Candidates(host = Mid.objects.get(alpha = request.POST['alpha']),
                           name = request.POST['name'],
                           source = request.POST['source'],
                           adminNote = request.POST['adminNote'],
                           arriveDate = cDate,
                           departDate = date(3000, 1, 1)
                           )
    cCandidate.save()
    
    return HttpResponseRedirect(reverse('zero8:candidates'))
    
@login_required(redirect_field_name='/')
def removeCandidate(request):    
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    cCandidate = Candidates.objects.get(id = request.POST['id'])
    cCandidate.departDate = date.today()
    cCandidate.save()
    
    return HttpResponseRedirect(reverse('zero8:candidates'))
    
@login_required(redirect_field_name='/')
def dutySectionMuster(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    cDuty = cMid.dutySection
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    lMids = Mid.objects.filter(company = cCompany).filter(dutySection = cDuty)
    lMusters = Inspections.objects.filter(zero8 = cReport).filter(type = "W")
    
    return render_to_response('zero8/dutySectionMuster.html', {'cMid':cMid,
                                                               'lMids' : lMids,
                                                               'lMusters' : lMusters
                                                               }, 
                                                               context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveDutySectionMuster(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    cInspection = Inspections(zero8 = cReport,
                              type = "W",
                              inspector = cMid,
                              inspectee = Mid.objects.get(alpha = request.POST['alpha']),
                              time = time(8,0,0),
                              scoreEarned = 0,
                              scorePossible = 0,
                              SAT = request.POST['SAT'],
                              comment = request.POST['comment']
                              )
    cInspection.save()
    
    return HttpResponseRedirect(reverse('zero8:dutySectionMuster'))

@login_required(redirect_field_name='/')
def bedCheck(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    lRooms = Room.objects.filter(company = cCompany)
    lMusters = Inspections.objects.filter(zero8 = cReport).filter(type = "B")
    
    return render_to_response('zero8/bedCheck.html', {'cMid':cMid,
                                                       'lRooms' : lRooms,
                                                       'lMusters' : lMusters
                                                        }, 
                                                        context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveBedCheck(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    cInspection = Inspections(zero8 = cReport,
                              type = "B",
                              inspector = cMid,
                              room = Room.objects.get(roomNumber = request.POST['roomNumber']),
                              time = time(8,0,0),
                              scoreEarned = request.POST['people'],
                              scorePossible = 0,
                              SAT = request.POST['SAT'],
                              comment = request.POST['comment']
                              )
    cInspection.save()
    
    return HttpResponseRedirect(reverse('zero8:bedCheck'))

@login_required(redirect_field_name='/')
def studyHour(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    lRooms = Room.objects.filter(company = cCompany)
    lMusters = Inspections.objects.filter(zero8 = cReport).filter(type = "S")
    
    return render_to_response('zero8/studyHour.html', {'cMid':cMid,
                                                       'lRooms' : lRooms,
                                                       'lMusters' : lMusters
                                                        }, 
                                                        context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def saveStudyHour(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    cInspection = Inspections(zero8 = cReport,
                              type = "S",
                              inspector = cMid,
                              room = Room.objects.get(roomNumber = request.POST['roomNumber']),
                              time = time(8,0,0),
                              scoreEarned = 0,
                              scorePossible = 0,
                              SAT = request.POST['SAT'],
                              comment = request.POST['comment']
                              )
    cInspection.save()
    
    return HttpResponseRedirect(reverse('zero8:studyHour'))

@login_required(redirect_field_name='/')
def BAC(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    lMids = Mid.objects.filter(company = cCompany)
    lMusters = Inspections.objects.filter(zero8 = cReport).filter(type = "A")
    
    return render_to_response('zero8/BAC.html', {'cMid':cMid,
                                                 'lMids' : lMids,
                                                 'lMusters' : lMusters
                                                 }, 
                                                 context_instance=RequestContext(request))
    
@login_required(redirect_field_name='/')
def sBAC(request):
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    cMid = Mid.objects.get(alpha=alpha)
    
    #Safety feature, makes sure we POST data to this view
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    
    if time(datetime.now().hour, datetime.now().minute, 0) < time(8, 0, 0):
        cDate = date.today() - timedelta(days = 1)
    else :
        cDate = date.today()
    
    cReport = Zero8.objects.get(reportDate = cDate)
    
    cInspection = Inspections(zero8 = cReport,
                              type = "A",
                              inspector = cMid,
                              inspectee = Mid.objects.get(alpha = request.POST['alpha']),
                              time = time(8,0,0),
                              scoreEarned = 0,
                              scorePossible = 0,
                              SAT = request.POST['SAT'],
                              comment = request.POST['comment']
                              )
    cInspection.save()
    
    return HttpResponseRedirect(reverse('zero8:BAC'))