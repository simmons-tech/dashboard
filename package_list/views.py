from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from django.http import HttpResponse
import json

def get_package_list(request):
	db = create_engine('postgresql://dashboard:d4shb04rd@simmons.mit.edu/sdb')

	Base = declarative_base()

	class Package(Base):
		__tablename__ = 'packages'

	 	packageid 	= Column(Integer, primary_key=True)
	 	recipient 	= Column(String) 
	 	bin 		= Column(String)
	 	checkin 	= Column(Date)
	 	checkin_by 	= Column(String)
	 	pickup 		= Column(Date)
	 	pickup_by 	= Column(String)
	 	perishable 	= Column(Boolean)

	Session = sessionmaker(bind=db)
	session = Session()

	# query db, get number of rows corresponding to a given user
	# this may be able to be made into a single sql query rather than using a dict
	pdict = {}
	for p in session.query(Package).filter(Package.pickup == None):
		if p.recipient in pdict:
			pdict[p.recipient] += 1
		else:
			pdict[p.recipient] = 1


	session.close()
	# this step is unnessary, we should just reformat frontend code, but hack hack hack!
	people = []
	for p, v in pdict.iteritems():
		people.append({'owner_name': p, 'number': v})
	
	return HttpResponse(json.dumps({'people':people}), mimetype="application/json")
