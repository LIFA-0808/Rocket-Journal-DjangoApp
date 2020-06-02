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
    path('research/new_topic/', views.new_topic, name="new_topic"),

    # Delete_Topic
    re_path(r'^delete_topic/(?P<topic_id>\d+)/$', views.delete_topic, name="delete_topic"),

    # New_Record
    re_path(r'^research/(?P<topic_id>\d+)/new_record/$', views.new_record, name="new_record"),

    # Edit_Record
    re_path(r'^edit_record/(?P<record_id>\d+)/$', views.edit_record, name="edit_record"),

    # Delete_Record
    re_path(r'^delete_record/(?P<record_id>\d+)/$', views.delete_record, name="delete_record"),
]