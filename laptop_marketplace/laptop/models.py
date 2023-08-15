from django.db import models


class StorageLocation(models.Model):
    address = models.CharField(max_length=255, blank=False, unique=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Vendor(models.Model):
    name = models.CharField(max_length=40, blank=False, unique=True)


class Laptop(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    storage_location = models.OneToOneField(StorageLocation, on_delete=models.PROTECT, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    vendors = models.ManyToManyField(Vendor)
