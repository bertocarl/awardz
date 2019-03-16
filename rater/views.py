from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm

def NewsLetter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
    if form.is_valid():
        print('valid')
    else:
        form = NewsLetterForm()
    return render(request, 'newsletter.html', {letterForm":form})
   



