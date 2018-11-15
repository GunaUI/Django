from django import template

register = template.Library()

@register.filter(name='replaceEmpty')

def replaceEmpty(value, args):
    """
    This cuts out all the values of the "arg"
    """
    return value.replace(args, '')

# register.filter('replaceEmpty', replaceEmpty)
