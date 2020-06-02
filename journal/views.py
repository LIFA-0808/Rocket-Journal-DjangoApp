from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TopicForm, RecordForm
from .models import Topic, Record
from account.models import Account


def index_view(request):
    """Home page of RJ app"""
    return render(request, 'journal/index.html')


def research_view(request):
    """Displays a list of research topics"""
    context = {}
    topics = Topic.objects.all()
    context['topics'] = topics
    if request.method != 'POST':
        form = TopicForm
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:research'))
    context['form'] = form
    return render(request, 'journal/research.html', context)


def section_view(request, topic_id):
    context = {}
    topic = Topic.objects.get(id=topic_id)
    records = topic.record_set.order_by('-date_added')
    context['topic'] = topic
    context['records'] = records
    return render(request, 'journal/section.html', context)


def new_topic(request):
    """Adding a new topic"""
    if request.method != 'POST':
        form = TopicForm
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:research'))
    context = {'form': form}
    return render(request, 'journal/new_topic.html', context)


def delete_topic(request, topic_id):
    """Delete record"""
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    return HttpResponseRedirect(reverse('journal:research'))


def new_record(request, topic_id):
    """Adding a new record"""
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = RecordForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        topic = Topic.objects.get(id=topic_id)
        obj.author = author
        obj.topic = topic
        obj.save()
        form = RecordForm()
        return redirect('journal:research')

    context['form'] = form
    return render(request, 'journal/new_record.html', context)


def edit_record(request, record_id):
    """Edits an existing record"""
    record = Record.objects.get(id=record_id)

    if request.method != 'POST':
        # Original request; the form is filled with the data of the current record
        form = RecordForm(instance=record)
    else:
        # Sending POST data; process data
        form = RecordForm(instance=record, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:research'))

    context = {'record': record, 'form': form}
    return render(request, 'journal/edit_record.html', context)


def delete_record(request, record_id):
    """Delete record"""
    record = Record.objects.get(id=record_id)
    record.delete()
    return HttpResponseRedirect(reverse('journal:research'))
