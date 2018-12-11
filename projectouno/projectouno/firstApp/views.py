from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from.models import Course, Lesson

# def course_list(request):
#     firstApp = Course.objects.all()
#     response = ', '.join([str(course) for course in firstApp])

#     return HttpResponse(response)

def course_list(request):
    firstApp = Course.objects.all()
    return render(request, 'firstApp/course_list.html', {'firstApp': firstApp}) #aqui se pasa un diccionario con las variables


def course_detail(request, pk):
    #course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'firstApp/course_detail.html', {'course': course})

def lesson_detail(request, course_pk, lesson_pk):
    lesson = get_object_or_404(Lesson, course_id = course_pk, pk = lesson_pk)
    return render(request, 'firstApp/lesson_detail.html', {'lesson': lesson})
