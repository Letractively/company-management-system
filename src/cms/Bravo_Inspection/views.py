# Create your views here.

def enter(request, poll_id):
    return HttpResponse("You're entering inspection  %s." % poll_id)

def review(request, poll_id):
    return HttpResponse("You're looking at the results of inspection %s." % poll_id)
