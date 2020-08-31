from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
# Create your views here.

# class UserPolicyList(APIView)
def homepage(request):
    return render(request, 'customer_insurance_policies/home.html',{})
