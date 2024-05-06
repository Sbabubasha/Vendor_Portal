from django.db import models
import uuid
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete
from django.core.exceptions import ValidationError

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, default=uuid.uuid4, editable=False)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


    

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    vendor = instance.vendor
    if instance.status == 'completed':
        vendor.on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
        vendor.fulfillment_rate = calculate_fulfillment_rate(vendor)
        vendor.save()
    if instance.quality_rating is not None:
        vendor.quality_rating_avg = calculate_quality_rating_avg(vendor)
        vendor.save()





@receiver(pre_delete, sender=PurchaseOrder)
def delete_update_vendor_metrics(sender, instance, **kwargs):
    vendor = instance.vendor
    vendor.on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
    vendor.quality_rating_avg = calculate_quality_rating_avg(vendor)
    vendor.fulfillment_rate = calculate_fulfillment_rate(vendor)
    vendor.save()

def calculate_on_time_delivery_rate(vendor):
    completed_orders = vendor.purchaseorder_set.filter(status='completed').count()
    if completed_orders == 0:
        return 0
    on_time_orders = vendor.purchaseorder_set.filter(status='completed', delivery_date__lte=models.F('acknowledgment_date')).count()
    return (on_time_orders / completed_orders) * 100

def calculate_quality_rating_avg(vendor):
    completed_orders_with_rating = vendor.purchaseorder_set.filter(status='completed', quality_rating__isnull=False).count()
    if completed_orders_with_rating == 0:
        return 0
    total_rating = sum(order.quality_rating for order in vendor.purchaseorder_set.filter(status='completed', quality_rating__isnull=False))
    return total_rating / completed_orders_with_rating

def calculate_fulfillment_rate(vendor):
    total_orders = vendor.purchaseorder_set.all().count()
    if total_orders == 0:
        return 0
    completed_orders = vendor.purchaseorder_set.filter(status='completed').count()
    return (completed_orders / total_orders) * 100