from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sign_in


def webserver(request):
    websever = Sign_in.objects.all().values()
    template = loader.get_template("all_webservers.html")
    context = {
        "mywebservers": websever,
    }
    return HttpResponse(template.render(context, request))


def details(request, slug):
    webserver = Sign_in.objects.get(slug=slug)
    template = loader.get_template("details.html")
    context = {
        "webserver": webserver,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())


def action_page(request):
    template = loader.get_template("action_page.html")
    context = {
        "Jambscore": 320,
    }
    return HttpResponse(template.render(context, request))


def template(request):
    mydata = Sign_in.objects.all().values()
    template = loader.get_template("template.html")
    context = {
        'mywebservers': mydata,
    }
    return HttpResponse(template.render(context, request))
