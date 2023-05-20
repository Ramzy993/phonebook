from django.urls import path, include
from .views import (
    ContactList,
    new_contact, contact_details
)


urlpatterns = [
    path("contacts/", ContactList.as_view(), name="contacts"),
    path("contacts/new/", new_contact, name="new"),
    path("contacts/<int:id>/details/", contact_details, name="details"),
]
