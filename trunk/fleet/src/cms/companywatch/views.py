#companywatch veiws.py
# Author: Michael Harrison  edited on 10May2011

from mid.models import Mid
from mid.models import Billet
from companywatch.models import AcYear
from companywatch.models import AcWatch
from companywatch.models import WatchBill
from companywatch.models import Watch
from companywatch.models import LogBook
from companywatch.models import LogEntry
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date, time, timedelta


@login_required(redirect_field_name='/')
def AcYearView(request):
    #check to make sure the reqester is the Company Adj.
    #get requesting username and alpha
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    
    #get the MIDN object and set the company variable
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
  
    #get list of MIDN current billets
    cBillets = Billet.objects.filter(mid=cMid)
  
    isAdj = False
    #go through list of MIDN billets and check for ADJ and if it is current
    for i in cBillets:
        if i.billet == 'ADJ' and i.current:
            isAdj = True
    # if either of these statements are false then redirect back to /
    if not isAdj:
        return HttpResponseRedirect('/')
    
    year = date.today().strftime("%y")
    acYear = AcYear.objects.get(acYear=year)
    return render_to_response('companywatch/AcYearView.html', { 'acYear': acYear },context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def AcYearEdit(request):
    #check to make sure the reqester is the Company Adj.
    #get requesting username and alpha
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    
    #get the MIDN object and set the company variable
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
  
    #get list of MIDN current billets
    cBillets = Billet.objects.filter(mid=cMid)
  
    isAdj = False
    #go through list of MIDN billets and check for ADJ and if it is current
    for i in cBillets:
        if i.billet == 'ADJ' and i.current:
            isAdj = True
    # if either of these statements are false then redirect back to /
    if not isAdj:
        return HttpResponseRedirect('/')
    
    year = date.today().strftime("%y")
    acYear = AcYear.objects.get(acYear=year)
    
    return render_to_response('companywatch/AcYearEdit.html',{'acYear':acYear},context_instance=RequestContext(request))

@login_required(redirect_field_name='/')
def AcYearSubmit(request):
    #check to make sure the reqester is the Company Adj.
    #get requesting username and alpha
    alpha = request.user.username.split('m')
    alpha = alpha[1]
    
    #get the MIDN object and set the company variable
    cMid = Mid.objects.get(alpha=alpha)
    cCompany = cMid.company
  
    #get list of MIDN current billets
    cBillets = Billet.objects.filter(mid=cMid)
  
    isAdj = False
    #go through list of MIDN billets and check for ADJ and if it is current
    for i in cBillets:
        if i.billet == 'ADJ' and i.current:
            isAdj = True
    # if either of these statements are false then redirect back to /
    if not isAdj:
        return HttpResponseRedirect('/')

    year = date.today().strftime("%y")
    acYear = AcYear.objects.get(acYear=year)
    
    acYear.fallStart = request.POST['fallStart']
    acYear.fallGoldWeekStart = request.POST['fallGoldWeekStart']
    acYear.fall6Weeks = request.POST['fall6Weeks']
    acYear.fall12Weeks = request.POST['fall12Weeks']
    acYear.thanksgivingStart = request.POST['thanksgivingStart']
    acYear.thanksgivingEnd = request.POST['thanksgivingEnd']
    acYear.fallXWeekStart = request.POST['fallXWeekStart']
    acYear.fallXWeekEnd = request.POST['fallXWeekEnd']
    acYear.christmasStart = request.POST['christmasStart']
    acYear.christmasEnd = request.POST['christmasEnd']
    acYear.christmasIntersessionalStart = request.POST['christmasIntersessionalStart']
    acYear.christmasIntersessionalEnd = request.POST['christmasIntersessionalEnd']
    acYear.laborDay = request.POST['laborDay']
    acYear.columbusDay = request.POST['columbusDay']
    acYear.veteransDay = request.POST['veteransDay']
    acYear.fallEnd = request.POST['fallEnd']
    acYear.startSpring = request.POST['startSpring']
    acYear.spring6Weeks = request.POST['spring6Weeks']
    acYear.spring12Weeks = request.POST['spring12Weeks']
    acYear.springXWeekStart = request.POST['springXWeekStart']
    acYear.springXWeekEnd = request.POST['springXWeekEnd']
    acYear.springBreakStart = request.POST['springBreakStart']
    acYear.springBreakEnd =  request.POST['springBreakEnd']
    acYear.mlkDay =  request.POST['mlkDay']
    acYear.washingtonBirthday =  request.POST['washingtonBirthday']
    acYear.springEnd =  request.POST['springEnd']
    acYear.springIntersessionalStart =  request.POST['springIntersessionalStart']
    acYear.springIntersessionalEnd =  request.POST['springIntersessionalEnd']
    acYear.summerStart =  request.POST['summerStart']
    
    acYear.save()        
    
    return HttpResponseRedirect(reverse('companywatch:AcYearView'))

def initWatchBills(request):
    #create all of the watchbills for a the semester
    acYear = AcYear.objects.get(acYear=11)
    numberOfDays = acYear.summerStart - acYear.fallStart
    count = 0
    while (count < numberOfDays.days):
        WatchBill.objects.create(date=acYear.fallStart + timedelta(days=count),type='W',dutySection=0)
        count = count + 1
    #Set the types of watch for all Leave dates
    #for Thanksgiving set type of Watchbill to Leave
    WatchBill.objects.filter(date__range=(acYear.thanksgivingStart,acYear.thanksgivingEnd)).update(type='L')
    #For Christmas Leave
    WatchBill.objects.filter(date__range=(acYear.christmasStart,acYear.christmasEnd)).update(type='L')
    WatchBill.objects.filter(date__range=(acYear.christmasIntersessionalStart,acYear.christmasIntersessionalEnd)).update(type='L')
    #For Spring Break
    WatchBill.objects.filter(date__range=(acYear.springBreakStart,acYear.springBreakEnd)).update(type='L')
    WatchBill.objects.filter(date__range=(acYear.springIntersessionalStart,acYear.springIntersessionalEnd)).update(type='L')
    
    #set Holidays as type H
    holidays = [acYear.laborDay,acYear.columbusDay,acYear.veteransDay,acYear.mlkDay,acYear.washingtonBirthday]
    for h in holidays:
        WatchBill.objects.get(date=h).update(type='H')
    
    bills = WatchBill.objects.filter(date__range=(acYear.fallStart,acYear.springEnd))
    for bill in bills:
        if bill.date.weekday() == 5:
            if bill.type == 'W':
                bill.type = 'H'
                bill.save()
        elif bill.date.weekday() == 6:
            if bill.type == 'W':
                bill.type = 'H'
                bill.save()
    noMid = Mid.objects.get(alpha=100000)
    workBillTimes = [time(6,30),time(7,00),time(7,50),time(8,50),time(9,50),time(10,50),time(11,50),time(12,20),time(12,50),time(13,25),time(14,25),time(15,30),time(16,00),time(17,00),time(18,00),time(19,00),time(20,00),time(21,00),time(22,00),time(23,00),time(00,00)]

    #Go through each Watch bill for the year and create all of the watches for each bill    
    for bill in bills:
        if bill.type=='W': # For each work day use the times in the workBillTimes to generate the start and end times for the watches
            count = 0
            while count < 20:
                Watch.objects.create(watchBill_id=bill,mid_id=noMid.alpha,startTime=workBillTimes[count],endTime=workBillTimes[count+1],post='Company Area')
                count = count +1
        elif bill.type=='H': # For each holiday all watches start at the top of the hour on the hour
            count = 0
            while count < 23: # from 0 to 23 is 23 watches
                Watch.objects.create(watchBill_id=bill.id,mid_id=noMid.alpha,startTime=time(count,0),endTime=time(count+1,0))
                count = count + 1
            # Last watch of the day is made seprately because time() will not accept a '24' as an hour
            Watch.objects.create(watchBill_id=bill.id,mid_id=noMid.alpha,startTime=time(count,0),endTime=time(0,0))


def WatchBill(request):
    
def WatchBillView(request):

def WatchBillSave(request):
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    