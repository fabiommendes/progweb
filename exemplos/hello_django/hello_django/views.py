from django.http import HttpResponse


def test_view(resquest, n=100):
    return HttpResponse('<h1 style="color: purple">hello world, %s!</h1>' % n)
    
