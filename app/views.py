from django.shortcuts import redirect, render
from .forms import CrispyForm
from django.http import HttpResponse


def home(request):
    #referencing the Form
    #if it comes with a post request or a get request
    form = CrispyForm(request.POST or None)
    #if it is a post request
    if request.method == 'POST':
        #check if the form is valid enough to be saved
        if form.is_valid():
            #to save the form
            form.save()
            return redirect ('home')
        else:
            return HttpResponse('invalid form')
    context = {
        'form': form
    }
    return render(request, 'app/home.html', context)
        
