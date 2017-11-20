from django.shortcuts import render, redirect
from .models import Person, EmailAddress, PhysicalAddress
import datetime


def add_contact(request):
    return render(request, './ContactManager/ContactForm.html')


def save_contact(request):
    assert request.method == "POST"
    form_data = {'emails': [], 'addresses': []}
    for field in request.POST:
        if field == "csrfmiddlewaretoken":
            continue
        else:
            if field.startswith("email"):
                form_data['emails'].append(request.POST[field])
            elif field.startswith("address"):
                form_data["addresses"].append(request.POST[field])
            else:
                form_data[field] = request.POST[field]
    this_person = Person.objects.create(first_name=form_data["first_name"],
                                        last_name=form_data["last_name"],
                                        date_of_birth=datetime.datetime.strptime(form_data['date_of_birth'],"%Y-%m-%d"),
                                        )
    this_person.save()
    for email in form_data['emails']:
        this_email = EmailAddress.objects.create(email_address=email, person=this_person)
        this_email.save()
    for address in form_data['addresses']:
        this_address = PhysicalAddress.objects.create(address=address, person=this_person)
        this_address.save()

    return render(request, "./ContactManager/ContactViewer.html", {'person_query': Person.objects.all()})


def view_all_contacts(request):
    return render(request, "./ContactManager/ContactViewer.html", {'person_query': Person.objects.all()})


def delete_contact(request, object_id):
    this_person = Person.objects.get(id=int(object_id))
    this_person.delete()
    return render(request, "./ContactManager/ContactViewer.html", {'person_query': Person.objects.all()})


def view_contacts(request):
    return render(request, "./ContactManager/ContactViewer.html", {'person_query': Person.objects.all()})


def edit_contact(request, object_id):
    this_person = Person.objects.get(id=int(object_id))
    email_query = EmailAddress.objects.filter(person=this_person)
    address_query = PhysicalAddress.objects.filter(person=this_person)
    return render(request, "./ContactManager/ContactDetail.html", {'person': this_person,
                                                                   'email_query': email_query,
                                                                   'address_query': address_query})


def change_email(request, object_id, email_id):
    this_person = Person.objects.get(id=int(object_id))
    this_email = EmailAddress.objects.get(id=email_id)
    email_query = EmailAddress.objects.filter(person=this_person)
    address_query = PhysicalAddress.objects.filter(person=this_person)
    try:
        this_email.email_address = request.GET['email']
        this_email.save()
        return render(request, "./ContactManager/ContactDetail.html", {'person': this_person,
                                                                       'email_query': EmailAddress.objects.filter(person=this_person),
                                                                       'address_query': address_query,
                                                                       'recent_change': "Email Changed"})
    except:
        return render(request, "./ContactManager/ContactDetail.html", {'person': this_person,
                                                                       'email_query': email_query,
                                                                       'address_query': address_query,
                                                                       'recent_change': "Email Change Error"})


def change_address(request, object_id, address_id):
    this_person = Person.objects.get(id=int(object_id))
    this_address = PhysicalAddress.objects.get(id=address_id)
    email_query = EmailAddress.objects.filter(person=this_person)
    address_query = PhysicalAddress.objects.filter(person=this_person)
    try:
        this_address.address = request.GET['address']
        this_address.save()
        return render(request, "./ContactManager/ContactDetail.html", {'person': this_person,
                                                                       'email_query': email_query,
                                                                       'address_query': PhysicalAddress.objects.filter(person=this_person),
                                                                       'recent_change': "Address Changed"})
    except:
        return render(request, "./ContactManager/ContactDetail.html", {'person': this_person,
                                                                       'email_query': email_query,
                                                                       'address_query': address_query,
                                                                       'recent_change': "Address Change Error"})


def change_person_info(request, object_id):
    this_person = Person.objects.get(id=object_id)
    this_person.first_name = request.GET['first_name']
    this_person.last_name = request.GET['last_name']
    this_person.date_of_birth = datetime.datetime.strptime(request.GET['date_of_birth'], "%Y-%m-%d")
    this_person.save()
    return render(request, "./ContactManager/ContactDetail.html", {'person': this_person,
                                                                   'email_query': EmailAddress.objects.filter(person=this_person),
                                                                   'address_query': PhysicalAddress.objects.filter(person=this_person),
                                                                   'recent_change': "User Name or DOB Changed"})


def search_contact(request):
    print(request.POST)
    person_query = Person.objects.filter(first_name__icontains=request.POST['search'])
    return render(request, "./ContactManager/ContactViewer.html", {'person_query': person_query})
