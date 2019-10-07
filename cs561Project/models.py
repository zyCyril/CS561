# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RentOrder(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rent_order'


class RenterAccount(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    balance = models.FloatField(blank=True, null=True)
    rented_warehouse = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'renter_account'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Warehouse(models.Model):
    warehouse_id = models.IntegerField(primary_key=True)
    warehouse_name = models.CharField(max_length=150, blank=True, null=True)
    warehouse_size = models.IntegerField(blank=True, null=True)
    warehouse_desc = models.CharField(max_length=254, blank=True, null=True)
    warehouse_image = models.CharField(max_length=255, blank=True, null=True)
    warehouse_price = models.FloatField(blank=True, null=True)
    warehouse_category = models.CharField(max_length=150, blank=True, null=True)
    warehouse_isavailable = models.IntegerField(db_column='warehouse_isAvailable', blank=True, null=True)  # Field name made lowercase.
    warehouse_currentowenr_use_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse'
