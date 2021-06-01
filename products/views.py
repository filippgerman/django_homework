from django.shortcuts import render
import datetime

def main(request):
    data = {
        'creator': 'German Filipp',
        'date': datetime.datetime.now()
    }
    return render(request, 'products/index.html', data)


def products(request):
    data = {
        'slider': [
            {'img':'img/controll.jpg'},
            {'img':'img/controll1.jpg'},
            {'img':'img/controll2.jpg'},
        ],
        'goods':[
        {
            'title': "стул повышенного качества",
            'text': "не оторваться",
            'img': "img/product-11.jpg"
        },
        {
            'title': "стул повышенного качества",
            'text': "не оторваться",
            'img': "img/product-21.jpg"
        },
        {
            'title': "стул повышенного качества",
            'text': "не оторваться",
            'img': "img/product-31.jpg"
        },

    ]}
    return render(request, 'products/products.html', data)


def contact(request):
    return render(request, 'products/contact.html')
