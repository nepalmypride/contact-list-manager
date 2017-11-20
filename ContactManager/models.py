from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()


class EmailAddress(models.Model):
    email_address = models.EmailField()
    person = models.ForeignKey(Person)

    def __str__(self):
        return self.email_address


class PhysicalAddress(models.Model):
    address = models.CharField(max_length=500)
    person = models.ForeignKey(Person)

    def __str__(self):
        return self.address

