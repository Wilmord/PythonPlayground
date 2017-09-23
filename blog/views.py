from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

# dict
dictForJason = {}

# list
personList = []


@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        name = request.GET['name']
        surname = request.GET['surname']
        personList.append(name.title() + ' ' + surname.title())
        return HttpResponse(request)


def show_list(request):
    if request.method == 'GET':
        for i in range(len(personList)):
            dictForJason[i + 1] = personList[i]
        return JsonResponse(dictForJason)
