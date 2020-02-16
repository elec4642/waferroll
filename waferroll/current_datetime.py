from django.shortcuts import render
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    context = {}
    context['cu_datetime'] = now
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'current_datetime.html', context)