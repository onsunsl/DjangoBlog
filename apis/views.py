from django.shortcuts import render

# Create your views here.


from django.views import View
from django.http import JsonResponse


class TestView(View):
    def get(self, request):
        return JsonResponse(dict(code=0, data=[], msg="GET ok"))

    def post(self, request):
        return JsonResponse(dict(code=0, data=[], msg="POST ok"))
