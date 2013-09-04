### About #####################################################################
#                                                                             #
# This code is part of the Simmons Hall Dashboard project. An up-to-date      #
# version can be found at https://github.com/simmons-tech/dashboard .         #
#                                                                             #
# The project is built an maintained by Simmons Tech, a student organization  #
# at MIT. The original code was produced by Luke O'Malley '14 and             #
# Will Oursler '15                                                            #
#                                                                             #
### License and Warranty ######################################################
#                                                                             #
# Copyright 2013 Simmons Hall                                                 #
#                                                                             #
# Licensed under LGPL3 (the "License"). You may not use this work except in   #
# compliance with the License. You may obtain a copy of the License at        #
# http://opensource.org/licenses/lgpl-3.0.html .                              #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT   #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.            #
###############################################################################

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
