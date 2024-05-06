from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response 
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return VendorSerializer
        return VendorSerializer

    def get_queryset(self):
        queryset = Vendor.objects.all()
        return queryset

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        return queryset

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

    def get_queryset(self):
        queryset = HistoricalPerformance.objects.all()
        return queryset
