from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from manager.models import Task, TaskType


@login_required
def index(request):
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "task_count": Task.objects.count(),
        "task_type_count": TaskType.objects.count(),
        "worker_count": get_user_model().objects.count(),
        "num_visits": num_visits
    }

    return render(request, "manager/index.html", context=context)
