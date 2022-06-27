from django.shortcuts import render
import pandas as pd
from checkout.models import OrderLineItem
from django.db.models import Count
from .models import Review
# Create your views here.


def index(request):
    """ A view to return the index page """
    data = OrderLineItem.objects.all().annotate(dcount=Count('quantity')).order_by('-quantity')
    products = []
    for row in data:
        products.append({
            'id':row.product.id,
            'category':row.product.category,
            'sku':row.product.sku,
            'name':row.product.name,
            'brand':row.product.brand,
            'description':row.product.description,
            'price':row.product.price,
            'rating':row.product.rating,
            'image_url':row.product.image_url,
            'image':row.product.image.url
        })

    products_df = pd.DataFrame(products)

    bool_series = products_df.duplicated()
    products_df_dup = products_df[~bool_series]
  
    context = {
        'products':products_df_dup.head(4).to_dict('records')
    }
    

    return render(request, 'home/index.html',context)
