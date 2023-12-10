from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=200)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

class PurchaseOrder(models.Model):
    po_number = models.CharField()
    vendor = models.ForeignKey(Vendor)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField()
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True)

class Performance(models.Model):
    vendor = models.ForeignKey(Vendor)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()