from django.http.response import HttpResponse, JsonResponse

def list(request):
    flight = {
        "name" : "IranAir",
        "No" : "1200",
        "capacity" : 120,
        "price" : 650000.0
    }
    return JsonResponse(flight)