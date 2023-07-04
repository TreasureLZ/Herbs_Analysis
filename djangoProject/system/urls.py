from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('chart1/', views.chart1, name='chart1'),
    path('chart2/', views.chart2, name='chart2'),
    path('chart3/', views.chart3, name='chart3'),
    path('chart4/', views.chart4, name='chart4'),
    path('chart5/', views.chart5, name='chart5'),
]
