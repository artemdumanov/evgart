from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from groups.views import all_groups, AddGroupView, add_group, GetGroup

urlpatterns = [
    path('all', all_groups),
    path('<int:id>', GetGroup.as_view()),
    path('add', AddGroupView.as_view()),
]

# /all
# /groups/all