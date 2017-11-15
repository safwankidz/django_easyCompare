from django.http import HttpResponse
from urllib.request import urlopen as uReq
from .models import PageCrawl, SearchItem
from bs4 import BeautifulSoup as soup
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
import logging
import requests


#main homepage
def first(request):
    all_page = PageCrawl.objects.all()
    return render(request,'page/homepage.html',{'all_page' : all_page})


#search main page
def home(request):
    page = PageCrawl.objects.all()
    return render(request,'page/index.html',{'all_page':page})


#insert into PageCrawl
def insert(request):
    my_url = 'https://testwebsite.com/search/products/?query=iphone'
    page_instance = PageCrawl.objects.create(info="test",page_url=my_url)
    return HttpResponse("<h1> Meh </h1>")


#page for each website
def details(request,page_id):
    webpage = get_object_or_404(PageCrawl,page_id=page_id)
    return render(request,'page/detail.html',{'webpage': webpage})


#insert data from scrap into model
def store(request):
    userkeyword = request.POST.get('userkeyword')
    # userCategory = input('Enter category first :')
    # userKeyword = input('Enter keyword to search : ')
    # different things different it last code
    # frontMudahURL = 'https://www.mudah.my/malaysia/'
    # lastMudahURL = '-for-sale'
    # fLastMudahURL = '?lst=0&fs=1&w=3&cg=0&q='
    # sLastMudahURL = '&so=1&st=s'
    # concatURL = frontMudahURL + userKeyword + lastMudahURL + fLastMudahURL + userKeyword + sLastMudahURL
    # my_url = concatURL

    # # opening up connection, grabbing the page
    # uClient = uReq(my_url)
    # page_html = uClient.read()
    # uClient.close()

    # # html parsing
    # page_soup = soup(page_html, "html.parser")

    # #page3 = PageCrawl.objects.get(pk=3)
    # page3 = get_object_or_404(PageCrawl,pk=3)

    # containers = page_soup.findAll("div", {"class": "top_params_col1"})

    # for container in containers:
    #     brandprice = container.findAll("div", {"class": "ads_price"})
    #     brandpricelist = brandprice[0].text.strip()
    #     brandname = container.h2.a["title"]

    #     item_instance = SearchItem.objects.create(price=brandpricelist, title=brandname,page=page3 )
    print(userkeyword)
    return HttpResponse("<h1> muahahahaha </h1>")


def renders(request):
    all_page = PageCrawl.objects.all()
    return render(request,'page/index.html',{'all_page': all_page})


#template example - replace with render
#def template(request):
#    all_page = PageCrawl.objects.all()
#    templates = loader.get_template('page/index.html')
#    return HttpResponse(templates.render({'all_page':all_page,},request))

#Http404 example - replace with getObjectOr404
    #try:
    #    webpage = PageCrawl.objects.get(page_id=page_id)
    #except PageCrawl.DoesNotExist:
    #    raise Http404('This page does not exists')

#dynamic page example - oreplace with template.render
# print(all_page)
#    html = ''
#    for pageCrawl in all_page:
#        url = '/search/'+str(pageCrawl.page_id)+'/'
#        html += '<a href ="' + url + '"> '+str(pageCrawl.info)+' </a> <br> '
#    return HttpResponse(html)

