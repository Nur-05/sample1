from django.shortcuts import render,HttpResponse

def homepage(request):
    # return render(request, 'index.html')
    return HttpResponse("hello world")


def test(request):
    return render(request, 'test.html')

def second(request):
    return HttpResponse("test 2 page")
