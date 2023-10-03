from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('django')

from planlist.models import Plan


# Create your views here.
def plan_list(request):
    return HttpResponse("这里是计划列表")


def index(request):
    latest_plan_list = Plan.objects.order_by("planStartTime")
    logger.info("latest_plan_list==" + str(len(latest_plan_list)))
    context = {"latest_plan_list": latest_plan_list}
    # template = loader.get_template("plan/index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "plan/index.html", context)


def detail(request, plan_id):
    try:
        plan = Plan.objects.get(id=plan_id)
    except:
        raise Http404(404, "No plans")
    return render(request, "plan/detail.html", {'plan': plan})
