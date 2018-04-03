from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, get_user_model,logout
from django.contrib.auth import login as dj_login
from .models import Question, Choice
from .form import UserLoginForm, SignUpForm
from django.contrib.auth.models import User
'''def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'poll/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})    

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})'''
def login_view(request):
    print(request.user.is_authenticated)
    next=request.GET.get('next')
    title ="Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user= authenticate(username=username, password=password)
        dj_login(request, user)
        if next:
            return HttpResponseRedirect(next)
        return HttpResponseRedirect("/home_polls/index")

        print(request.user.is_authenticated)
    return render(request,"poll/login.html",{"form":form,"title":title})


def signup_view(request):
    title="Signup"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data.get('username'),
            password = form.cleaned_data.get('password1'), email=form.cleaned_data.get('email'))
            return HttpResponseRedirect("/home_polls/")
    form = SignUpForm()
    return render(request, 'poll/signup.html',{'form':form,"title":title})

def logout_view(request):
    logout(request)
    return render(request,"poll/home.html",{})


def home(request):
    return render(request, 'poll/home.html')

def HomeView(request):
    if request.user.is_authenticated:
        polls = Question.objects.all()
        return render(request, 'poll/index.html',{'latest_question_list':polls})        
    else:        
        return render(request, 'poll/home.html')

def login(request):
    return render(request, 'poll/login.html')    

def signupView(request):
    return HttpResponse("Hello signup page")
    #return render(request, "Hello signup page")


def index(request):
    latest_question_list = Question.objects.all()

    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)

'''class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]'''


class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/result.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:result', args=(question.id,)))