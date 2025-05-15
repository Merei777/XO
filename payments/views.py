from django.http import HttpResponse

def home(request):
    return HttpResponse("Это главная страница для платежей.")
