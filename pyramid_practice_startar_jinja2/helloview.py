from pyramid.view import view_config


@view_config(route_name='hello', renderer='templates/hellotemplate.jinja2')
def hello_view(request):
    return {'myData': 'myHogemoge'}
