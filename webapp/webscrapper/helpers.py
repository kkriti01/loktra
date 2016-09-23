import sys
from bs4 import BeautifulSoup
import requests
from django.http import Http404

from models import Product, Result


class Scrapper(object):
    """
    scrapper methods
    """
    def __init__(self):
        pass

    def scrapper_query1(self, key):
        """
        function to query result and result counts based on search key provided
         from user input
        :return: total count, list of elements for particular selection
        """
        print key
        base_url = 'http://www.shopping.com/womens/products'
        # url based on search key
        url_scrap = (base_url+'?'+'KW'+'='+key)
        print url_scrap
        response = requests.get(url_scrap)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        # find total results on current page otherwise give exception
        try:
            count = soup.find('span',{'class': 'numTotalResults'})
            print count
            total = count.text.split('of')[-1]
            result_obj, created = Result.objects.get_or_create(
                count=total,
                key=key)
            result_obj.save()
            print "Total number of results for category " + key + " is:" + total
        except:
            raise Http404('No  result found')

    def scrapper_query2(self, key, page):
        """
        function to query result and result counts based on page number and search key provided
        from user input
        :return: total count, list of elements for particular selection
        """
        base_url = 'http://www.shopping.com/products'
        # url based on page number and search key given
        url_scrap = (base_url + '~' + 'PG' + '-' + page + '?' + 'KW' + '=' + key)
        print url_scrap
        response = requests.get(url_scrap)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        product_list = []
        # find results on the current page otherwise give Exception
        try:
            div_top = soup.findAll('div', {'class': 'gridItemTop'})
            for link in div_top:
                product = link.findNext("a")
                images = product.findNext('img')
                title = images.get('title', None)
                product_images = link.findNext('span', {'class': 'placeholderImg'})
                image_url = product_images.text
                if title is None or image_url is None or title == '' or  image_url == '':
                    pass
                else:
                    span_price = link.findNext("span", {'class':"productPrice toSalePrice"})
                    price = span_price.text
                    #print title
                    #print price
                    #print image_url
                    result = {'title': title,
                              'price': price,
                              'image': image_url}
                    product_list.append(result)
                    #print product_list

        except:
            if len(product_list) > 0:
                print "No  result found"
            else:
                raise Http404('No  result found')

        for item in product_list:
            product_obj, created = Product.objects.get_or_create(
                title=item["title"],
                price=item["price"],
                image_url=item["image"],
                key=key,
                page=page
               )
            product_obj.save()

