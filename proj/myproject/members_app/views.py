from django.shortcuts import render, redirect
from .models import Member

def input_view(request):
    return render(request, 'members_app/input.html')

def output_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        member = Member.objects.create(name=name, email=email)
        return render(request, 'members_app/output.html', {'member': member})
    else:
        return render(request, 'members_app/output.html')

def session_view(request):
    if request.method == 'POST':
        request.session['username'] = request.POST['username']
        return redirect('members_app:session')
    else:
        username = request.session.get('username', None)
        return render(request, 'members_app/session.html', {'username': username})
