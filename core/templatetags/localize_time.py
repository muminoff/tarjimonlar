# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def uzbekify_daymonthyear(value):
    month_names_in_uzbek = [
            'январь', 'февраль', 'март',
            'апрель', 'май', 'июнь',
            'июль', 'август', 'сентябрь',
            'октябрь', 'ноябрь', 'декабрь'
            ]
    day, month, year = value.split('-')
    return '{day} {month}, {year} йил'.format(
            day=int(day),
            month=month_names_in_uzbek[int(month)-1],
            year=year
            )


@register.filter
@stringfilter
def uzbekify_monthyear(value):
    month_names_in_uzbek = [
            'январь', 'февраль', 'март',
            'апрель', 'май', 'июнь',
            'июль', 'август', 'сентябрь',
            'октябрь', 'ноябрь', 'декабрь'
            ]
    month, year = value.split('-')
    return '{month}, {year} йил'.format(
            month=month_names_in_uzbek[int(month)-1],
            year=year
            )
