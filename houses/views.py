from django.shortcuts import render, get_object_or_404
from .models import House
from orders.forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def list(request):
    houses = House.objects.all()
    return  render(request, "houses/list.html", {"houses": houses})

def detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
    form = OrderForm(request.POST or None, initial={
        "house": house
    })

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{}?sended=True".format(reverse("house", kwargs={"house_id": house.id})))

    return render(request, "houses/detail.html", {
        "house": house,
        "form": form,
        "sended": request.GET.get("sended", False)
    })
