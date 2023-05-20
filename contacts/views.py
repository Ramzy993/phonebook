from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact, PhoneNum
from django.views.generic import ListView


class ContactList(ListView):
    context_object_name = "contacts"
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Contact.objects.filter(created_by=self.request.user)
        return Contact.objects.filter(created_by=None)


@login_required(login_url="/login/")
def contact_details(request, id):
    contact = get_object_or_404(Contact, id=id)
    context = {"contact": contact}
    return render(request, "contacts/contact_details.html", context)


@login_required(login_url="/login/")
def new_contact(request):
    if request.method == "POST":
        created_by = request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phones = request.POST.get("phones").split(',')
        email = request.POST.get("email")

        contact = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            created_by=created_by
        )
        contact.save()

        for phone in phones:
            phone_num = PhoneNum.objects.create(number=phone, contact=contact)
            phone_num.save()

        return redirect("/contacts/")

    return render(request, "contacts/new_contact.html")