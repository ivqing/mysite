#from django.http import HttpResponse
#from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:2]
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {
    #    'latest_poll_list': latest_poll_list,
    #    })
    #return HttpResponse(template.render(context))

    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    #return HttpResponse("You're looking at poll %s." % poll_id)
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExit:
        raise Http404
    return render(request, 'polls/detail.html', {'poll':poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
