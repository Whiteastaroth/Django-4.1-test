from django.urls import path
from .views import NewList, Newid, create_New, NewUpdate, NewDelete, SearchList

urlpatterns = [
    path('news_list/', NewList.as_view(), name= 'default'),
    path(' new/ <str:category>', Newid.as_view(), name= 'news_id'),


    path('create/', create_New, name= 'create'),
    path('<int:pk>/updata', NewUpdate.as_view(), name='updata'),
    path('<int:pk>/delete/', NewDelete.as_view(),name = 'delite'),
    path('search/', SearchList.as_view(), name='search'),


]