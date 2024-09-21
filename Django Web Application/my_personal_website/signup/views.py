from django.http import HttpResponse
from django.template import loader

def signup(request):
  template = loader.get_template('user_reg.html')
  return HttpResponse(template.render())