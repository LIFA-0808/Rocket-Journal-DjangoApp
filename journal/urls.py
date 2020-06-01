from django.urls import path, re_path

from . import views

"""Defines URL schemes for users"""

app_name = 'journal'
urlpatterns = [
    path('', views.index_view, name="index"),
    path('research/', views.research_view, name="research"),

    # Research_Section
    # r'^edit_record/(?P<record_id>\d+)/$'
    re_path(r'^research/(?P<topic_id>\d+)/$', views.section_view, name="section"),

    # New_Topic
    path('journal/new_topic/', views.new_topic, name="new_topic"),

    # New_Record
    path('journal/new_record/', views.new_record, name="new_record"),

    # Edit_Record
    re_path(r'^edit_record/(?P<record_id>\d+)/$', views.edit_record, name="edit"),

    # Delete_Record
    re_path(r'^delete_record/(?P<record_id>\d+)/$', views.delete_record, name="delete"),
]