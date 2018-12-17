from django import template

from firstApp.models import Course

register = template.Library()

@register.simple_tag
def last_course():
    '''Obtiene el ultimo curso puesto en la libreria'''
    return Course.objects.latest('created_at')

@register.filter(name='cutString')
def cutString(value,arg):
    ''' This cuts out all values of "arg" form the string! '''
    return value.replace(arg,'')

