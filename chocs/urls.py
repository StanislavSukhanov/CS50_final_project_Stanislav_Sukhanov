from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_idex_page, name='index'),
    path('chocsets/', views.SetsListView.as_view(), name='sets-list'),
    path('chocset/<int:pk>', views.SetsDetailView.as_view(), name='set-detail'),
    path('drawbars/', views.BarListView.as_view(), name='bar-list'),
    path('drawbar/<int:pk>', views.BarDetailView.as_view(), name='bar-detail'),
]

urlpatterns += [
    path('basket_adding/', views.basket_adding, name='basket_adding')
]
