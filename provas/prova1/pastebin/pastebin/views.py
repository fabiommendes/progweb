from django.shortcuts import render, get_object_or_404


def index(request):
    ctx = {}
    return render(request, 'pastebin/index.jinja2', ctx)


def paste(request, id):
    ctx = {}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    ctx = {'pastes': []}
    return render(request, 'pastebin/paste-language.jinja2', ctx)