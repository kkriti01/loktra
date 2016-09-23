from django.shortcuts import render
from django.views.generic import View
from django.http import Http404

from models import Product, Result
from helpers import Scrapper


class HomeView(View):

    def get(self, request, *args, **kwargs):
        key = request.GET.get('key', '')
        page = request.GET.get('page')
        if key == '' and page == '':
            raise Http404("enter either key or page to search")
        scrapper = Scrapper()
        if key and page == '':
            scrapper.scrapper_query1(key)
            total = Result.objects.get(key=key)
            return render(request, "home.html", {'total': total.count})
        elif key and page:
            scrapper.scrapper_query2(key, page)
            result = Product.objects.filter(key=key).filter(page=page)
            return render(request, "home.html", {'result': result})
        else:
            return render(request, "home.html")