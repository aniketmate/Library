from django.http import HttpResponse

def func1(request):
    return HttpResponse("in func1")