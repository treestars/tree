from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {'project': 'Tree'}


@view_config(route_name="menu", renderer='templates/menu.jinja2')
def menu(request):
    return {}


@view_config(route_name="about", renderer='templates/menu.jinja2')
def about(request):
    return {}


@view_config(route_name="contact", renderer='templates/menu.jinja2')
def contact(request):
    return {}


@view_config(route_name="signin", renderer='templates/signin.jinja2')
def signin(request):
    return {}


@view_config(route_name="signup", renderer='templates/signup.jinja2')
def signup(request):
    return {}
