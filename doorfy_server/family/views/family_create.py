#coding:utf-8
'''
Created on 2013-1-7

@author: wolf_m
'''
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.family.forms.family_create import CreatFamilyForm
from doorfy_server.family.models import Family, Family_User

@csrf_protect
def family_create(request):
    if request.method == 'POST': 
        createForm = CreatFamilyForm(request.POST)
        c = {'createForm':createForm}
        if createForm.is_valid() and request.user.is_authenticated():
            cd = createForm.cleaned_data
            family = Family()
            family.name = cd['name']
            family.desc = cd['desc']
            family.creator = request.user
            family.save()
            familyUser = Family_User()
            familyUser.user = request.user
            familyUser.family = family
            familyUser.save()
            return HttpResponseRedirect("/family/list/")
        else:
            return render(request, "family/create.html", c, context_instance=RequestContext(request))
        
    else:
        if request.user.is_authenticated():
            createForm = CreatFamilyForm()
            c = {'createForm':createForm}
            return render(request, "family/create.html", c, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("/")