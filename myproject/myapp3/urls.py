from django.urls import path
from .views import view_show_products
#
urlpatterns = [
    # path('hello/', hello, name='hello'),
    # path('hello2/', HelloView.as_view(), name='hello2'),
    path('products/<str:client_name>/', view_show_products, name='view_show_products'),
    # path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    # path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    ]
#
# from django.http import JsonResponse
#
#
# def post_detail(request, year, month, slug):
#
#     post = {
#         "year": year,
#         "month": month,
#         "slug": slug,
#         "title": "Кто быстрее создаёт списки в Python, list() или []",
#         "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python работает быстрее..."
#         }
#     return JsonResponse(post, json_dumps_params={'ensure_ascii': False})
#

