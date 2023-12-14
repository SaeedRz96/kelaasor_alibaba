from django.http.response import HttpResponse, JsonResponse

def welcome(request):
    return HttpResponse("Hello World!")

def about(request):
    return HttpResponse("Here is about page!")

def flight(request):
    flight = {
        "name" : "IranAir",
        "No" : "1200",
        "capacity" : 120,
        "price" : 650000
    }
    return JsonResponse(flight)