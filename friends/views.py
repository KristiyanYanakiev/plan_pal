from idlelib.rpc import request_queue

from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from friends.forms import FriendForm, FriendSearchFrom
from friends.models import Friend


def friends_list(request: HttpRequest) -> HttpResponse:
    friend_search_form = FriendSearchFrom(request.GET or None)
    friends = Friend.objects.all()

    if request.method == 'GET':
        if friend_search_form.is_valid():
            query = friend_search_form.cleaned_data['query']
            friends = Friend.objects.filter(name__icontains=query)

    context = {
        'friends': friends,
        'friend_search_form': friend_search_form
    }

    return render(request, 'friends/list.html', context)

def friend_details(request: HttpRequest, pk:int) -> HttpResponse:

    friend = get_object_or_404(Friend, pk=pk)

    context = {
        'friend': friend
    }

    return render(request, 'friends/details.html', context)

def create_friend(request: HttpRequest) -> HttpResponse:


    if request.method == 'POST':
        form = FriendForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('friends:list')
    else:
        form = FriendForm()

    context = {
            'form': form,
        }

    return render(request, 'friends/create.html', context)

def edit_friend(request: HttpRequest, pk:int) -> HttpResponse:

    friend = get_object_or_404(Friend, pk=pk)

    if request.method == 'POST':
        form = FriendForm(request.POST, request.FILES, instance=friend)
        if form.is_valid():
            instance = form.save()
            return redirect('friends:details', pk=instance.pk)
    else:
        form = FriendForm(instance=friend)

    context = {
        'friend': friend,
        'form': form
    }

    return render(request, 'friends/edit.html', context)

def delete_friend(request: HttpRequest, pk) -> HttpResponse:
    friend = get_object_or_404(Friend, pk=pk)

    if request.method == 'POST':
        friend.delete()
        return redirect('friends:list')

    context = {
        'friend': friend
    }

    return render(request, 'friends/delete.html', context)