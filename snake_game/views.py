import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Max
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from snake_game.forms import SnakeUserCreationForm
from snake_game.models import Score


def home(request):
    if request.user.is_authenticated() == False:
        return redirect("register")

    score = Score.objects.filter(user=request.user).aggregate(Max('score'))
    highscore = score['score__max']

    return render(request, 'index.html', {'highscore':highscore})

def dome(request):
    return render(request, 'new.html')

def register(request):
    if request.method == 'POST':
        form = SnakeUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect("/")
    else:
        form = SnakeUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@csrf_exempt
def update_score(request):
    data = json.loads(request.body)
    score = Score.objects.create(user=request.user, score=data)
    print score


def profile(request):
    score = Score.objects.filter(user=request.user)
    return render(request, 'profile.html', {'score': score})

def leaderboard(request):
    score = Score.objects.all().order_by('-score')
    return render(request ,'leaderboard.html', {'score': score})