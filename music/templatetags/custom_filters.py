from django import template

register = template.Library()

# Convert the track duration from ms to display as (min:sec). e.g. 264473 milleseconds to 4:24
@register.filter
def ms_to_min_sec(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)

    return f"{minutes:02}:{seconds:02}"