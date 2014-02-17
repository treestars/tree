from pyramid.view import view_config
import atom.data
import gdata.data
import gdata.contacts.client
import gdata.contacts.data
from oauth2client.client import flow_from_clientsecrets

@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {'project': 'Tree'}


@view_config(route_name="menu", renderer='templates/menu.jinja2')
def menu(request):
    return {}


@view_config(route_name="about", renderer='templates/about.jinja2')
def about(request):
    return {}


@view_config(route_name="contact", renderer='templates/contact.jinja2')
def contact(request):
    return {}


@view_config(route_name="signin", renderer='templates/signin.jinja2')
def signin(request):
    return {}

@view_config(route_name="newsletter_signup", renderer='json')
def newsletter_signup(request):
   import ipdb; ipdb.set_trace()
   flow = flow_from_clientsecrets('/home/kaboom/tree/oauth/client_secret.json',
		       scope='https://www.googleapis.com/auth/contacts',
		       redirect_uri='http://www.treestarscollective.com/')
   gd_client = gdata.contacts.client.ContactsClient()
   new_contact = gdata.contacts.data.ContactEntry()
   new_contact.email.append(gdata.data.Email(address="test@test.com", primary='true'))
   contact_entry = gd_client.CreateContact(new_contact)
   return {} 


@view_config(route_name="signup", renderer='templates/signup.jinja2')
def signup(request):
    return {}
