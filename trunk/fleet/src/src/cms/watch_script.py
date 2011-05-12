from django.core.management import setup_environ
import settings
setup_environ(settings)

import sys

from mid.models import Mid
from mid.models import Billet
from companywatch.models import AcYear
from companywatch.models import AcWatch
from companywatch.models import WatchBill
from companywatch.models import Watch
from companywatch.models import LogBook
from companywatch.models import LogEntry

from datetime import date, time, timedelta


year = date.today().strftime("%y")
try:
    acYear = AcYear.objects.create(acYear=year)
    break
except (RuntimeError, TypeError, NameError,ValueError):
        pass
    
acYear = AcYear.objects.get(acYear=year)

acYear.fallStart = date(2010,8,24)
acYear.fallGoldWeekStart = 'E'
acYear.fall6Weeks = date(2010,10,5)
acYear.fall12Weeks = date(2010,11,9)
acYear.thanksgivingStart = date(2010,11,25)
acYear.thanksgivingEnd = date(2010,11,25)
acYear.fallXWeekStart = date(2010,12,14)
acYear.fallXWeekEnd = date(2010,12,21)
acYear.christmasStart = date(2010,12,21)
acYear.christmasEnd = date(2011,1,07)
acYear.christmasIntersessionalStart = date(2011,1,7)
acYear.christmasIntersessionalEnd = date(2011,1,10)
acYear.laborDay = date(2010,9,6)
acYear.columbusDay = date(2010,10,11)
acYear.veteransDay = date(2010,11,11)
acYear.fallEnd = date(2010,12,10)
acYear.startSpring = date(2011,1,11)
acYear.spring6Weeks = date(2011,2,23)
acYear.spring12Weeks = date(2011,4,12)
acYear.springXWeekStart = date(2011,5,5)
acYear.springXWeekEnd = date(2011,5,12)
acYear.springBreakStart = date(2011,3,12)
acYear.springBreakEnd =  date(2011,3,20)
acYear.mlkDay = date(2011,1,17)
acYear.washingtonBirthday =  date(2011,2,21)
acYear.springEnd =  date(2011,5,3)
acYear.springIntersessionalStart =  date(2011,5,4)
acYear.springIntersessionalEnd =  date(2011,5,12)
acYear.summerStart =  date(2011,5,27)
    
acYear.save()

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

