from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.
@api_view(['GET'])
@parser_classes([JSONParser])
def Sample(req):
    try:
        data=req.data
        return JsonResponse({"data":"hello"})
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@parser_classes([JSONParser])
def Sample1(req):
    try:
        print(dir(req))
        print(req.data)
        data =req.data
        # data=json.loads(req.data)
        print(data)
        print(type(data))
        return JsonResponse(data)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)