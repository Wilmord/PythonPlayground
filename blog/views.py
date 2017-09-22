from django.http import HttpResponse


def hello(request):
    name = request.GET['name']
    surname = request.GET['surname']
    response = 'Hello ' + name.title() + ' ' + surname.title()
    return HttpResponse(response)
