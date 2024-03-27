from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

count_about = 0
count_index = 0


def index(request):
    global count_index
    count_index += 1
    logger.info(f'Count_index = {count_index}')
    return HttpResponse("""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
            Title<br>My first<br>Django app<br>
            </body>
            </html>""")


def about(request):
    global count_about
    count_about += 1
    logger.info(f'Count = {count_about}')
    return HttpResponse("""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
            My name is<br>Lida<br>
            </body>
            </html>""")
