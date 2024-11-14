from django import template

register = template.Library()

@register.filter
def ms_to_min_sec(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)

    return f"{minutes:02}:{seconds:02}"