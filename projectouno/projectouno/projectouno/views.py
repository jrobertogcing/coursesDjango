from django.shortcuts import render

#from django.http import HttpResponse

# def hello_world(request):
#     return HttpResponse("Hola primera vista")

def hello_world(request):
    return render(request, 'home.html')

def company_information(request):

    context_dict = {'text': 'esto es un texto agregado en views.py/company_information', 'number': 100, }
    return render(request, 'company_information.html', context_dict)


    