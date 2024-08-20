"""
views for the home page
"""
# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class SiteIndex(View):
    """
    CBV for site index
    """
    def get(self, request):
        """
        site index handler for GET
        """
        return HttpResponse("Login")