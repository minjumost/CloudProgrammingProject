from django.db.models import Count, Sum, DateField, Q
from django.db.models.functions import Cast
from django.utils.datetime_safe import strftime

from management.models import Sales
from datetime import datetime, timedelta, date


def best_seller():
    top_selling_products = Sales.objects.filter(date=date.today()).values('product').annotate(total_sales=Count('product')).order_by('-total_sales')[:3]
    product_list = []
    for item in top_selling_products:
        product_list.append(item['product'])
    print(product_list)
    return product_list

def best_seller_ammount():
    now = datetime.now()
    top_selling_products = Sales.objects.filter(date=date.today()).values('product').annotate(total_sales=Count('product')).order_by('-total_sales')[:3]
    sales_list = []
    for item in top_selling_products:
        sales_list.append(item['total_sales'])
    return sales_list


def sales_amount_by_hour():
    sales_list = [0] * 12
    today_selling = Sales.objects.filter(date=date.today())
    for i in today_selling:
       if 9 <= i.time.hour <= 20:
           sales_list[i.time.hour] += i.price

    return sales_list