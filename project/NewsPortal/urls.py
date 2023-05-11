from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsList.as_view(), name='news_home'),
    path('<int:pk>', views.NewsId.as_view(), name='news_id'),  # переход по динамическим страницам
    path('create/', views.create, name='create'),  # переход на страницу добавления записи
    path('search/', views.SearchList.as_view(), name='search'),
    path('<int:pk>/updata', views.NewsUpdataView.as_view(), name='news_updata'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('subscriptions/', views.subscriptions.as_view(), name='subscriptions'),
]