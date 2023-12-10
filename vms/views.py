from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods, require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Vendor, Performance, PurchaseOrder
from.serializers import PerformanceSerializer, PurchaseOrderSerializer, VendorReadSerializer, VendorWriteSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the vendor index.")

#get and create vendors
@csrf_exempt
@api_view(["GET", "POST"])
def vendors(request):
    if request.method == "GET":
        vendor = Vendor.objects.all()
        serializer = VendorReadSerializer(vendor, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = request.data
        serializer = VendorWriteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse("something bad happened")

#get and update vendor
@csrf_exempt
@api_view(["GET", "POST"])
def vendorbyid(request):
    if request.method == "GET":
        vendor_code = request.GET.get('vendor_code', None)
        if vendor_code is not None:
            try:
                vendor = Vendor.objects.get(vendor_code=vendor_code)
                serializer = VendorSerializer(vendor, many=True)
                return JsonResponse(serializer.data, safe=False)
            except:
                return JsonResponse({"error":"vendor not found"}, status=404)
        else:
            return JsonResponse({"error":"vendor code parameter missing!"}, status=404)
          
    elif request.method == "POST":
        data = request.data
        serializer = VendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse("something bad happened")