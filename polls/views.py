from django.http import HttpResponse


def index(request):
    return HttpResponse("Ну привет мастер веб разработки!")
