from django.http import HttpResponse
from django.http import request
from django.views.decorators.csrf import csrf_exempt

myList = []


@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.GET['name']
        surname = request.GET['surname']
        myList.append(name + ' ' + surname + '\n')
        return HttpResponse(request)


def showList(request):
    if request.method == 'GET':
        return HttpResponse(myList)
