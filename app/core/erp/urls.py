from django.urls import path
from core.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/uno/', CategoryListView.as_view(), name='category_list'),
    path('category/dos/', category_list, name='category_list2'),
]
