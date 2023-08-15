
from django.shortcuts import render
from django.views.generic import ListView

from laptop.forms import LaptopForm

from laptop.models import Laptop


def list_laptops_view(request):
    laptops = [{
        "model": "ZenBook",
        "brand": "Asus"
    }, {
        "model": "MacBookPro",
        "brand": "Apple"

    }]
    return render(request, "laptop/laptop_list.html", {"laptops": laptops})


class LaptopListView(ListView):

    model = Laptop
    context_object_name = "laptops"


def create_laptop_view(request):
    if request.POST:
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LaptopForm()
    return render(request, "laptop/laptop_form.html", {"form": form})
