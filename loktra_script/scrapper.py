import sys
from bs4 import BeautifulSoup
from mechanize import Browser


class Scrapper(object):
    """
    scrapper to scrap count of result and elements on a specific page based on
    choosen key and page number
    """

    def __init__(self):
        pass

    def scrapper_query1(self, key):
        """
        function to query result and result counts based on search key provided
         from user input
        :return: total count, list of elements for particular selection
        """
        base_url = 'http://www.shopping.com/womens/products'
        # url based on search key
        url_scrap = (base_url+'?'+'KW'+'='+key)
        print url_scrap
        browser = Browser()
        browser.open(url_scrap)
        soup = BeautifulSoup(browser.response(), "html.parser")
        # find total results on current page otherwise give exception
        try:
            count = soup.find('span',{'class': 'numTotalResults'})
            print count
            total = count.text.split('of')[-1]
            print "Total number of results for category " + key +" is:"+total
        except:
            print "count doesn't exists"

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
        browser = Browser()
        browser.open(url_scrap)
        soup = BeautifulSoup(browser.response(), "html.parser")
        # find results on the current page otherwise give Exception
        try:
            div_top = soup.findAll('div', {'class': 'gridItemTop'})
            for link in div_top:
                product = link.findNext("a")
                images = product.findNext('img')
                title = images.get('title', None)
                product_images = link.findNext('span', {'class': 'placeholderImg'})
                image_url = product_images.text
                if title is None or image_url is None:
                    pass
                else:
                    span_price = link.findNext("span", {'class':"productPrice toSalePrice"})
                    price = span_price.text
                    print title
                    print price
                    print image_url
        except:
            print "No result for this search"


if __name__ == '__main__':
    argv = sys.argv
    scraper = Scrapper()
    # Check if key and page is entered by user
    # i.e. User has run the program as `http://www.shopping.com/products~PG-<number>?KW=<keyword>"`
    # Call the scrapper_query2() function to print total results and elements on specified page
    if len(argv) == 3:
        key = argv[1]
        page = argv[2]
        scraper.scrapper_query2(key, page)
    # If user has entered key only
    # i.e user has run the program as http://www.shopping.com/products?KW=<keword>
    # Call the scrapper_query1() function to print total results and element on specified page
    elif len(argv) == 2:
        key = argv[1]
        scraper.scrapper_query1(key)
    else:
        print "please run again with key and parameter"


