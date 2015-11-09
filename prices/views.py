from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import College

def index(request):
    template = loader.get_template('prices/index.html')
    college_list = College.objects.order_by('college_name')

    context = RequestContext(request, {'college_list': college_list})
    return HttpResponse(template.render(context))
