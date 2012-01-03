# -*- coding: utf-8 -*-

import jinja2 as j2
import lxml.html
from lxml.html import builder as html


@j2.contextfunction
def prev_li(context):
    prev_classes = ['prev']
    if not context['offset'] > 0:
        prev_classes.append('disabled')
    prev = html.LI(
        html.A(
            u"← Previous",
            href="#"
        ),
        {'class': " ".join(prev_classes)},
    )
    return prev

@j2.contextfunction
def next_li(context):
    next_classes = ['next']
    if not context['total'] > (context['offset'] + context['limit']):
        next_classes.append('disabled')
    next = html.LI(
        html.A(
            u"Next →",
            href="#"
        ),
        {'class': " ".join(next_classes)},
    )
    return next

def page_counter(context):
    total = context['total']
    offset = context['offset']
    limit = context['limit']
    current = 0
    page = 0
    while current < total:
        start = current + 1
        end = current + limit
        if current <= offset < end:
            active = True
        else:
            active = False
        current = current + limit
        page = page + 1
        yield dict(
            page=page,
            start=start,
            end=end,
            active=active)
