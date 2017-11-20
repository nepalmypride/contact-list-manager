"""ContactList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ContactManager.views import *
urlpatterns = [
    url(r'^$', add_contact),
    url(r'add-contact/$', add_contact),
    url(r'view-contacts', view_all_contacts),
    url(r'save-contact/$', save_contact),
    url(r'view-contacts/$', view_contacts),
    url(r'delete-contact/(\d+)/$', delete_contact),
    url(r'edit-contact/(\d+)/$', edit_contact),
    url(r'search-contact/$', search_contact),
    url(r'change-email/(\d+)/(\d+)/$', change_email),
    url(r'change-address/(\d+)/(\d+)/$', change_address),
    url(r'change-person-info/(\d+)/$', change_person_info),
]
