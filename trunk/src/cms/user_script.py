from django.core.management import setup_environ
import settings
setup_environ(settings)

from django.contrib.auth.models import User
from mid.models import Mid
from unit.models import UnitLeader

mids = Mid.objects.all()

for mid in mids:
    user = User.objects.create_user('m'+mid.alpha,'m'+mid.alpha+'@usna.edu','1')

leaders = UnitLeader.objects.all()

for leader in leaders:
    email = ""
    if leader.billet == "BO":
        email = 'bat'+leader.unitNumber+'ofcer@usna.edu'
    elif leader.billet == 'CO':
        email = 'co'+leader.unitNumber+'ofcer@usna.edu'
    elif leader.billet == 'SEL':
        email = 'co'+leader.unitNumber+'asst@usna.edu'
    user = User.objects.create_user(leader.billet+"_"+leader.unitNumber,email,'1')