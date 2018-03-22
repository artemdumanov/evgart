from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from groups.views import all_groups, AddGroupView, add_group

urlpatterns = [
    path('all', add_group),
    path('add', AddGroupView.as_view()),
]

# /all
# /groups/all