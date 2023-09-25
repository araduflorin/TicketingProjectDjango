from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
# class GeneralView:
#     template_name = 'aplicatieTicketing/general_index.html'


def general(request):
  template = loader.get_template('aplicatieTicketing/general_index.html')
  return HttpResponse(template.render())