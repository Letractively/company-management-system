#form1 views.py
# Author: Dimitri Hatley
# Editor: Michael Laws


# note to dimitri:  i wrote this to try to figure out some url nonsense.
#  none of this is well thought out or close to permanent.  feel free to delete all of it and start over.

from mid.models import Mid
from form1.models import Form1
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def createNewForm1(request):
    
    rForm1 = "reasons?"
    
    return render_to_response('form1/create.html', { 'reasons' : rForm1})
 
 
def reviewForm1(request):
    return render_to_response('form1/reviewForm1.html')