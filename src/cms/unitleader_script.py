from django.core.management import setup_environ
import settings
setup_environ(settings)

from unit.models import Unit
from unit.models import UnitLeader

leaders = UnitLeader.objects.all()

for leader in leaders:
	print u'%s %s %s' % (leader,leader.unitNumber,leader.billet)
	
	if leader.billet == 'BO':
		unit = Unit.objects.get(battalion = leader.unitNumber,company ='0')
		leader.unit_id = unit.id
		leader.save()
	else:
		unit = Unit.objects.get(company = leader.unitNumber)
		leader.unit_id = unit.id
		leader.save()

