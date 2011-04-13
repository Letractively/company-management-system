from django.core.management import setup_environ
import settings
setup_environ(settings)

from django.contrib.auth.models import User
from mid.models import Mid

mids = Mid.objects.all()

for mid in mids:
    user = User.objects.create_user(mid.fName + ' '+ mid.LName,'m'+mid.alpha+'@usna.edu','1')
