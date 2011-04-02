#ORM veiws.py
# Author: Dimitri Hatley

from mid.models import Mid
from mid.models import Billet

from orm.models import OrmChit
from orm.models import LeisureActivites
from orm.models import MethodsOfTravel

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django.template import RequestContext
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from datetime import date
from datetime import timedelta

