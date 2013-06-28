from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )


@view_config(route_name='samples', renderer='samples.mak')
def samples(request):
    10 / 0
    return {'project': 'brewcontrol'}

@view_config(route_name='settings')
def settings(request):
    return Response("not implemented", status=500)

@view_config(route_name='shutdown')
def shutdown(request):
    return Response("not implemented", status=500)

@view_config(route_name='home', renderer='home.mak')
def home(request):
    return {}
