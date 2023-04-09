from django.shortcuts import render
from cars.models import Car, Driver, seperate
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def car_detail(request, pk):
    owner = Driver.objects.get(pk=pk)
    cars = Car.objects.filter(owner_id=owner.id)
    return JsonResponse({
        "cars": cars[0].make,
    })


@csrf_exempt
def sep(request):
    if request.method == "POST":
        name = request.POST.get("name")
        sep = seperate.objects.create(name=name)
        return HttpResponse("ok")

       
    else:
        sep = seperate.objects.get(pk=1)
        return JsonResponse({
            "name": sep.name
        })
    

