from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from groups.models import Group


def all_groups(request):
    return HttpResponse(render(request, 'all_groups.html', {'groups': Group.objects.all()}))


# post and get
# function-based view
def add_group(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'add-group.html'))
    elif request.method == 'POST':
        name = request.POST.get('name')
        start_date = request.POST.get('startDate')
        max_students = request.POST.get('maxStudents')

        group = Group()

        group.name = name
        group.start_date = start_date
        group.max_students = max_students

        group.save()

    return redirect('/groups/all')

# from django.views.generic.list import ListView
# from django.utils import timezone
#
# class GroupListView(ListView):
#
#     model = Group
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# class-based view
class AddGroupView(View):
    def get(self, request):
        return HttpResponse(render(request, 'add-group.html'))

    def post(self, request):
        name = request.POST.get('name')
        start_date = request.POST.get('startDate')
        max_students = request.POST.get('maxStudents')

        group = Group()

        group.name = name
        group.start_date = start_date
        group.max_students = max_students

        group.save()

        return redirect('/groups/all')
