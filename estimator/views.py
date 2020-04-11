from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from estimator.helper.estimator import estimator
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
from rest_framework_xml.renderers import XMLRenderer
from estimator.helper.file import readFile

import json

class Covid19EstimatorJson(APIView):
    def post(self, request, format=None):        
        estimate = estimator(request.data) 
        return Response(estimate, 200)


class Covid19EstimatorXML(APIView):
    renderer_classes = [XMLRenderer]
    def post(self, request, format=None):
        estimate = estimator(request.data) 
        return Response(estimate, 200)

class Covid19EstimatorLogs(APIView):
    renderer_classes = [StaticHTMLRenderer]
    def get(self, request, format=None):
        content = readFile() 
        return Response(content, 200)