from django.urls import path
from . import views

urlpatterns = [
    path('', views.plan_list, name="planlist"),
    path('index', views.index, name="index"),
    path('<int:plan_id>/', views.detail, name='detail'),
]
