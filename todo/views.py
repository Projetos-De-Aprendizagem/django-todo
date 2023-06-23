from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'base.html'
    return render(request, template)