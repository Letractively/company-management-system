#companywatch veiws.py
# Author: Michael Harrison

from mid.models import Mid
from companywatch import AcYear
from companywatch import AcWatch
from companywatch import WatchBill
from companywatch import Watch
from companywatch import LogBook
from companywatch import LogEntry

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date


@login_required(redirect_field_name='/')
