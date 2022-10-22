# Having all urls for this app organized here

from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/',views.product_detail_view)
]