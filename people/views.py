from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from django.http import HttpResponse, Http404
import json

password = 'pass'

def get_people(request):
	db = create_engine('postgresql://dashboard:'+password+'@simmons.mit.edu/sdb')

	Base = declarative_base()

	class Resident(Base):
		__tablename__ = 'directory'
		username = Column(String, primary_key = True)

		firstname = Column(String)
		lastname = Column(String)
		room = Column(String)
		phone = Column(String)
		year = Column(Integer)
		cellphone = Column(String)
		homepage = Column(String)
		#home_city = Column(String)
		#home_state = Column(String)
		home_country = Column(String)
		#quote = Column(String)
		favorite_category = Column(String)
		favorite_value = Column(String)
		private = Column(Boolean)
		type = Column(String)
		email = Column(String)
		lounge = Column(String)
		title = Column(String)
		loungevalue = Column(Integer)
		showreminders = Column(Boolean)
		guest_list_expiration = Column(String)

	Session = sessionmaker(bind=db)
	session = Session()

	# Make a full list of people of interest...
	people = []
	for person in session.query(Resident):
		if person.private:
			continue
		people.append( {
			'kerberos'	:person.username,
			'firstname'	:person.firstname,
			'lastname'	:person.lastname,
			'room'		:person.room,
			'year'		:person.year,
			'title'		:person.title,
			'email'		:person.email,
			} )

		
	session.close()

	return people

def get_person(request,username="test"):
	people = get_people(request)
	for person in people:
		if person['kerberos'] == username:
			return HttpResponse(json.dumps({'person':person}), content_type="application/json")
	raise Http404

def get_active_usernames(request):

	db = create_engine('postgresql://dashboard:'+password+'@simmons.mit.edu/sdb')

	Base = declarative_base()

	people = get_people(request)

	class ActiveUsernames( Base ):
		__tablename__ = 'sds_users_all'
	
		username = Column( String, primary_key = True )
		active = Column( Boolean )

	Session = sessionmaker(bind=db)
	session = Session()
	
	# Figure out which users are active...
	active = {}
	for username in session.query(ActiveUsernames):
		active[ username.username ] = username.active

	usernames = []
	for person in people:
		if active[ person['kerberos'] ]:
			usernames.append( person['kerberos'] )

	return HttpResponse(json.dumps({'usernames':usernames}), content_type="application/json")
