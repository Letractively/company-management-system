from django.http import HttpResponse
from django.http import Http404
from Bravo_Inspection.models import Bravo_Inspection


def index(request):
    return HttpResponse();

def enter(request, bInspection_id):
    return HttpResponse("You're entering inspection  %s." % bInspection_id);

def review(request, bInspection_id):
    p = get_object_or_404(Bravo_Inspection, pk=bInspection_id)
    return HttpResponse(p)
