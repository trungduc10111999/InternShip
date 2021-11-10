from django.shortcuts import render

def Home(request):
    context = {}
    return render(request,'structure/Home/index.html', context)
