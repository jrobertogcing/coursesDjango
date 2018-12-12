from django.shortcuts import render

#from django.http import HttpResponse

# def hello_world(request):
#     return HttpResponse("Hola primera vista")

def hello_world(request):
    return render(request, 'home.html')

def company_information(request):
    return render(request, 'company_information.html')


    