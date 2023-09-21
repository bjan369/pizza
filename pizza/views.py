from django.shortcuts import render

def templateHello(request):
    return render(request, 'hello.html')