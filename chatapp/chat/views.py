from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Message
from .forms import UserForm, MessageForm, MessageEditForm

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            return redirect('chat')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def chat(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('register')
    user = User.objects.get(id=user_id)
    messages = Message.objects.all().order_by('timestamp')
    if request.method == 'POST':
        if 'edit_message_id' in request.POST:
            message_id = request.POST['edit_message_id']
            message = get_object_or_404(Message, id=message_id)
            if message.user == user:
                form = MessageEditForm(request.POST, instance=message)
                if form.is_valid():
                    form.save()
                    return redirect('chat')
        elif 'delete_message_id' in request.POST:
            message_id = request.POST['delete_message_id']
            message = get_object_or_404(Message, id=message_id)
            if message.user == user:
                message.is_delete = True
                message.save()
                return redirect('chat')
        elif 'restore_message_id' in request.POST:
            message_id = request.POST['restore_message_id']
            message = get_object_or_404(Message, id=message_id)
            if message.user == user:
                message.is_delete = False
                message.save()
                return redirect('chat')
        else:
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.user = user
                message.save()
                return redirect('chat')
    else:
        form = MessageForm()
    messages=Message.objects.exclude(is_delete=True).union(Message.objects.filter(user=user)).order_by('timestamp')
    return render(request, 'chat.html', {
        'messages': messages,
        'form': form,
        'user': user
    })