from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')
    
@login_required(login_url='/accounts/login/')
def NewsLetter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
    if form.is_valid():
        print('valid')
    else:
        form = NewsLetterForm()
    return render(request, 'newsletter.html', {"NewsLetterForm":form})
   



