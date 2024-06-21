# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse("Welcome Home")
    return render(request, 'base.html')


def profile(request):
   # return HttpResponse("My Profile")
   return render(request, 'Profile.html')
   


def Tembeakenya(request):
  # return HttpResponse("Tembea Kenya")
  return render(request, 'Tembeakenya.html')


def Translate(request):
  # return HttpResponse("Translate")
  return render(request, 'Translate.html')


def Posterrand(request):
  # return HttpResponse("Post Errand")
  return render(request, 'Posterrand.html')


def Market(request):
  # return HttpResponse("Market")
  return render(request, 'Market.html')

def Login(request):
  # return HttpResponse("Market")
  return render(request, 'Login.html')




