from django.urls import path

from laptop.views import LaptopListView, create_laptop_view

urlpatterns = [
    path("", LaptopListView.as_view(), name="list-laptops"),
    path("add", create_laptop_view, name="create-laptop"),

]